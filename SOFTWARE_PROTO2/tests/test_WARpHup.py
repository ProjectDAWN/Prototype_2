import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
WARpHup_pin = ...
GPIO.setup(WARpHup_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(WARpHup_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARpHup_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(WARpHup_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARpHup_pin, GPIO.LOW)
