import RPi.GPIO as GPIO
import time
from pH import *

GPIO.setmode(GPIO.BCM)

##########################################################################
#TEST WATERING Module

#get pHvalue

pH = pH()
pH_value = pH.get()

#get EC value
EC = EC()
EC_value = EC.get()

#test pH
if pH_value > 6.5 :

    pin5 =33
    GPIO.setup(pin5, GPIO.OUT)
    GPIO.output(pin5, GPIO.HIGH)
    print("Pompe pH Down allumée \n")
    time.sleep(10)
    GPIO.cleanup(pin5)
    print("Pompe pH Down éteinte \n")

#watering test

pin=18
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
print("WAR_MistMaker allumé \n")

pin2=36
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2, GPIO.HIGH)
print("WAR_Ventilator allumé \n")

time.sleep(20)

GPIO.cleanup(pin)
GPIO.cleanup(pin2)
print("WAR_MistMaker éteint \n")
print("WAR_MVentilator éteint \n")

pin3=11

GPIO.setup(pin3, GPIO.OUT)
GPIO.output(pin3, GPIO.HIGH)
print("WAR_Mixer allumé \n")

time.sleep(15)

GPIO.cleanup(pin3)
print("WAR_Mixer éteint \n")
