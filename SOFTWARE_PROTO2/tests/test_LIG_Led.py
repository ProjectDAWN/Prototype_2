import RPi.GPIO as GPIO
import time

pin=21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.HIGH)

print("LED éteintes")

time.sleep(35)

GPIO.cleanup()

print("LED allumées")