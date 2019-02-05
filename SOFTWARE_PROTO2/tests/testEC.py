import RPi.GPIO as GPIO
from AtlasI2C import *

EC_I2C_address = 0x64
#get pH value
device = AtlasI2C(EC_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
EC = string.split(device.query("R"), ",")
print(EC)

