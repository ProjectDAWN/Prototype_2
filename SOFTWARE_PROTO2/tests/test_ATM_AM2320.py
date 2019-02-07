import RPi.GPIO as GPIO
import time
from am2320 import *

GPIO.setmode(GPIO.BCM)
#create the I2C shared bus
am2320 = AM2320()


am2320.read()
time.sleep(2)