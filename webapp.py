# !/usr/bin/env python
import json
import time

import math
from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit
from random import randint
from pyduino import *

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
global a

A0 = 0
A1 = 1
# A2 = 2
Power_PIN = 13
Pressure_OUT = 12
Temperature_OUT = 3



def background_thread():
    """Example of how to send server generated events to clients."""
    while True:
        socketio.sleep(2)
        heaterTemp = a.analog_read(A0)
        # print(heaterTemp)
        # heaterTemp = get_actual_temperatuer(heaterTemp)
        data = get_data()
        temperature_in = data['temperature']
        pressure_in = data['pressure']
        # print(heaterTemp,temp)
        set_heater_temperature(heaterTemp,100)
        pressure = a.analog_read(A1)
        pressure = get_actual_pressure(pressure)
        # print(pressure)
        socketio.emit('my_response',
                      {'data': 'Values','heaterTemp': heaterTemp, 'inPressure': pressure},
                      namespace='/carpi')


mesg = 'we are here...'


@app.route('/')
def index():
    speed = randint(0, 133)
    templateData = {
        'mesg': mesg,
        'speed': speed
    }
    return render_template('index.html', async_mode=socketio.async_mode, **templateData)


@socketio.on('connect', namespace='/carpi')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)


@socketio.on('power button press', namespace='/carpi')
def handle_message(message):
    a.set_pin_mode(Power_PIN, 'O')
    time.sleep(1)
    if message.get('checkbox'):
        print("power ON")
        a.digital_write(Power_PIN, 1)
    else:
        print("power OFF")
        a.digital_write(Power_PIN, 0)


@socketio.on('temperature input', namespace='/carpi')
def handle_temperature_slider(message):
    temperature = int(message.get('value'))
    data = get_data()
    data['temperature']= temperature
    with open("persist", "w") as f1:
        json.dump(data, f1)


def get_actual_temperatuer(x):
    # print("Temp_sensor_analog_reading:  ", x)
    if x>335:
        y=0
    else:
        y = 394474.6 - 3895.867 * x + 12.83176 * x ** 2 - 0.01407962 * x ** 3
    # print("Temperature_Guage_output: ",y)
    return y


def get_actual_pressure(x):
    if x<212:
        y=0
    else:
        y = 7.205e-07 * x ** 2 + 0.148 * x + -30.89
    return y


def set_heater_temperature(heater_temperature,temp_thresh):
    if(heater_temperature>temp_thresh+5):
        a.digital_write(Temperature_OUT,0)
    else:
        a.digital_write(Temperature_OUT,1)


@socketio.on('pressure input', namespace='/carpi')
def handle_pressureslider(message):
    pressure = int(message.get('value'))
    data = get_data()
    data['pressure'] = pressure
    with open("persist", "w") as f1:
        json.dump(data, f1)
    pressure = 0.004607 * pressure **2 + 1.715 * pressure + -1.033
    print(pressure)
    a.analog_write(Pressure_OUT,pressure)
    time.sleep(1)


def get_data():
    # read json file data for persisted data
    with open("persist") as f_check:
        data = json.load(f_check)
    return data


if __name__ == '__main__':
    print("startin application...")
    a = Arduino(serial_port='COM5')
    time.sleep(3)
    a.set_pin_mode(Temperature_OUT, 'O')
    a.set_pin_mode(Pressure_OUT, 'O')
    time.sleep(1)
    socketio.run(app, host='0.0.0.0',debug=False)
