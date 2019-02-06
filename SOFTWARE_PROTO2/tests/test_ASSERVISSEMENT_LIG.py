import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)

##########################################################################
#TEST LIGHTING Module

t = datetime.datetime.now()
if t.hour > 8 and t.hour < 20 :
    pin=40
    print("Leds allumée \n")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

else :
    print("Leds éteintes \n")
    GPIO.cleanup()

time.slepp(30)
GPIO.cleanup(pin)
print("Leds éteintes \n")
