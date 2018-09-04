Reference: https://www.raspberrypi.org/learning/networking-lessons/rpi-static-ip-address/

## 1. open the dhcpcd.conf file to edit

```bash
sudo nano /etc/dhcpcd.conf
```

## 2. Copy the following code at the bottom of the script
   Replace {NUM} with a number from 2-255 (ENSURING IT IS UNIQUE FOR EACH PI)

```bash
interface eth0

static ip_address=192.168.0.{NUM}/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1

interface wlan0

static ip_address=192.168.0.{NUM}/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
```

## 3. restart the pi
```bash
sudo reboot
```

OR

```bash
sudo shutdown -r now
```

## 4. Check the ip addres

```bash
sudo ifconfig
```

OR

```bash
ip a
```
