# salem-candy-dispenser
Halloween candy dispenser in the shape of a witch's brew

## Note
This project is currently still under development.  More changes and completed documentation are on the way!

## Description
The Salem Candy Dispenser works by connecting an arduino to a trigger and a motor, and then loading the ino file onto the arduino.  When the arduino is triggered, it sends a serial message onto the machine that it is connected to via USB, which then (running the included py file `salemCandyDispenser`) plays a sound from its local selection of Halloween sounds.  The python script logs to a local SQLite database, and an hourly count of triggers can be viewed on a locally hosted web page.

## How to Set Up
Two main pieces need to be configured in order to run the Salem Candy Dispenser: the arduino and the main machine (in my case, I chose to use a Raspberry Pi Zero W).  The code for both pieces is included within this repository, within the salemPi and the salemTrigger folders.

### Configuring the Arduino
The arduino is coded such that it only actively uses two pins: pin 2 for receiving input from the trigger and pin 13 for outputting a current for running the dispenser.  For testing, I ran power from the 5v pin to a button, which then was wired to pin 2.  Whenever the button is pressed, the arduino will receive its trigger.  Pin 13 was then wired to a relay, which could then make the connection to run a motor or solenoid to push candy out of the dispenser.  The relay is also connected to the ground pin on the arduino in order to complete the circuit.

### Configuring the Raspberry Pi/Computing Device
In order to run the Salem Candy Dispenser on the computing device, this device needs to have the following software installed:
- Python 3.7
- Pip3
- NodeJS
- SQLite
- npm

Once python is installed, run `pip install sqlite3` and `pip install pydub`.  In the salemStats folder, run `npm install` to install sqlite3.  The two applications can now be run by calling `python salemCandyDispenser.py` and `node app.js`.  In order to work, the computing device must be connected to the arduino via USB.