import RPi.GPIO as GPIO
from AtlasI2C import *

pH_I2C_address = 0x63

device = AtlasI2C(pH_I2C_address)     # creates the I2C port object, specify the address or bus if necessary

# Step 1
#pH = string.split(device.query("Cal,mid,7.01"), ",")
#print(pH)

# # Step 2
#pH = string.split(device.query("Cal,low,4.01"), ",")
#print(pH)
#
# # Step 3
pH = string.split(device.query("Cal,high,10.01"), ",")
print(pH)
