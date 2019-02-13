import time
from pH import *
from EC import *
from am2320_Humidity import *
from am2320_Temperature import *
from ds18b20 import *
from mcp3008 import *

#ini pH
pH = pH()

# ini EC
EC = EC()

#ini ATM_H
am2320_Humidity = AM2320_Humidity()

#ini ATM_T
am2320_Temperature = AM2320_Temperature()

#ini WAR_T
ds18b20 = DS18B20()

#ini WAR_level
mcp3008 = MCP3008()

#Get pH value 
pH.print()
time.sleep(5)

# Get EC value
EC.print()
time.sleep(5)

#Get ATM_H value
am2320_Humidity.print()
time.sleep(5)


#Get ATM_T value
am2320_Temperature.print()
time.sleep(5)

# Get WAR_T
ds18b20.print()
time.sleep(5)

# Get WAR_level
mcp3008.print()
time.sleep(5)
