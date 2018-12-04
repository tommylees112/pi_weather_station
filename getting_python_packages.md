NOTE: there are lots of different approaches here to downloading the same thing.
Use your common sense as there is no need to download the same package again
and again!

## UPDATE apt-get
sudo apt-get update

## Install pip3 (pip for python3)
sudo apt-get install python3-pip

# install the necessary packages
pip3 install gpiozero;
pip3 install w1thermsensor;
pip3 install pigpio;
pip3 install RPIO;
pip3 install RPi.GPIO;

## TO GET w1thermsensor working
### tis stops the `KERNEL ERROR` message

ERROR MESSAGE:
```python
Traceback (most recent call last):
  File "pi_weather_station/weatherstation.py", line 4, in <module>
    from w1thermsensor import W1ThermSensor #An interface library produced by the makers of the temperature sensor
  File "/home/pi/.local/lib/python3.5/site-packages/w1thermsensor/__init__.py", line 8, in <module>
    from .core import W1ThermSensor  # noqa
  File "/home/pi/.local/lib/python3.5/site-packages/w1thermsensor/core.py", line 352, in <module>
    load_kernel_modules()
  File "/home/pi/.local/lib/python3.5/site-packages/w1thermsensor/core.py", line 346, in load_kernel_modules
    raise KernelModuleLoadError()
w1thermsensor.errors.KernelModuleLoadError: Cannot load w1 therm kernel modules
```
https://github.com/timofurrer/w1thermsensor/issues/42

SOLUTION:
`sudo nano /boot/config.txt`

Then at the end add the following
`dtoverlay=w1-gpio`
Save the file

Finally, reboot
`sudo reboot`

## TEST IT HAS WORKED:
python3 -c "import w1thermsensor; import gpiozero"
python3 pi_weather_station/weatherstation.py

#####################
ALTERNATIVES
----------------------

## DEPENDENCIES FOR GPIOZERO
sudo apt-get install python-setuptools
sudo easy_install -U RPIO

## I downloaded it and then scp'd the zip file into
## pigpio - download directly
wget abyz.co.uk/rpi/pigpio/pigpio.zip;
unzip pigpio.zip;
cd PIGPIO;
make;
sudo make install;

## RPIO - download directly
git clone https://github.com/metachris/RPIO.git
cd RPIO
sudo python setup.py install

# OR USE apt-get
sudo apt-get install python3-w1thermsensor
sudo apt install python3-gpiozero
