from Raspberry_Interface.sensor_classes.AtlasI2C import *
import time

class EC:
	"""Class for the conductivity sensor: Get the conductivity in the water"""

	def __init__(self):
		"""Initialize the class  & establish the I2C connection between the Raspberry and the sensor"""
		self.EC_I2C_address= 0x64
		self.device = AtlasI2C(self.EC_I2C_address)

	def get(self):
		"""Get the conductivity value, it's in microSiemens"""
		msg = self.device.query("R") #Get a message from the sensor, it's in a String and it contains the value
		list_msg = msg.split( ) #Parse the string with a blanck a space
		EC_value = list_msg[2].split("\x00")[0] #Get the 3rd value in the list then parse it with \x00 and get the 1st value
		return float(EC_value)

	def read(self):
		"""Print the value in terminal"""
		print("La conductivité vaut " + str(self.get()) + " uS")

	def dry(self):
		self.device.query("Cal,dry")

	def low(self):
		self.put("de conductivité 1413 uS")
		self.wait()
		self.device.query("Cal,low,1413")

	def high(self):
		self.put("de conductivité 12880 uS")
		self.wait()
		self.device.query("Cal,high,12880")

	def calibration(self):
		self.dry()
		self.low()
		self.high()
		print("La sonde est calibrée")


	def put(self,solution):
		print("Mettre la sonde pH dans la solution " + solution)
		isPut = False
		while not isPut:
			rep = input("Rentrer y si c'est fait")
			isPut = (rep=="y")

	def wait(self):
		print("Attendre 2 minutes avec la sonde dans la solution")
		time.sleep(120)
