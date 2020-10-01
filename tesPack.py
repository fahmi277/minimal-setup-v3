
import RPi.GPIO as GPIO
# from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep
import time
import binascii
import os
import can
from datetime import datetime

idPack = [124045411, 124045410, 124045409, 124045408, 124045407, 124045406, 124045405, 124045404, 124045403, 124045402, 124045401, 124045400, 124045399, 124045398, 124045397, 124045396, 124045395]
baseId = 124045412
dataDock = []

def forSaveData(nama_file, data):
    log = open(nama_file,"a")
    log.write(data+'\n')
    log.close()
    print("saved : " + str(data))

def readDock(waktu):
    # dockdata = dockdata-1
    try:
            
            data = []
            msg = can0.recv(0.1)
            uid = msg.arbitration_id
            if uid != 490784999:
                # print (uid)
                if uid in idPack:
                    data = baseId-uid
                    if data not in dataDock:
                        dataDock.append(data)
                    print(f'Dock : {data}')
                    # forSaveData("/home/pi/ehubv3/logger/logger.txt",str(waktu) + " Dock : " + str(data))

    except:
            os.system('sudo ifconfig can0 down')
            time.sleep(0.5)
            os.system('sudo ip link set can0 type can bitrate 250000')
            os.system('sudo ifconfig can0 up')
            return "0","0"


os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')
#print("can up")
time.sleep(2)
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native
lastTime = ''
savedData = False

while True:
    now = datetime.now()
    dataJam = now.strftime("%Y-%m-%d %H:%M:%S")
    # if str(dataJam) != lastTime:
    #     print(dataJam)
    readDock(str(dataJam))

    if len(dataDock) > 8:
        print(dataDock)
        dataDock.clear()
        os.system('sudo ifconfig can0 down')
        time.sleep(2)
        os.system('sudo ip link set can0 type can bitrate 250000')
        os.system('sudo ifconfig can0 up')
        break
    





# while True:
#     now = datetime.now()
#     dataJam = now.strftime("%Y-%m-%d %H:%M:%S")
#     if str(dataJam) != lastTime:
#         print(dataJam)
#         # readDock(str(dataJam))
        
#     if now.second == 0 :
#         try:
#             os.system('sudo ip link set can0 type can bitrate 250000')
#             os.system('sudo ifconfig can0 up')
#             print("up suksess")
#         except:
#             print("error up")
        

#     elif now.second < 5:
#         # print("satu detik")
#         # break
#         readDock(str(dataJam) + " ")
#     elif now.second == 5 and savedData == False:
#         #if not dataDock:
            
#         dataDock.sort()
#         forSaveData("/home/pi/ehubv3/logger/logger.txt",str(dataJam) + " Dock : " + str(dataDock))
#         try:
            
#             os.system('sudo ifconfig can0 down')
#             print("down sukses")
#         except:
#             print("errorrr down")
#         dataDock.clear()
#         savedData = True
    
#     elif now.second == 6 :
#         savedData = False
#         # try:
#             # os.system('sudo ip link set can0 type can bitrate 250000')
#             # os.system('sudo ifconfig can0 up')
#             # print("up suksess")
#         # except:
#             # print("error up")
        

#     lastTime = str(dataJam)
