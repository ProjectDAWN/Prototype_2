from Raspberry_Interface.sensor_classes.AtlasI2C import *
import time

class pH:
	"""Class for the pH sensor:  Get the pH value in the water"""

	def __init__(self):
		"""Initialize the classe & establish the I2C connection between the Raspberry and the sensor"""
		self.pH_I2C_address = 0x63
		self.device = AtlasI2C(self.pH_I2C_address)

	def read(self):
		"""Get the pH value"""
		msg = self.device.query("R") #Get a message from the sensor, it's in a String and it contains the value
		list_msg = msg.split( ) #Parse the string with a blanck a space
		pH_value = list_msg[2].split("\x00")[0] #Get the 3rd value in the list then parse it with \x00 and get the 1st value
		return float(pH_value)

	def mid(self):
		self.put("de pH 7.01")
		self.wait()
		self.device.query("Cal,mid,7.01")

	def low(self):
		self.put("de pH 4.01")
		self.wait()
		self.device.query("Cal,low,4.01")

	def high(self):
		self.put("de pH 10.01")
		self.wait()
		self.device.query("Cal,high,10.01")

	def calibrate(self):
		self.mid()
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

