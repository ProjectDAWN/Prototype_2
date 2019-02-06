import time
from pH import *
from EC import *
from am2320 import *
from ds18b20 import *
from mcp3008 import *

#ini pH
pH = pH()

# ini EC
EC = EC()

#ini ATM_T\H
am2320 = AM2320()

#ini WAR_T
ds18b20 = DS18B20()

#ini WAR_level
mcp3008 = MCP3008()

#Get pH value 
pH.read()
time.sleep(5)

# Get EC value
EC.read()
time.sleep(5)

#Get ATM_T\H value
am2320.read()
time.sleep(5)

# Get WAR_T
ds18b20.read()
time.sleep(5)

# Get WAR_level
mcp3008.read()
time.sleep(5)
