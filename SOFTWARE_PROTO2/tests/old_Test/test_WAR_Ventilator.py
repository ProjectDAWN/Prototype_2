import RPi.GPIO as GPIO
import time

pin=16

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.HIGH)

time.sleep(15)

GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()