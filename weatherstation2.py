##IMPORTED MODULES##
import threading #Enables parrallel execution of code so all three sensors can be monitored and logged simultaneously 
from time import sleep #Used to suppress temperature sensor input 
from gpiozero import DigitalInputDevice #A low level library that interfaces directly with the hardware
from w1thermsensor import W1ThermSensor #An interface library produced by the makers of the temperature sensor
import math

##FUNCTIONS##

#These functions record and log the input from the sensors.
#They are executed whenever a new input is received from the corresponding sensor.
def wind(time_sec):
	global wind_count
	circumference_cm = (2 * math.pi) * radius_cm
	rotations = wind_count / 2.0 #wind count tracks half rotations of the anemometer. Incremented by spin()
	wind_count = 0

	dist_km = (circumference_cm * rotations) / CM_IN_A_KM

	km_per_sec = dist_km / time_sec
	km_per_hour = km_per_sec * SECS_IN_AN_HOUR

	return km_per_hour * ADJUSTMENT

def spin():
	global wind_count
	wind_count = wind_count + 1

def rain():
	global bucket_count
	bucket_count = bucket_count + 1
	print("rainfall is currently" + str(round(bucket_count * BUCKET_SIZE,2))+"mm\n")

def temperature():
	while True:
		temp = sensor.get_temperature()
		print("The Temperature is %s celsius \n" % temp)
		sleep(TEMP_SLEEP_TIME) #this sleep function prevents the thermometer from logging continously

##CONSTANTS##
wind_count = 0
bucket_count = 0
radius_cm = 9.0
WIND_SLEEP_TIME= 0.5
TEMP_SLEEP_TIME=5
ADJUSTMENT = 1.18 #This calibration constant accounts for the mass of the anemometer.
CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600
BUCKET_SIZE = 0.2794


##EXECUTABLE CODE##

#Initialises the three sensors.
#first input to DigitalinputDevice denotes the GPIO pin the sensor is connected to.
sensor = W1ThermSensor()
wind_speed_sensor = DigitalinputDevice(17, pull_up=True)
rain_sensor = DigitalinputDevice(27, pull_up=True)

#Initialises three threads which track the three sensors. 
#Each is linked to one of the functions defined above which will print information to terminal
windspeed = threading.Thread(name='wind', target=wind(WIND_SLEEP_TIME))
raindata = threading.Thread(name='rain', target=rain)
tempdata = threading.Thread(name='temperature', target=temperature)

windspeed.start()
raindata.start()
tempdata.start()

#The hardware will set the 'when_activated' property of the wind and rain sensors to True
#when an input is received. This will trigger the corresponding spin and rain functions which
#increment wind_count and bucket_count
wind_speed_sensor.when_activated = spin
rain_sensor.when_activated = rain

#perpetually prints the wind speed sleeping for every WIND_SLEEP_TIME seconds
while True:
	sleep(WIND_SLEEP_TIME)
	print("The wind speed is " + str(round(wind(WIND_SLEEP_TIME),2) + "kph \n"))
