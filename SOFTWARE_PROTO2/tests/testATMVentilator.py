import RPi.GPIO as GPIO
import time

pin1=15
pin2=22

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

GPIO.output(pin1, GPIO.HIGH)
GPIO.output(pin2, GPIO.HIGH)

print("ON")

time.sleep(15)

GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)

print("OFF")


time.sleep(15)

GPIO.output(pin1, GPIO.HIGH)
GPIO.output(pin2, GPIO.HIGH)

print("ON")

GPIO.cleanup(pin1)

time.sleep(15)

GPIO.cleanup(pin2)