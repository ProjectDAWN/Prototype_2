import RPI.GPIO as GPIO

pH_I2C_address = ...
#get pH value
device = AtlasI2C(pH_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
pH = info = string.split(device.query("I"), ",")[1]
print(pH)
