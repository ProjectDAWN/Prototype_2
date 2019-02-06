import RPi.GPIO as GPIO
import time
from pH import *

GPIO.setmode(GPIO.BCM)

##########################################################################
#TEST NUTRIENTS Module

#Tests pompes nutriments

#Pompe 1
pin=25
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
print("Pompe 1 allumée \n")
time.sleep(5)
GPIO.cleanup(pin)
print("Pompe 1 éteinte \n")
time.sleep(10)

#Pompe2
pin2=6
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2, GPIO.HIGH)
print("Pompe 2 allumée \n")
time.sleep(5)
GPIO.cleanup(pin2)
print("Pompe 2 éteinte \n")
time.sleep(10)

#Pompe3
pin3=12
GPIO.setup(pin3, GPIO.OUT)
GPIO.output(pin3, GPIO.HIGH)
print("Pompe 3 allumée \n")
time.sleep(5)
GPIO.cleanup(pin3)
print("Pompe 3 éteinte \n")
time.sleep(10)

#Pompe4
pin4=13
GPIO.setup(pin4, GPIO.OUT)
GPIO.output(pin4, GPIO.HIGH)
print("Pompe 4 allumée \n")
time.sleep(5)
GPIO.cleanup(pin4)
print("Pompe 4 éteinte \n")
time.sleep(10)


# pHDOWN
pH = pH()
value = pH.get()


pin5 = 20
GPIO.setup(pin5, GPIO.OUT)
GPIO.output(pin5, GPIO.HIGH)
print("Pompe pH Down allumée \n")
time.sleep(10)
GPIO.cleanup(pin5)
print("Pompe pH Down éteinte \n")

#test NUT mixer
pin6=19
GPIO.setup(pin6, GPIO.OUT)
GPIO.output(pin6, GPIO.HIGH)
print("NUT Mixer allumé \n")
time.sleep(15)
GPIO.cleanup(pin6)
print("NUTMixer éteinte \n")
