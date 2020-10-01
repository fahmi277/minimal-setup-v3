import RPi.GPIO as GPIO
# from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep
import time
import binascii
import os
import can
from shiftregister_sia.shift import ShiftRegister
import time
import board
import neopixel


countCek = 0

pixel_pin = board.D18


num_pixels = 16

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


pinDock = [0,1,2,3,8,9,10,11,16,17,18,19]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

data_pin = 4 #pin 14 on the 75HC595
latch_pin = 27 #pin 12 on the 75HC595
clock_pin = 17 #pin 11 on the 75HC595

shift_register = ShiftRegister()

def controlLed(dock,color):

    
      
    dock = dock-1
    if color == 'green':
        pixels[dock] = (0, 255, 0)
    else:
        pixels[dock] = (255, 0, 0)
    pixels.show()

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

        baseId = 124045412

        if uid != 490784999:
            ledId = baseId-uid

           

         

                # countCek += 1
                # print(countCek)

                
                # print("grren")/
                # for a in range(1,17):
                #     if a!=ledId:
                #         pixels[a-1] = (255,0,0)
                #     else:
                #         pixels[a-1] = (0,255,0)
                        
                #         print("red")
            
           
            # else:
                

        if uid == 124045395:
            print("ada dock 17")


            # shifting_dock(2)
            # print("3")
            for x in range(1,17):

                shifting_dock(x)
            #     time.sleep(0.1)
                
            #     print("dock : " + str(x))
            #     if(x>1):
            #         shift_register.setOutput(x, GPIO.LOW)
            #         shift_register.latch()



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

    # shift_register.setOutput(0, GPIO.HIGH)
    # shift_register.setOutput(1, GPIO.HIGH)
    # shift_register.setOutput(2, GPIO.HIGH)
    # shift_register.setOutput(3, GPIO.HIGH)
    # shift_register.setOutput(4, GPIO.HIGH)
    # shift_register.setOutput(5, GPIO.HIGH)
    # shift_register.setOutput(7, GPIO.HIGH)


    # no_shift = int(dox / 8)

    # sisa = dox % 8
    # pengali = 4 * (no_shift + 1)
    # nomor_pin = no_shift * 8 + sisa 
    # shift = (2 ** a) + 1

    # hasil = shift_regis + shift

    numberdock = dox-1
    numberShift = int(numberdock/4)
    pinShift = dox + (4*numberShift)


    shift = int(pinShift)

    print(numberdock)
    print(numberShift)
    print(shift)










    # if dox > 4:
    #     shift = dox+4
    # else:
    #     shift = dox

    shift_register.setOutput(shift-1, GPIO.LOW) # low untuk press

    shift_register.latch()
    change_dock(dox)
    sleep(1)

    shift_register.setOutput(shift-1, GPIO.HIGH) # low untuk press

    shift_register.latch()
    
    
    change_dock(dox)
    sleep(1)
    shift_register.setOutput(shift-1, GPIO.LOW) # low untuk press

    shift_register.latch()
    sleep(1)

# while True:
#     shift_register.setOutput(5, GPIO.LOW)
#     shift_register.latch()
#     sleep(1)
#     shift_register.setOutput(5, GPIO.HIGH)
#     shift_register.latch()
#     sleep(1)

os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

# pixels.fill((255, 0, 0))
pixels.show()

while True:
    
    # print(countCek)
    read()
    # for x in range(1,17):

    #     # pixels[x] = (0,255,0)
    #     pixels[x-1] = (0, 255, 0)

    # pixels.show()





#addressing 4 5 6 7 : tombol 1-4
#addressing 0 1 2 3 : addresing 1-4

#addressing 12 13 14 15 : tombol 5-8
#addressing 8 9 10 11 : addresing 5-8



# for x in range(0,1):



#     shift_register.setOutput(2, GPIO.LOW) # low untuk press
#     shift_register.latch()
#     change_dock(dox)
#     sleep(1)

#     shift_register.setOutput(2, GPIO.HIGH) # low untuk press

#     shift_register.latch()
#     change_dock(dox)
#     sleep(0.7)



    # print("Alhamdulillah")

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