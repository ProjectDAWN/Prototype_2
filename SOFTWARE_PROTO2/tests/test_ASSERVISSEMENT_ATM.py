import RPi.GPIO as GPIO
import time
from am2320 import *

GPIO.setmode(GPIO.BCM)

##########################################################################
#TEST ATMOSPHERIC Module


am2320 = AM2320()
temperature,humidity = am2320.get()

# loop on temperature
print("Temperature: ", temperature)

if temperature < 25 :
    print("Chauffage activé \n")
    pin=27
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

else :
    print("Chauffage desactivé \n")
    GPIO.cleanup(pin)

#loop on humidity
print("Humidity: ",humidity,"\n")

if humidity < 70 :
    pin2=23
    print("MistMaker activé \n")
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.output(pin2, GPIO.HIGH)
    pin1=22
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.output(pin1, GPIO.HIGH)
    print("Ventilateur activé")

else:
    print("MistMaker désactivé \n")
    print("Ventilateur désactivé \n")
    GPIO.cleanup(pin1)
    GPIO.cleanup(pin2)

time.sleep(30)

GPIO.cleanup(pin)
GPIO.cleanup(pin1)
GPIO.cleanup(pin2)
print("MistMaker désactivé \n")
print("Ventilateur désactivé \n")
print("Chauffage desactivé \n")
