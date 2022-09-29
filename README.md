# P1-IntroRPi-PWM

This exersice consists on drive a LED with the GPIO available on the Raspberry Pi 3B+.

It is important to take care of some precautions with this firsts steps, as they involve physicall access to the board.

- 1.- There are two ways of refering to the pins of the board.
	- a) BOARD mode. This is the physicall order of the pins.
	- b) BCM mode. This are the GPIO numbers
- 2.- There is some resources to read, like this [interactive page.](https://pinout.xyz/) However, if you do not have access to internet the command `pinout` helps with printing on the screen a representation of the pins either with its GPIO number or board number.

![PINOUT](https://raspberry-valley.azurewebsites.net/img/Pin-Layout-on-Raspberry-Pi-01.png)
