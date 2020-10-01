
import RPi.GPIO as GPIO
# from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep
import time
import binascii
import os
import can
from datetime import datetime

idPack = [124045411, 124045410, 124045409, 124045408, 124045407, 124045406, 124045405, 124045404,
          124045403, 124045402, 124045401, 124045400, 124045399, 124045398, 124045397, 124045396, 124045395]
baseId = 124045412
dataDock = []
messagePack = []
dataVpack = []
dataIpack = []


def forSaveData(nama_file, data):
    log = open(nama_file, "a")
    log.write(data+'\n')
    log.close()
    print("saved : " + str(data))


def conversion(dataIn):

    byteVp1 = dataIn[4:6]
    byteVp2 = dataIn[6:8]
    byteAp1 = dataIn[8:10]
    byteAp2 = dataIn[10:12]

    outputData1 = int("0x"+byteVp1, 0)
    outputData2 = int("0x"+byteVp2, 0)

    outputData3 = int("0x"+byteAp1, 0)
    outputData4 = int("0x"+byteAp2, 0)
   

    factorv = 0  # 0 untuk a_a1 <<<<< 100, 100 jika  a_a1 >>>> 100
    if outputData1 <=100:
        factorv = 0
    elif outputData1 >100:
        factorv = 1
       

    outputDataVoltage = 25700 - (outputData1+((outputData2-1)*256))

    factora = 0  # 0 untuk a_a1 <<<<< 100, 100 jika  a_a1 >>>> 100
    if outputData3 <= 100:
        factora = 0
    elif outputData3 > 100:
        factora = 1
       

    outputDataCurrent = 25700 - (outputData3+((outputData4-factora)*256))

    # if selectData == "V":
    outputDataVoltage = outputDataVoltage/100
    # if selectData == "A":
    outputDataCurrent = outputDataCurrent/100

    dataVpack.append(outputDataVoltage)
    dataIpack.append(outputDataCurrent)
    return outputDataVoltage, outputDataCurrent


def readDock(waktu):
    # dockdata = dockdata-1
    try:
        data = []
        msg = can0.recv(20)
        uid = msg.arbitration_id
        if uid != 490784999:
            #print (uid)
            if uid in idPack:
                data = baseId-uid
                hex_msg = binascii.hexlify(msg.data)
                dataBattery = str(hex_msg.decode("utf-8"))

                if data not in dataDock:
                    dataDock.append(data)
                    conversion(dataBattery)
                    # print("Dock " + str(data) + " : " +
                    #       str(conversion(dataBattery)))
                    # print(str(dataBattery) + "\n")
                    messagePack.append(dataBattery)
                    dataBattery = ""

                    # print(f'Dock : {data}')

                    # os.system('sudo ifconfig can0 down')
                    # time.sleep(0.5)
                    # os.system('sudo ip link set can0 type can bitrate 250000')
                    # os.system('sudo ifconfig can0 up')
                # forSaveData("/home/pi/ehubv3/logger/logger.txt",str(waktu) + " Dock : " + str(data))

    except:
        print("error coiii ")
        os.system('sudo ifconfig can0 down')
        time.sleep(2)
        os.system('sudo ip link set can0 type can bitrate 250000')
        os.system('sudo ifconfig can0 up')
        return "0", "0"


os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')

time.sleep(1)
can0 = can.interface.Bus(
    channel='can0', bustype='socketcan_ctypes')  # socketcan_native
lastTime = ''
savedData = False

for x in range(0, 1000):


    now = datetime.now()
    dataJam = now.strftime("%Y-%m-%d %H:%M:%S")
    readDock(str(dataJam) + " ")

dataDock.sort()
print(dataDock)
print(dataVpack)
print(dataIpack)
print(dataDock)
print(max(dataVpack))
print(min(dataVpack))
print(max(dataIpack))
print(min(dataIpack))

# counter = 0

# print(conversion(messagePack[0]))
# for target_list in messagePack:
#     print(conversion(messagePack[counter]))
#     counter+=1

# while True:
    # now = datetime.now()
    # dataJam = now.strftime("%Y-%m-%d %H:%M:%S")
    # if str(dataJam) != lastTime:
    # print(dataJam)

    # elif now.second < 5:
    # readDock(str(dataJam) + " ")
    # elif now.second == 5 and savedData == False:
    # dataDock.sort()

    # try:
    # forSaveData("/home/pi/ehubv3/logger/logger.txt",str(dataJam) + " Dock : " + str(dataDock))
    # print("saved")
    # except:
    # forSaveData("/home/pi/ehubv3/logger/error.txt", " Error saved : " + str(dataJam))

    # dataDock.clear()
    # savedData = True

    # elif now.second == 6 :
    # savedData = False

    # lastTime = str(dataJam)
