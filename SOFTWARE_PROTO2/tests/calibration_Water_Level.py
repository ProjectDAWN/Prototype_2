import sys
path = sys.path[0]+"/.."
sys.path.append(path)
from Raspberry_Interface.sensor_classes.mcp3008 import *

mcp3008 = MCP3008()

mcp3008.calibrate()