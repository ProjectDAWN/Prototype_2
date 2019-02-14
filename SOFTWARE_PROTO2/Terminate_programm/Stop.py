from Raspberry_Interface import GPIO_Actuators, GPIO_Sensors
import time

InOutMode = "GPIO"
chanel_file = "Files/Actuators.csv"

actuators = GPIO_Actuators.GPIO_Actuators(chanel_file,InOutMode)
actuators.cleanup()
time.sleep(25)
actuators.activate("LIG_Led")
print("Stopped !")
