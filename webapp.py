# !/usr/bin/env python
import time

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
A2 = 2
PIN = 13
def background_thread():
    """Example of how to send server generated events to clients."""
    while True:
        socketio.sleep(2)
        heaterTemp = a.analog_read(A0)
        pressure = a.analog_read(A1)
        kt = a.analog_read(A2)
        bd = 20
        socketio.emit('my_response',
                      {'data': 'Values','heaterTemp': heaterTemp, 'fr': pressure, 'kt': kt, 'bd': bd},
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
    a.set_pin_mode(PIN, 'O')
    time.sleep(1)
    if message.get('checkbox'):
        print("power ON")
        a.digital_write(PIN, 1)
    else:
        print("power OFF")
        a.digital_write(PIN, 0)


@socketio.on('temperature input', namespace='/carpi')
def handle_slider(message):
    print(message.get('value'))


@socketio.on('pressure input', namespace='/carpi')
def handle_slider(message):
    print(message.get('value'))


if __name__ == '__main__':
    print("startin application")
    # a = Arduino(serial_port='COM10')
    time.sleep(3)
    socketio.run(app, debug=True)
