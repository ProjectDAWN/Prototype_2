import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)
print("Leds allumée \n")

pin=21

##########################################################################
#TEST LIGHTING Module

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
print("Leds éteintes \n")

time.sleep(15)

GPIO.cleanup(pin)
print("Leds allumée \n")

time.sleep(15)

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
print("Leds éteintes \n")

time.sleep(15)

GPIO.cleanup(pin)
print("Leds allumée \n")
