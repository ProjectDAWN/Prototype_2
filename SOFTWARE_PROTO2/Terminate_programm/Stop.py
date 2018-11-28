GPIO.setmode(GPIO.BOARD)

####### Atmospheric module (ATM)
ATMventilator_pin =  ...
GPIO.setup(ATMventilator_pin, GPIO.OUT, initial = GPIO.LOW)
ATMmistmaker_pin = ...
GPIO.setup(ATMmistmaker_pin, GPIO.OUT, initial = GPIO.LOW)
ATMelectricwarmer_pin = ...
GPIO.setup(ATMelectricwarmer_pin, GPIO.OUT, initial = GPIO.LOW)

####### Lighting module (LIG)
LIGled_pin = ...
GPIO.setup(LIGled_pin, GPIO.OUT, initial = GPIO.LOW)
####### Nutrients module (NUT)
NUTpump1_pin = ...                     #Flora Micro/Mato
GPIO.setup(NUTpump1_pin, GPIO.OUT, initial = GPIO.LOW)
NUTpump2_pin = ...                     #FloraGro
GPIO.setup(NUTpump2_pin, GPIO.OUT, initial = GPIO.LOW)
NUTpump3_pin = ...                     #FloraBloom
GPIO.setup(NUTpump3_pin, GPIO.OUT, initial = GPIO.LOW)
size_x_bac = ...
size_y_bac ...
####### Watering module (WAT)
WARultrasonicmistmaker_pin = ...
GPIO.setup(WARultrasonicmistmaker_pin, GPIO.OUT, initial = GPIO.LOW)
WARmixer_pin = ...
GPIO.setup(WARmixer_pin, GPIO.OUT, initial = GPIO.LOW)
WARventilator_pin = ...
GPIO.setup(WARventilator_pin, GPIO.OUT, initial = GPIO.LOW)
WARwaterlevel_pin = ...
WARpHup_pin = ...
GPIO.setup(WARpHup_pin, GPIO.OUT, initial = GPIO.LOW)
WARpHdown_pin = ...
GPIO.setup(WARpHdown_pin, GPIO.OUT, initial = GPIO.LOW)
pH_I2C_adress = ...
EC_I2C_address = ...

"put all the GPIO pins at LOW value"
#ATM module
GPIO.output(ATMventilator_pin, GPIO.LOW)
GPIO.output(ATMmistmaker_pin, GPIO.LOW)
GPIO.output(ATMelectricwarmer_pin, GPIO.LOW)
#LIG module
GPIO.output(LIGled_pin, GPIO.LOW)
#NUT module
GPIO.output(NUTpump1_pin, GPIO.LOW)
GPIO.output(NUTpump2_pin, GPIO.LOW)
GPIO.output(NUTpump3_pin, GPIO.LOW)
#WAT module
GPIO.output(WARultrasonicmistmaker_pin, GPIO.LOW)
GPIO.output(WARmixer_pin, GPIO.LOW)
GPIO.output(WARventilator_pin, GPIO.LOW)
GPIO.output(WARwatermevel_pin, GPIO.LOW)
GPIO.output(WARpHup_pin, GPIO.LOW)
GPIO.output(WARpHdown_pin, GPIO.LOW)
