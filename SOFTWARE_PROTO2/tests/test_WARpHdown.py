import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
WARpHdown_pin = ...
GPIO.setup(WARpHdown_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(WARpHdown_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARpHdown_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(WARpHdown_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARpHdown_pin, GPIO.LOW)
