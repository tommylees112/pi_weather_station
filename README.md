# Raspberry Pi Weather Stations

![image](https://user-images.githubusercontent.com/25530332/192252861-2d898804-bf3b-4320-9dc0-1399f69e9c74.png)

The aim of this project is to build an automated weather station that you can
deploy in Wytham Woods, and that will automatically record
temperature, wind speed and rainfall, ready for analysis.
The measurement devices are connected to a Raspberry Pi mini-computer, such that
the weather station is (with a power bank) fully autonomous and can be left outside
for as long as the power bank lasts.

The project has two parts
- assembling and wiring up the three sensors
- customising the Python script on the Raspberry Pi that will monitor the sensors

These parts can be done largely in parallel, so it might be sensible to split up into two smaller groups.

### The kit needed for the Pi weather stations

- [ ] 1 raspberry pi (check name on the back)
- [ ] 1 power bank
- [ ] 1 USB to micro USB adapter (for power)
- [ ] 1 temperature sensor
- [ ] 1 rain gauge
- [ ] 1 weather vane
- [ ] 1 anemometer
- [ ] Poles for mounting the wind sensors
- [ ] 1 wiring connector box
- [ ] 1 4.7K Ohm resistor
- [ ] 7 GPIO connectors
- [ ] 1 weatherproof box (to weatherproof the pi)
- [ ] 1 tupperware box (for the power banks that are too large for the weatherproof box) 

## Part 1: Hardware

Your final weather station will have three operational sensors, a thermometer, an
anemometer (wind speed sensor) and a rain gauge. Some anemometers require the weather
vane to be connected to the Raspberry Pi, others work independent of the weather vane.

### Step 1: Prepare the sensor cables

**The thermometer:** strip about 1cm of insulation from each of the three
wires and braid the copper together. The red wire will be connected to
power, the black wire to ground, and the yellow wire will output the
temperature data.

**The wind sensor:** The anemometers that are connected to weather vane use the
red and yellow cable, the independent ones use red and green.

a) In the first case (via weather vane),
plug the ethernet connector on the wind speed sensor into the port on the underside
of the weather vane. The cable coming out of the weather vane has 4 wires, we shall
only be using the red and yellow ones. Strip 1cm of insulation from each, and braid.

b) In the second case (no weather vane), use the red and green cable instead.
Red is data, green is ground.

**The rain sensor:** strip and braid both cables. Red is data, green is ground.

### Step 2: Loop cables through the weatherproof box

Pop out one of the rubber seals on the weatherproof box and install the gland in its place.
Pull all the cables from the sensors through the gland now, as you won’t be able to do
this once they are wired into the connector box.

### Step 3: Wire into connector box.

The connector box allows you to connect the messy wiring of the sensors
to neat GPIO connectors for use with the pi. Arrange the cables as shown:

