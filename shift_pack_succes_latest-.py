import RPi.GPIO as GPIO
from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep
import time
import binascii
import os
import can


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

data_pin = 21 #pin 14 on the 75HC595
latch_pin = 16 #pin 12 on the 75HC595
clock_pin = 20 #pin 11 on the 75HC595

shift_register = ShiftRegister(data_pin, latch_pin, clock_pin)


def change_dock (uid):
    try:
        can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native
        dock = uid
        base_dock = 0x0c24c865
        id1 = 0x1002ff9c
        id2 = 0x1c60fbf9
        id3 = 0x0c24ff9c
        id4 = dock-base_dock
        id5 = 0x0c24ff9c

        msg1 = can.Message(arbitration_id=id1, data=[0x6d, 0x5d, 0x5f, 0x4e, 0x4e, 0x4F, 0x3e, 0x64], extended_id=True)
        msg2 = can.Message(arbitration_id=id2, data=[0x08, 0x19, 0x1f, 0x02, 0x08, 0x00, 0x00, 0x00], extended_id=True)
        msg3 = can.Message(arbitration_id=id3, data=[0xba, 100-dock, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64], extended_id=True)
        msg4 = can.Message(arbitration_id=id4, data=[0xa9, 100-dock, 0x65, 0x65, 0x65, 0x65, 0x65, 0x65], extended_id=True)
        msg5 = can.Message(arbitration_id=id5, data=[0xba, 100-dock, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64], extended_id=True)

        can0.send(msg1)
        can0.send(msg2)
        can0.send(msg3)
        can0.send(msg4)
        can0.send(msg5)
        os.system('sudo ifconfig can0 down')
        print("dock" + str(id4))
    except:
        # os.system('sudo ifconfig can0 down')
        # time.sleep(0.5)
        os.system('sudo ip link set can0 type can bitrate 250000')
        os.system('sudo ifconfig can0 up')
        return "0","0","0","0"


def readCanbus():
    try:
        data = []
        msg = can0.recv(0.1)
        uid = msg.arbitration_id
        if uid == 124045395:
            print("17")

    

    except:
        os.system('sudo ifconfig can0 down')
        time.sleep(0.5)
        os.system('sudo ip link set can0 type can bitrate 250000')
        os.system('sudo ifconfig can0 up')
        return "0","0"

def read():
    try:
        data = []
        msg = can0.recv(0.1)
        uid = msg.arbitration_id
        if uid == 124045395:
            print("ada dock 17")


            # shifting_dock(2)
            # print("3")
            shifting_dock(1)



        # if uid != 490784999:

        #     print("em")
        # os.system('sudo ifconfig can0 down')
        
        

    except:
        os.system('sudo ifconfig can0 down')
        time.sleep(0.5)
        os.system('sudo ip link set can0 type can bitrate 250000')
        os.system('sudo ifconfig can0 up')
        return "0","0"

def shifting_dock (dox):
    

    shift_register.setOutput(dox, GPIO.LOW) # low untuk press
    shift_register.latch()
    change_dock(dox)
    sleep(1)

    shift_register.setOutput(dox, GPIO.HIGH) # low untuk press

    shift_register.latch()
    change_dock(dox)
    sleep(1)



os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native
while True:
    # print("=== change dock ===")
    # readCanbus()
    read()

#addressing 4567 : tombol 1-4
#addressing 0123 : addresing 1-4



# for x in range(0,1):



#     shift_register.setOutput(2, GPIO.LOW) # low untuk press
#     shift_register.latch()
#     change_dock(dox)
#     sleep(1)

#     shift_register.setOutput(2, GPIO.HIGH) # low untuk press

#     shift_register.latch()
#     change_dock(dox)
#     sleep(0.7)

# while(1):
    # try:

    #     read()
    #     print("read")
    #     # os.system('sudo ifconfig can0 down')
    #     # time.sleep(0.1)
    # except:
    #     print("err")

print("Alhamdulillah")

# shift_register.setOutput(6, GPIO.HIGH) # low untuk press

# shift_register.latch()
# sleep(1)


# try:
#     while 1:
#         # Set all outputs
#         shift_register.setOutputs([GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH])
#         shift_register.latch()
#         sleep(1)

#         print ("N Press")

#         shift_register.setOutputs([GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW])
#         shift_register.latch()

#         sleep(1)
#         print ("Press")
#         # GPIO.cleanup()
# except KeyboardInterrupt:
#     print ("Ctrl-C - quit")

GPIO.cleanup()