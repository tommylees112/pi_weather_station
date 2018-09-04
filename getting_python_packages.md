## UPDATE apt-get

sudo apt-get update

## Install pip3 (pip for python3)
sudo apt-get install python3-pip

# install the necessary packages
pip3 install gpiozero
pip3 install w1thermsensor
pip3 install pigpio

# OR download directly
wget abyz.co.uk/rpi/pigpio/pigpio.zip;
unzip pigpio.zip;
cd PIGPIO;
make;
sudo make install


# OR USE apt-get
sudo apt-get install python3-w1thermsensor
sudo apt install python3-gpiozero

## TO GET w1thermsensor working
https://github.com/timofurrer/w1thermsensor/issues/42

`sudo nano /boot/config.txt`

Then at the end add the following
`dtoverlay=w1-gpio`
Save the file

Finally, reboot
`sudo reboot`

## TEST IT HAS WORKED:
python3 -c "import w1thermsensor; import gpiozero"


