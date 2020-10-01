import serial
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu
import time
import pyrebase
# import redis
from pyModbusTCP.client import ModbusClient

SERVER_HOST = "192.168.200.18"
SERVER_PORT = 502
address_currpack = 8448


# c = ModbusClient()

# c.host(SERVER_HOST)
# c.port(SERVER_PORT)
# c.open()

master = modbus_rtu.RtuMaster(serial.Serial("/dev/ttyS0", baudrate= 115200, parity='N', stopbits=1))
master.open
master.set_timeout(1)
master.set_verbose(True)

# def tes_mppt():
#     curr = c.read_holding_registers(58634, 16)
#     time.sleep(0.5)
#     return curr
    
def tes_mppt(uid):
    read = master.execute(uid,cst.READ_INPUT_REGISTERS,12544, 6)
    time.sleep(0.5)
    return read

while True:
    dataMppt1 = tes_mppt(1)
    if dataMppt1 != None:
        print("MPPT 1 :" + str(dataMppt1))
        break
    time.sleep(1)

while True:
    dataMppt2 = tes_mppt(2)
    if dataMppt2 != None:
        print("MPPT 2 :" + str(dataMppt2))
        break
    time.sleep(1)


#print(tes_mppt(2))
# curr = c.read_holding_registers(address_currpack, 16)
# print(curr)


