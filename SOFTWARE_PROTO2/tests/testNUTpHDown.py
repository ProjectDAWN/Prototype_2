import RPi.GPIO as GPIO
import time

pin=33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.HIGH)

time.sleep(15)

GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()