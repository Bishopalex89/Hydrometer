# Hydrometer
A Hydrometer with Arduino Uno and python program to track specific gravity. This project is intended to be used in conjunction with beer brewing and assumes the user has some knowledge of taking specific gravity measurements and their importance in monitoring the fermentation process and determining the alcohol content of the beer. 

The Sensor uses the Adafruit VL53L0X Time of Flight - mini Lidar Sensor (ToF Sensor) to send distance measurements bounced off of a tradional hyrometer to a python script. The script will then convert the Distance measurements into a Specfic Gravity.

# Sensor set up:
The sensor can be installed on any kind of cap for a fermentation vessel. In my case, I used a PVC screw plug. I drilled a hole in the top of the cap for wires to be fed through to the sensor. The sensor was then mounted on standoffs and glued to the bottom inside of cap. It is important to make sure that the hole dilled for the wires is completely filled with glue to prevent contmanination. wires can then be connected to the arduino.

The ToF sensor was setup accourding to the Adafruit website Tutorials found at:
https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/arduino-code

The code used for the Arduino was almost identical. I commented out some of the startup print lines. I replaced the "out of range" print line at the end of the code to print the int(0). This made sure that only integers were collected on python scrpit side

# Physical Set up:
A traditional hydromoeter uses the principle of bouancy to determine a specific gravity. The "primitive" divice can be found at local homebrew shops and are typically a sealed glass tube with a weighted end that has gradations on the unwe=ighted side. Becuase they are typically glass, a "hat" for the hydrometer needs to be made to fit over the top end that will reflect the light from the ToF Sensor. I cut mine out of styrofoam to minimize the contribution of weight to the hydrometer. To make sure that the hydrometer travels (as the S.G goes down from alcohol production, the hydrometer will sink and move further away from the sensor) in a path that the ToF sensor can still take accurate measrements, I mounted a 12" transpernt plastice tube on the inside bottom of the cap. The "Hat" should be a smaller diameter than the tube to allow it to travel unresetricted. 

# Python Script

The python script was adapted from toptechboy.com website, mainly for the tutotial on using the drawnow library to print data in real time. The basic overview of the code is to import libraties, open serial port, collect data in a try loop sequence to prevent errors from sigfigs, convert data into an S.G., and finally graph the reults. Due to the nature of the setup and differences in fermentation vessels, Calibrations for each device would need to be done based on the individuals setup. 

# Calibration
If using for beer fermentation, the level shold be specified in the fermentation tank and filled with tap water to get first reading (about 1.000). Before beer is put into fermentation vessel and filled to the previously specified level, a specfic gravity should be read. Using a linear equation, a calibration curve can then be input into the python script to convert the distance measurement to a S.G.

# Analysis
Evenw/out calibration, or changing the specific gravity, the distance measuremnt can provide the nessesary information to the brewer needed to determine when fermentation of the beer is complete. The curve should look similar to a log curve (depending on feremtnation conditions) however, the brewer will know that fermentation is complete when the curve levels out with minimal change. 
