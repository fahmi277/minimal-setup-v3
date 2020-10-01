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


def enableVsat():
	gpio.output(vsatOn, gpio.HIGH)

def disableVsat():
	gpio.output(vsatOff, gpio.HIGH)

def enableBts():
	gpio.output(btsOn, gpio.HIGH)

def disableBts():
	gpio.output(btsOff, gpio.HIGH)


def allOff():
	gpio.output(btsOff, gpio.LOW)
	gpio.output(btsOn, gpio.LOW)
	gpio.output(vsatOn, gpio.LOW)
	gpio.output(vsatOff, gpio.LOW)
# gpio.output(19, gpio.HIGH)
# gpio.output(12, gpio.HIGH)

# while True:
passcode = input("Select Load : vsat on / vsat off / bts on / bts off / off both : ")

print(passcode)

if passcode == "vsat on" :
	enableVsat()

elif passcode == "vsat off" :
	disableVsat()

elif passcode == "bts on":
	enableBts()

elif passcode == "bts off":
	disableBts()




#     print("relay 1 on")
#     # print("relay 2 off")
#     gpio.output(relay3, gpio.HIGH)
#     gpio.output(relay4, gpio.LOW)
#     time.sleep(2)
#     print("relay 1 off")
#     print("relay 2 on")
#     gpio.output(relay3, gpio.LOW)
#     gpio.output(relay4, gpio.HIGH)
#     time.sleep(2)

# while True:

#     print("relay 1 on")
#     # print("relay 2 off")
#     gpio.output(relay1, gpio.HIGH)
#     gpio.output(relay2, gpio.LOW)
#     time.sleep(2)
#     print("relay 1 off")
#     print("relay 2 on")
#     gpio.output(relay1, gpio.LOW)
#     gpio.output(relay2, gpio.HIGH)
#     time.sleep(2)


