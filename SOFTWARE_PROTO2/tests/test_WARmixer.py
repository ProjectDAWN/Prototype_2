import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
WARmixer_pin = ...
GPIO.setup(WARmixer_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(WARmixer_pinn, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARmixer_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(WARmixer_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(WARmixer_pin, GPIO.LOW)
