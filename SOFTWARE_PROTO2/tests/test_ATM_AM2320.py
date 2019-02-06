import time
from am2320 import *

#create the I2C shared bus
am2320 = AM2320()


am2320.read()
time.sleep(2)