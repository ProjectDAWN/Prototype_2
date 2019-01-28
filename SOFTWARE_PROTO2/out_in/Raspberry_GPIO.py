#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
import RPi.GPIO as GPIO

def activate(pin,init=GPIO.LOW):
    #penser aux securites
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT, initial = init)

def output(pin, val):
    #penser aux verifs de setup
    GPIO.output(pin, val)

def input(pin):
    return(GPIO.intput(pin))

def cleanup():
    GPIO.cleanup()
