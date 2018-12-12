import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
WARultrasonicmistmaker_pin = ...
GPIO.setup(WARultrasonicmistmaker_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(WARultrasonicmistmaker_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARultrasonicmistmaker_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(WARultrasonicmistmaker_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARultrasonicmistmaker_pin, GPIO.LOW)
