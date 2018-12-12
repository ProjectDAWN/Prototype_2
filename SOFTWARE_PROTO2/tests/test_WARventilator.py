import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
WARventilator_pin = ...
GPIO.setup(WARventilator_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(WARventilator_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARventilator_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(WARventilator_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARventilator_pin, GPIO.LOW)
