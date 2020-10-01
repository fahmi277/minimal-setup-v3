import os
import can
import time
import binascii

print("=== Ehub V3 ===")

def readEM():
    try:
        data = []
        msg = can0.recv(0.1)
        uid = msg.arbitration_id

        if uid == 490784999 :
            hex_msg = binascii.hexlify(msg.data)
            str_msg = str(hex_msg)
            # print(str_msg)
            byteA1 = "0x"+ str_msg[6:8]
            bytemA1 = "0x"+ str_msg[8:10]
            byteA2 = "0x"+ str_msg[10:12]
            bytemA2 = "0x"+ str_msg[12:14]
            # print (byteA1)
            # print (bytemA1)
            # print (byteA2)
            # print (bytemA2)
            dataAmpere1 = int(byteA1,0)
            datamAmpere1 = int(bytemA1,0)/100

            dataAmpere2 = int(byteA2,0)
            datamAmpere2 = int(bytemA2,0)/100


            currentEM1 = dataAmpere1+datamAmpere1
            currentEM2 = dataAmpere2+datamAmpere2

            print("\n===  ===\n")
            
            print ("Load Vsat : "+str(currentEM1))
            print ("Load BTS : "+str(currentEM2))

            print("\n===  ===\n")


    except:
            os.system('sudo ifconfig can0 down')
            time.sleep(0.5)
            os.system('sudo ip link set can0 type can bitrate 250000')
            os.system('sudo ifconfig can0 up')
            return "0","0","0","0"

def readV():
    try:
            data = []
            msg = can0.recv(0.1)
            uid = msg.arbitration_id

            # can message pembuka isinya pack V dan current

            if uid == 124045395 : 

                hex_msg = binascii.hexlify(msg.data)
                str_msg = str(hex_msg)
                print(str_msg)
                byteVp1 = "0x"+ str_msg[6:8]
                byteVp2 = "0x"+ str_msg[8:10]
               
                
                byteIp1 = "0x"+ str_msg[10:12]
                byteIp2 = "0x"+ str_msg[12:14]

                # print(byteVp1)
                # print(byteVp2)
                # print(byteIp1)
                # print(byteIp2)

                v_b1 = int(byteVp1,0)
                v_b2 = int(byteVp2,0)

                factorv = 0 # 0 untuk a_a1 <<<<< 100, 100 jika  a_a1 >>>> 100
                if v_b1<=100 and v_b1>0:
                    factorv = 0
                elif v_b1>100:
                    factorv =1

                v_pack = 25700 - (v_b1+((v_b2-factorv)*256))

                print(v_b2)

                a_a1 = int(byteIp1,0)
                a_a2 = int(byteIp2,0)
                # print(a_a1)
                # print(a_a2)
                factor = 0 # 0 untuk a_a1 <<<<< 100, 100 jika  a_a1 >>>> 100
                if a_a1<=100 and a_a1>0:
                    factor = 0
                elif a_a1>100:
                    factor =1
                i_pack = 25700 - (a_a1+((a_a2-factor)*256))


                print(v_pack/100)
                print(i_pack/10) #nilai positif menandakan pengecasan, negatif menandakan penggunaan

            



    except:
            os.system('sudo ifconfig can0 down')
            time.sleep(0.5)
            os.system('sudo ip link set can0 type can bitrate 250000')
            os.system('sudo ifconfig can0 up')
            return "0","0","0","0"


os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

while True:

    readEM()
    #readV()
    # time.sleep(2)