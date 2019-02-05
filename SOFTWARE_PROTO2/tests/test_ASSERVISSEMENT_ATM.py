import RPi.GPIO as GPIO
from AtlasI2C import *
import time
import board
import busio
import adafruit_am2320
from ds18b20 import *

GPIO.setmode(GPIO.BOARD)

##########################################################################
#TEST ATMOSPHERIC Module

while True :
    # loop on temperature
    i2c = busio.I2C(board.SCL, board.SDA)
    am = adafruit_am2320.AM2320(i2c)
    print("Temperature: ", am.temperature)

    if am.temperature < 25 :
        print("Chauffage activé \n")
        pin=13
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    else :
        print("Chauffage desactivé \n")
        GPIO.cleanup(pin)

    #loop on humidity
    print("Humidity: ", am.relative_humidity)

    if am.relative_humidity < 70 :
        pin=16
        print("MistMaker activé \n")

        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        pin1=15
        
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.output(pin1, GPIO.HIGH)
        print("Ventilateur activé")

    else:
        print("MistMaker désactivé \n")
        print("Ventilateur désactivé \n")
        GPIO.cleanup(pin1)
        GPIO.cleanup(pin)

        time.sleep(15)
