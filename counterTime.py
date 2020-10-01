import os
import can
import time
from time import gmtime, strftime
import datetime


def read (uid):
    try:
        # can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native
        dock = uid
        base_dock = 0x0c24c864
        id1 = 0x1002ff9c
        id2 = 0x1c60fbf9
        id3 = 0x0c24ff9c
        id4 = base_dock-dock
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
    except:
        os.system('sudo ifconfig can0 down')
        time.sleep(0.5)
        os.system('sudo ip link set can0 type can bitrate 250000')
        os.system('sudo ifconfig can0 up')
        return "0","0","0","0"

def pushDate ():
    try:

        id1 = 203751324
        date1 = [186, 99, 100, 100, 100, 100, 100, 100]
        for y in range (0,3):

            for x in range(0,4):
                date1 = [186, 99-y, 100, 100, 100, 100, 100, 100]
                msg1 = can.Message(arbitration_id=id1, data=date1, extended_id=True)
                can0.send(msg1)
                time.sleep(0.1)

        for z in range(0,3):
                date1 = [186, 96, 100, 100, 100, 100, 100, 100]
                msg1 = can.Message(arbitration_id=id1, data=date1, extended_id=True)
                can0.send(msg1)
                time.sleep(0.1)
        
        date1 = [8, 25, 31, 2, 8, 0, 0, 0]
        msg1 = can.Message(arbitration_id=476118009, data=date1, extended_id=True)
        can0.send(msg1)
        time.sleep(0.1)

        date1 = [100, 100, 100, 100, 100, 100, 100, 100]
        msg1 = can.Message(arbitration_id=268631964, data=date1, extended_id=True)
        can0.send(msg1)
        time.sleep(0.1)

        date1 = [186, 91, 100, 100, 100, 100, 100, 100]
        msg1 = can.Message(arbitration_id=203751324, data=date1, extended_id=True)
        can0.send(msg1)
        time.sleep(0.1)

        for y in range (0,4):

            for x in range(0,4):
                date1 = [186, 95-y, 100, 100, 100, 100, 100, 100]
                msg1 = can.Message(arbitration_id=id1, data=date1, extended_id=True)
                can0.send(msg1)
                time.sleep(0.1)

        for z in range(0,3):
                date1 = [186, 91, 100, 100, 100, 100, 100, 100]
                msg1 = can.Message(arbitration_id=id1, data=date1, extended_id=True)
                can0.send(msg1)
                time.sleep(0.1)

        date1 = [8, 25, 31, 2, 8, 0, 0, 0]
        msg1 = can.Message(arbitration_id=476118009, data=date1, extended_id=True)
        can0.send(msg1)
        time.sleep(0.1)

        date1 = [100, 100, 100, 100, 100, 100, 100, 100]
        msg1 = can.Message(arbitration_id=268631964, data=date1, extended_id=True)
        can0.send(msg1)
        time.sleep(0.1)

        date1 = [186, 91, 100, 100, 100, 100, 100, 100]
        msg1 = can.Message(arbitration_id=203751324, data=date1, extended_id=True)
        can0.send(msg1)
        time.sleep(0.1)

        for y in range (0,4):

            for x in range(0,4):
                date1 = [186, 90-y, 100, 100, 100, 100, 100, 100]
                msg1 = can.Message(arbitration_id=id1, data=date1, extended_id=True)
                can0.send(msg1)
                time.sleep(0.1)

        for z in range(0,3):
                date1 = [186, 86, 100, 100, 100, 100, 100, 100]
                msg1 = can.Message(arbitration_id=id1, data=date1, extended_id=True)
                can0.send(msg1)
                time.sleep(0.1)

        date1 = [8, 25, 31, 2, 8, 0, 0, 0]
        msg1 = can.Message(arbitration_id=476118009, data=date1, extended_id=True)
        can0.send(msg1)
        time.sleep(0.1)

        date1 = [100, 100, 100, 100, 100, 100, 100, 100]
        msg1 = can.Message(arbitration_id=268631964, data=date1, extended_id=True)
        can0.send(msg1)
        time.sleep(0.1)

        date1 = [186, 91, 100, 100, 100, 100, 100, 100]
        msg1 = can.Message(arbitration_id=203751324, data=date1, extended_id=True)
        can0.send(msg1)
        time.sleep(0.1)

        for y in range (0,4):

            for x in range(0,4):
                date1 = [186, 85-y, 100, 100, 100, 100, 100, 100]
                msg1 = can.Message(arbitration_id=id1, data=date1, extended_id=True)
                can0.send(msg1)
                time.sleep(0.1)

        

    except:
        os.system('sudo ifconfig can0 down')
        time.sleep(0.5)
        os.system('sudo ip link set can0 type can bitrate 250000')
        os.system('sudo ifconfig can0 up')
        return "0","0","0","0"


def counterDate():
    # print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    now = datetime.datetime.now()
    date1 = [8, 25, 31, 2, 8, 0, 0, 0]
    msg1 = can.Message(arbitration_id=476118009, data=date1, extended_id=True)
    can0.send(msg1)
    time.sleep(0.1)
    date2 = [156-(int(now.year)-2000), 100, 100-int(now.month), 100-int(now.day), 100-int(now.hour), 100-int(now.minute), 100-int(now.second), 100]
    msg2 = can.Message(arbitration_id=268631964, data=date2, extended_id=True)
    # can0.send(msg1)
    # time.sleep(0.1)
    can0.send(msg2)
    time.sleep(0.1)
    print(now)




os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native


pushDate()
while True:
    counterDate()
    time.sleep(0.4)


