import RPi.GPIO as GPIO
import time

pin = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)

print("ON")

time.sleep(15)

GPIO.output(pin, GPIO.LOW)

print("OFF")

time.sleep(15)

GPIO.output(pin, GPIO.HIGH)

print("ON")

GPIO.cleanup(pin)