import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

btsOn=13
btsOff = 12

vsatOn = 16
vsatOff = 19

gpio.setup(btsOff, gpio.OUT)
gpio.setup(btsOn, gpio.OUT)
gpio.setup(vsatOn, gpio.OUT)
gpio.setup(vsatOff, gpio.OUT)

gpio.output(btsOff, gpio.LOW)
gpio.output(btsOn, gpio.LOW)
gpio.output(vsatOn, gpio.LOW)
gpio.output(vsatOff, gpio.LOW)


def allLow():
    gpio.output(btsOff, gpio.LOW)
    gpio.output(btsOn, gpio.LOW)
    gpio.output(vsatOn, gpio.LOW)
    gpio.output(vsatOff, gpio.LOW)


def enableVsat():
	gpio.output(vsatOn, gpio.HIGH)
    # allLow()
    

def disableVsat():
	gpio.output(vsatOff, gpio.HIGH)
    # allLow()/

def enableBts():
	gpio.output(btsOn, gpio.HIGH)

def disableBts():
	gpio.output(btsOff, gpio.HIGH)


while True:
    enableVsat()
    time.sleep(2)
    allLow()
    disableVsat()
    time.sleep(2)
    allLow()

    enableBts()
    time.sleep(2)
    allLow()
    disableBts()
    time.sleep(2)
    allLow()

    enableBts()
    enableVsat()
    time.sleep(2)
    allLow()
    disableBts()
    disableVsat()
    time.sleep(4)
    allLow()