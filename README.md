# Hydrometer
A Hydrometer with Arduino Uno and python program to track specific gravity 

The Sensor uses the Adafruit VL53L0X Time of Flight - mini Lidar Sensor to send distance measurements bounced off of a tradional hyrometer to a python script. The script will then convert the Distance measurements into a Specfic Gravity

#Calibration
If using for beer fermentation, the level shold be specified in the fermentation tank and filled with tap water to get first reading (about 1.000). Before beer is put into fermentation vessel and filled to the previously specified level, a specfic gravity should be read. Using a linear equation, a calibration curve can then be input into the python script to convert the distance measurement to a S.G.
