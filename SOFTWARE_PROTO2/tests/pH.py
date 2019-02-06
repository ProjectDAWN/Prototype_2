from AtlasI2C import *
import time

class pH:

	def __init__(self):
		self.pH_I2C_address = 0x63
		self.device = AtlasI2C(self.pH_I2C_address)

	def read(self):
		pH = self.device.query("R").split()[2]
		print("Le ph vaut " +str(pH))

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

	def calibration(self):
		self.mid()
		self.low()
		self.high()
		print("La sonde est calibrée")

	def put(self,solution)
		print("Mettre la sonde pH dans la solution " + solution)
		isPut = False
		while !isPut:
			rep = input("Rentrer y si c'est fait")
			isPut = (rep=="y")

	def wait(self)
		print("Attendre 2 minutes avec la sonde dans la solution")
		time.sleep(120)