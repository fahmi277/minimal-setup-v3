import RPi.GPIO as GPIO
from shiftregister_sia.shift import ShiftRegister
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

data_pin = 4 #pin 14 on the 75HC595
latch_pin = 27 #pin 12 on the 75HC595
clock_pin = 17 #pin 11 on the 75HC595

shift_register = ShiftRegister()

#addressing 4 5 6 7 : tombol 1-4
#addressing 0 1 2 3 : addresing 1-4

#addressing 12 13 14 15 : tombol 5-8
#addressing 8 9 10 11 : addresing 5-8

def wake(dock):
    numberdock = dock-1
    numberShift = int(numberdock/4)
    pinShift = dock + (4*numberShift)


    shift = int(pinShift)+4

    shift_register.setOutput(shift-1, GPIO.HIGH)
    shift_register.latch()
    time.sleep(1)

    shift_register.setOutput(shift-1, GPIO.LOW)
    shift_register.latch()
    time.sleep(1)

    print(numberdock)
    print(numberShift)
    print(shift)

counter = 12
while True:

    wake(counter)
    counter+=1
    time.sleep(0.5)
    if counter == 17:
       counter=12
    print(f'{counter}\n')

