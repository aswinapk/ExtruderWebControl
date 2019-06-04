Retrofit an Injection Molding Machine for Remote Access

Background

•	Why remote access to a lab equipment?
o	A remote access lab equipment can be accessed 24 hours per day, 7 days a week from any Internet connected location, without requiring staff supervision. 
o	Due to more efficient sharing of resources, institutions can satisfy laboratory demand with less equipment. Alternatively, expensive and bulky equipment can be shared and utilized more effectively.
o	Courses that traditionally had to be taught on-campus in their entirety may now offer opportunities for distance learning.
o	Students who work and study part time may also find remote laboratories helpful in balancing their commitments.
o	Many experiments can pose fire, electrical, radiation, biological and hazards to personal safety.
•	Examples of equipment for remote access?
o	Remote access 3-D printers, Remote access CNC machine, Remote access boring machines and drilling machines.

•	Pros and Cons?
o	Pros: 24 hour per day, 7 days a week access to equipment with possibility of resource sharing and task scheduling. This also enables resource access to locations where bulky and costly equipment is not affordable.
o	Cons: In case of server downtime all the stakeholders are effected. In case of any machine malfunction which might cause accidents or fire remote control may fail to have quick onsite response.
•	Objectives of this work?
o	Study the working of the injection molding machine so as to make necessary enhancements to enable remote access and control of the machine.
o	Develop a web-based User interface and host the server so that anyone in the network can access the interface and control the equipment. Integrate the web-server to Arduino microcontroller through serial communication which in turn controls the equipment.
o	Interface real-time video surveillance of the equipment to the User-Interface.

Problem to be solved – process to be automated 

•	Current physical system.
o	The initial examination of the machine reviled that the energy distribution unit was faulty and hence the machine heater was not powering on.
o	The mold nozzle had broken out and was filled with a lot of plastic material, which prevented it from being attached to the heater.

Overall Proposed System Design

•	What does the system do?
o	Injection molding machine, also known as an injection press, is a machine for manufacturing plastic products by the injection molding process. The machine melts plastic and then injects it into the mold to get desired product.
o	The system has a remote web-access interface from which you can monitor and control the temperature and pressure of the system. By varying these parameters we can determine the optimal setting for best product quality.
o	There is real-time video feed that helps us to have real-time visual feedback of the system. 

•	Sequence of operations-
o	Power on the machine and connect the pressure inlet to a compressor.
o	In any computer connected to the same network as the server open a web-browser and navigate to http://128.194.119.88:5000/ to access the UI which looks like below.  
o	Click the power button slider to turn the power on for the system.
o	Use the pressure and temperature sliders to set the desired temperature and pressure.
o	Once the desired setting are reached and the material is ready to be injected to the mold turn the valve to the right.

•	Difference from original system:
o	Remote web-interface based power ON and OFF.
o	Automatic heater temperature and pressure control based on remote web-interface.
o	Online temperature and pressure monitoring through the web-interface.
o	Real-time video feed of front and top view of the equipment.

•	What is the overall proposed system architecture?
o	The proposed architecture has a python flask based web-server that is hosted and accessible to anyone in the same network.
o	The machine is controlled electronically using a Arduino microcontroller board Which is communicating to the server through serial communication
o	The web-server also access direct feed from the two camera on the system to give real-time video feedback. 

Web Server and User Interface

•	Web server –
o	 The Web server controls the power ON and OFF of the system. Along with the power control the webserver monitors the temperature and pressure output of the equipment to display the same in an analog dial similar to the actual physical gauge. There are sliders which can be used to control the temperature and pressure of the equipment remotely.
o	The webserver is based on Flask framework. Flask is a Python web framework built with a small core and easy-to-extend philosophy. As our project requirement does not have heavy requirements we will be using this light weight framework to host our web-server. The user interface is built using simple HTML5
o	 Why this layout?
This layout was chosen to make the user interface as identical to the physical equipment as possible. The analog gauges give the exact feel of that on the machine.
The camera views are for visual feedback on what is happening and will help in assisting the user.

o	 What can user do?
	The user can power ON and OFF the equipment.
	User has control over the pressure output and also the temperature output which can be done using the corresponding sliders.
	User gets a real-time remote feedback video of the equipment on the interface

Hardware Design and Retrofit
•	Add on components:
o	Solid state Relay: 
o	Electromagnetic  Relay:
o	Proportional pressure control valve (SMC)
o	¼ pneumatic male to male connectors:
o	Cameras:
o	Arduino:
o	Power supply:
o	K-type thermocouple instrumentation amplifier:

