import RPi.GPIO as GPIO
from AtlasI2C import *
import time
import board
import busio
import adafruit_am2320
from ds18b20 import *
from mcp3008 import *

#ini pH
pH_I2C_address = 0x63

# ini EC
EC_I2C_address= 0x64

#ini ATM_T\H
i2c = busio.I2C(board.SCL, board.SDA)


#ini WAR_T
ds18b20 = DS18B20()

#ini WAR_level
mcp3008 = MCP3008()

#Get pH value
device = AtlasI2C(pH_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
pH = str.split(device.query("R"), ",")
print(pH)
time.sleep(5)

# Get EC value
device = AtlasI2C(EC_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
EC = str.split(device.query("R"), ",")
print(EC)
time.sleep(5)

#Get ATM_T\H value
am = adafruit_am2320.AM2320(i2c)
print("Temperature: ", am.temperature)
print("Humidity: ", am.relative_humidity)
time.sleep(5)

# Get WAR_T
ds18b20.read_temp()
time.sleep(5)

# Get WAR_level
mcp3008.read_waterlevel()
time.sleep(5)
