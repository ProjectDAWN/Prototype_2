import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
ATMmistmaker_pin = ...
GPIO.setup(ATMmistmaker_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(ATMmistmaker_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(ATMmistmaker_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(ATMmistmaker_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(ATMmistmaker_pin, GPIO.LOW)
