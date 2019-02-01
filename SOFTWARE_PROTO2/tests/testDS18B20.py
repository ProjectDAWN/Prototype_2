from ds18b20 import *
import time

ds18b20 = DS18B20()
ds18b20.read_temp()
time.sleep(10)
ds18b20.read_temp()