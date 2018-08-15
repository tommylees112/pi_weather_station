##IMPORTED MODULES##
import threading #Enables parrallel execution of code so all three sensors can be monitored and logged simultaneously
import time  #Used to suppress temperature sensor input
from gpiozero import DigitalInputDevice #A low level library that interfaces directly with the hardware
from w1thermsensor import W1ThermSensor #An interface library produced by the makers of the temperature sensor
import math
import os
import glob

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
	wind_count += 1

def bucket_tip():
  global bucket_count
  bucket_count += 1

def rainfall():
  global bucket_count
  rain_value = BUCKET_SIZE*bucket_count # ignore initial bucket count occuring when switch on
  bucket_count = 0
  return rain_value

def temperature():
	while True:
		temp = temp_sensor.get_temperature()
		print("The Temperature is %s celsius \n" % temp)
		time.sleep(TEMP_SLEEP_TIME) #this sleep function prevents the thermometer from logging continously

def timestring():
  return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())



##CONSTANTS##
wind_count = 0
bucket_count = 0
radius_cm = 9.0
WIND_SLEEP_TIME = 0.5
TEMP_SLEEP_TIME = 5
ADJUSTMENT = 1.18 #This calibration constant accounts for the mass of the anemometer.
CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600
BUCKET_SIZE = 0.2794
CSVOUTPUT = 0
OUTPUT_DT = 5  # in seconds

if CSVOUTPUT:

  # create data folder if not already existing
  try:
    os.mkdir("data")
  except:
    pass

  # get measurement id
  all_ids = glob.glob("data/pws_????.csv")

  if not all_ids: # empty list
    measurement_id = 0
  else:
    measurement_id = max([int(id[-8:-4]) for id in all_ids])+1

  csvfile = open("data/pws_{:04d}.csv".format(measurement_id),"w")

  # Write header

  csvfile.write("Pi Weather station data, initialised "+time.asctime()+"\n")
  csvfile.write("Format YYYY-MM-DDTHH:MM:SS, Temperature [degC], Wind speed [km/h], Rainfall [mm]\n")
  csvfile.write("Temperature is instantaneous, wind speed is averaged since previous measurement,\n"
  csvfile.write("rainfall is accumulated since previous measurement.\n")
  csvfile.write("\n")
  csvfile.flush()

##EXECUTABLE CODE##

#Initialises the three sensors.
#first input to DigitalinputDevice denotes the GPIO pin the sensor is connected to.
temp_sensor = W1ThermSensor()
wind_speed_sensor = DigitalInputDevice(17, pull_up=True)
rain_sensor = DigitalInputDevice(27, pull_up=True)

#Initialises three threads which track the three sensors.
#Each is linked to one of the functions defined above which will print information to terminal
windspeed = threading.Thread(name='wind', target=wind(WIND_SLEEP_TIME))
raindata = threading.Thread(name='rain', target=rainfall)

# start the threads
raindata.start()
windspeed.start()

#The hardware will set the 'when_activated' property of the wind and rain sensors to True
#when an input is received. This will trigger the corresponding spin and bucket_tip functions which
#increment wind_count and bucket_count
wind_speed_sensor.when_activated = spin
rain_sensor.when_activated = bucket_tip

# initial time to calculate interval between measurements
time_of_prev_measurement = time.time()

for i in range(10):

  # measure time in seconds each instant of output
  # differene to last measurement is used to determine the wind speed in that period
  # wind speed is going to be an average of the period ending at time stamp
  time_of_this_measurement = time.time()
  windspeed_value = round(wind(time_of_this_measurement-time_of_prev_measurement),2)

  # get instantaneous temperature measurement
  temp_value = temp_sensor.get_temperature()

  # get accumulated rainfall in mm, functions updates the global rain_value
  rain_value = rainfall()

  outputstring = timestring()+", "+str(temp_value)+", "+str(windspeed_value)+", "+str(rain_value)+"\n"

  if CSVOUTPUT:
    csvfile.write(outputstring)
    csvfile.flush()
  else:
    print(outputstring)

  # this becomes previous
  time_of_prev_measurement = time_of_this_measurement
  print("Measurement {:02d} taken.\n".format(i))
  time.sleep(OUTPUT_DT)

csvfile.close()
