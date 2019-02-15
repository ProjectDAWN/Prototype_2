import sys
path = sys.path[0]+"/.."
sys.path.append(path)
from Raspberry_Interface.sensor_classes.EC import *

EC = EC()

EC.calibrate()