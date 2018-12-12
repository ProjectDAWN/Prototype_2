import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
ATMelectricwarmer_pin = ...
GPIO.setup(ATMelectricwarmer_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(ATMelectricwarmer_pinn, GPIO.HIGH)
time.sleep(10)
GPIO.output(ATMelectricwarmer_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(ATMelectricwarmer_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(ATMelectricwarmer_pinn, GPIO.LOW)
