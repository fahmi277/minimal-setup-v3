import RPi.GPIO as GPIO
# from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep
import time
import binascii
import os
import can

# ea for discharge mosfet
# eb for charge mosfer

def mosfetControl (dockInput,mosBlock,mosStatus):

    dock = (int(dockInput)-1)*256

    dataMosblock = 0xea
    dataMosStatus = 0xba

    if mosBlock == 'input':
        dataMosblock = 0xeb
    elif mosBlock == 'output':
        dataMosblock = 0xea

    if mosStatus == 'on':
        dataMosStatus = 0x0f
    elif mosStatus == 'off':
        dataMosStatus = 0xba

    print(dock)
    print (dataMosblock)
    print(dataMosStatus)

    

    try:
        # can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native
        id1 = 429982054 + dock
        id2 = 430046819 + dock
        id3 = 312738150 + dock
        id4 = 312802915 + dock

        print (id1)
        print (id2)
        print (id3)
        print (id4)

        msg1 = can.Message(arbitration_id=id1, data=[dataMosblock ,0x64 ,0x63 ,0x64 ,0x64 ,0x64 ,0x63 ,0x64], extended_id=True)
        msg2 = can.Message(arbitration_id=id2, data=[dataMosblock ,0x64 ,0x64], extended_id=True)
        msg3 = can.Message(arbitration_id=id3, data=[dataMosblock,0x64,dataMosStatus,0x64,0x64,0x64], extended_id=True)
        msg4 = can.Message(arbitration_id=id4, data=[dataMosblock,0x64,0x64], extended_id=True)
        # msg5 = can.Message(arbitration_id=id5, data=[0xba, 100-dock, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64], extended_id=True)

        can0.send(msg1)
        can0.send(msg2)
        can0.send(msg3)
        can0.send(msg4)
        # can0.send(msg5)
        # os.system('sudo ifconfig can0 down')
        print("terkirim")
    except:
        print("eror")
        os.system('sudo ifconfig can0 down')
        time.sleep(0.5)
        os.system('sudo ip link set can0 type can bitrate 250000')
        os.system('sudo ifconfig can0 up')
        return "0","0","0","0"

os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native


# msg1 = can.Message(arbitration_id=1, data=[1,2,3,4,5,6,7,8], extended_id=True)
# can0.send(msg1)

# mosfetControl('1','output','on')

passcode = input("Nomor dock [spasi] input/output on/off === > ")
# while True:
inputStr = passcode.split()
mosfetControl(inputStr[0],inputStr[1],inputStr[2])
# if inputStr[]



# print(passcode[0:1])
# print(passcode[1:2])
# print(passcode[2:3])


