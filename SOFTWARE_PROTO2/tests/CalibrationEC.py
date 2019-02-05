import RPi.GPIO as GPIO
from AtlasI2C import *

EC_I2C_address= 0x64

device = AtlasI2C(EC_I2C_address)     # creates the I2C port object, specify the address or bus if necessary

#Step 1

#EC = string.split(device.query("Cal,dry"), ",")
#print(EC)

#Step 2

#EC = string.split(device.query("Cal,low,1413"), ",")
#print(EC)

#Step 3

EC = string.split(device.query("Cal,high,12880"), ",")
print(EC)
