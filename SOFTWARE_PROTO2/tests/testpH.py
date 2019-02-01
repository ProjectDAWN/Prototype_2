import RPi.GPIO as GPIO
from AtlasI2C import *

pH_I2C_address = 0x63
#get pH value
device = AtlasI2C(pH_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
pH = string.split(device.query("R"), ",")
print(pH)

