
import RPi.GPIO as GPIO
# from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep
import time
import binascii
import os
import can


def readDock(dockdata):
    dockdata = dockdata-1
    try:
            data = []
            msg = can0.recv(0.1)
            uid = msg.arbitration_id

            if uid == 124045410:
                print("dock 2")

            # if uid != 490784999:
                # listUid = [124045411-dockdata,123979875-dockdata,123914339-dockdata,123848803-dockdata,123783267-dockdata,123717731-dockdata,123652195-dockdata,123586659-dockdata,123521123-dockdata,123455587-dockdata,123390051-dockdata]
                # if uid not in listUid and uid != 0:

                    # listUid2 = [308608611,308543075,308477539,308543846,308477539,308543075] # from poweroad software

                    # if uid not in listUid2:

                        # hex_msg = binascii.hexlify(msg.data)
                        # # print ("======\nUID : "+str(uid)+" data : " + str(hex_msg))
            # # if uid == 123979875:
            # #     hex_msg = binascii.hexlify(msg.data)
            # #     str_msg = str(hex_msg)
            # #     print("mos: "+str_msg)

    except:
            os.system('sudo ifconfig can0 down')
            time.sleep(0.5)
            os.system('sudo ip link set can0 type can bitrate 250000')
            os.system('sudo ifconfig can0 up')
            return "0","0"

os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

print("ok")
while True:
    readDock(2)