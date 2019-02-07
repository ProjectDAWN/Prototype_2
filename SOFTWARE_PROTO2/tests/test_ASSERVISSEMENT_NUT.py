import RPi.GPIO as GPIO
import time
from pH import *

GPIO.setmode(GPIO.BCM)

##########################################################################
#TEST NUTRIENTS Module

#Tests pompes nutriments

#Pompe 1 : BioGrow
pin=25
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
print("Pompe 1 allumée \n")
#Pompe2 : BioBloom
pin2=6
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2, GPIO.HIGH)
print("Pompe 2 allumée \n")
#Pompe3 : Heaven
pin3=12
GPIO.setup(pin3, GPIO.OUT)
GPIO.output(pin3, GPIO.HIGH)
print("Pompe 3 allumée \n")
#Pompe4 : TopMax
pin4=13
GPIO.setup(pin4, GPIO.OUT)
GPIO.output(pin4, GPIO.HIGH)
print("Pompe 4 allumée \n")
#test NUT mixer
pin6=19
GPIO.setup(pin6, GPIO.OUT)
GPIO.output(pin6, GPIO.HIGH)
print("NUT Mixer allumé \n")


time.sleep(30)

GPIO.cleanup(pin)
print("Pompe 1 éteinte \n")
GPIO.cleanup(pin2)
print("Pompe 2 éteinte \n")
GPIO.cleanup(pin3)
print("Pompe 3 éteinte \n")
GPIO.cleanup(pin4)
print("Pompe 4 éteinte \n")
GPIO.cleanup(pin6)
print("NUTMixer éteinte \n")
