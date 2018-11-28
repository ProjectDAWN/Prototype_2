EC_I2C_address= ...
#get EC value
device = AtlasI2C(EC_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
EC = info = string.split(device.query("I"), ",")[1]
print(EC)
