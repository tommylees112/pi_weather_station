# Raspberry Pi Weather stations

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

- [ ] 1 raspberry pi
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

- *The thermometer:* strip about 1cm of insulation from each of the three
wires and braid the copper together. The red wire will be connected to
power, the black wire to ground, and the yellow wire will output the
temperature data.
- *The wind sensor:* Plug the ethernet connector on the wind speed sensor
into the port on the underside of the weather vane. The cable coming out
of the weather vane has 4 wires, we shall only be using the red and yellow
ones. Strip 1cm of insulation from each, and braid.
- *The rain sensor:* strip and braid both cables. Red is data, green is ground.