![image](https://user-images.githubusercontent.com/25530332/192256927-4ba2b490-95fb-4416-ae4d-a3e767c02546.png)

For each cable, insert the exposed copper wiring into the connector box
and tighten the screw so the cable is secure. This will be easier if the wire
is well braided. If the connection is poor, or two neighbouring wires are in
electrical contact your weather station will not work, so take the time to
get this right!

Next we want to connect the GPIO pins to the box. Each pin will be in
electrical contact with the wire directly across from it on the box. For the
thermometer, the power and data cables must be bridged by the resistor.
This serves to transfer a small amount of power to the yellow data wire. To
do this, bend the resistor so it looks a bit like a staple and trim the ends to
~1cm in length. It should then be possible to insert the resistor along with
GPIO pins as shown:

![image](https://user-images.githubusercontent.com/25530332/192257320-45daf17d-3004-4b39-8a94-fbd03cc54821.png)

Attach the GPIO connectors to the correct type of pins on the raspberry pi
as follows. The orientation is such that most of the pi is below this diagram,
which is also so that the letters GPIO on the board are the correct way around.

![image](https://user-images.githubusercontent.com/25530332/192257095-890af097-697b-4c2b-a0be-4c2a2dd1edf4.png)

| Wire from sensor | Pin on Raspberry Pi GPIO |
| - | - |
| Anemometer (with vane) - **red** | A ground pin |
| Anemometer (with vane) - **yellow** | Data pin 17 |
| Anemometer (no vane) - **red** | Data pin 17 |
| Anemometer (no vane) - **green** | A ground pin |
| Rain gauge - **red** | Data pin 27 |
| Rain gauge - **green** | A ground pin |
| Thermometer - **black** | A ground pin |
| Thermometer - **red** | A 3V power pin |
| Thermometer - **yellow** | Data pin 4 |

We had some issues in the past with the wiring of the anemometers, in case yours is not working, please play around
by swapping the connections.

## Part 2: Software

To interface with the pi you will log into it remotely via ssh (secure shell). If you
are using a mac or linux computer all you will need is an open terminal. If you
are using Windows you will instead need to install the ssh client PuTTy. Your Pi
will have a unique name stuck on it which will identify it.

### Step 1: Logging in

- Power on the Pi by connecting to the power bank and wait for the light to stop flickering.
- Connect with your laptop to the local wifi network “pi_wifi” with the password “raspberry”.

The pi will have automatically connected to the local network, so once you
are also on that network you can access the pi using the command:

```
ssh username@address
```

You find the username and address in the following table

| Pi name | user name | address | password |
| - | - | - | - |
| summer | pi | summer.local | raspberry |
| spring | pi | spring.local | raspberry |
| autumn | pi | autumn.local | raspberry |
| mulberry | pi | mulberry.local | raspberry |
| gooseberry | pi | gooseberry.local | raspberry |

If everything went well you will get a prompt that look similar to

```
pi@summer:~ $
```

which lets you type commands, then hit enter.
Example: type `ls`, short for *list*, that shows you files and folders in the current directory.
All pis already have a folder called `pi_weather_station`.

### Step 2: Changing the python script

- To change directories in linux we use the command ‘cd’. Move to the
directory where the script is located by typing `cd pi_weather_station`
- To open the file so we can read and edit it, we will use a tool called `nano`.
Type `nano weatherstation.py` to open the file in your terminal.
- Since the nano interface can be a little awkward, if you just want to read
the code and get a sense for how it works, try looking at it on your laptop
on github at

https://github.com/milankl/pi_weather_station/blob/master/weatherstation.py

- You can edit text intuitively, for saving use `cntrl+o` then enter, for exiting `cntrl+x`.
- You will not need to fiddle too much with the code (unless you want to!),
but you will want to think about the values of some of the constants.
`CSVOUTPUT` controls whether the pi prints results to terminal or saves
them in a `.csv` file, and `OUTPUT_DT` sets the time between measurements (in seconds).
You also want to set ‘codename’ to the name of your pi.
- If you have connected any of the data cables to different pins than the
default suggestion, then you will have to change the value of the `DATA_PIN`
constants accordingly

For testing purposes you can always do

```
python weatherstation.py
```
if the `CSV_OUTPUT` is set to 0, it will print measurements to the terminal.

### Step 3: Initialisation script

Once you are happy with the configuration of the python script you must tell the
pi when the script should be run. To do this, you need to open the `.bashrc` file
which contains all commands that the pi executes at boot up.

- Type `nano .bashrc` to open the file
- At the bottom of the file you will need to uncomment this line

```
nohup python pi_weather_station/weatherstation.py &
```
- `nohup` (no hang up) launches what cames afterwards as a process independent
of the current terminal session.
- The `&` isn't strictly needed but will give you back a prompt in case you want to log in while the
measurements are running in the background.
- Any text preceded by a `#` in the bash shell will not be executed, so add some information
what the above line is doing.

## Part 3: Assembly

You should now have a fully programmed pi, and a fully wired sensor network. All
that remains now is to make sure that your weatherstation can withstand the
weather!

The power pack will need to be connected to the raspberry pi via the USB to
micro USB connector for it to function. Due to an entirely intentional design
choice, some power banks we have will not fit into the weatherproof boxes, and so
they will need to be deployed in a separate Tupperware box. Once the power cable
is in place, put a ring of blutac around it to create a watertight seal.

Now go out into the world and place your station.
Make sure that you power on your power bank before leaving!

# Credits

Originally written by Josh Dorrington, Tommy Lees and Milan Klöwer in 2018.
Changes made in 2022 and 2024 by Milan Klöwer.

