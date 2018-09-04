reference: https://desertbot.io/blog/ssh-into-pi-zero-over-usb

## Edit config.txt

`sudo nano /boot/config.txt`

Append this line to the bottom of it:
`dtoverlay=dwc2`

## Edit cmdline.txt

`sudo nano /boot/cmdline.txt`

After rootwait, append this text leaving only one space between rootwait and the new text (otherwise it might not be parsed correctly):

`modules-load=dwc2,g_ether`

If there was any text after the new text make sure that there is only one space between that text and the new text


## PLUG IN TO USB (and wait 15s for it to boot)

## ssh into local
Replacing {NAME} with the name of your pi:
  - raspberry
  - blueberry
  - mulberry
  - elderberry
  ...

`ssh pi@{NAME}pi.local`

Type your password
