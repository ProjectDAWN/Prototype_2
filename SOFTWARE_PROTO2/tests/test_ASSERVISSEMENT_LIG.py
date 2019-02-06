import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)

##########################################################################
#TEST LIGHTING Module

t = datetime.datetime.now()
if t.hour > 8 and t.hour < 20 :
    pin=21
    print("Leds allumée \n")
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

else :
    print("Leds éteintes \n")
    GPIO.cleanup()

time.sleep(30)
GPIO.cleanup(pin)
print("Leds éteintes \n")
