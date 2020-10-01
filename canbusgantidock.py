from time import sleep
import time
import binascii
import os
import can
import time


def change_dock (uid):
    try:
        dock = uid
        base_dock = 0x0c24c865
        id1 = 0x1002ff9c
        id2 = 0x1c60fbf9
        id3 = 0x0c24ff9c
        id4 = base_dock-dock
        id5 = 0x0c24ff9c

        print(base_dock)
        print(id1)
        print(id2)
        print(id3)
        print(id4)
        print(id5)

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
        print("dock" + str(id1))
    except:
        os.system('sudo ifconfig can0 down')
        time.sleep(0.5)
        os.system('sudo ip link set can0 type can bitrate 250000')
        os.system('sudo ifconfig can0 up')
        print("error")
        return "0","0","0","0"




os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

change_dock(2)
