import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from math import *

class MCP3008:
	"""Class for the mcp3008 sensor: Get the water level in the reservoir"""

	def __init__(self):
		"""Initialize the class & establish the connection with the sensor"""

		# create the spi bus
		self.spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
		# create the cs (chip select)
		self.cs = digitalio.DigitalInOut(board.D5)
 
		# create the mcp object
		self.mcp = MCP.MCP3008(self.spi, self.cs)
		self.Vmax = 1.891728
		self.Vmin = 0.947475
		self.Hmax = 213

	def read(self):
		"""Get the water level, it's in millimeter""" 
		chan = AnalogIn(self.mcp,MCP.P0)
		V = chan.voltage
		H = self.Hmax*(self.Vmax-V)/(self.Vmax-self.Vmin)
		return round(H)

	def print(self):
		"""Print the value in terminal"""
		print ("La hauteur immergée vaut " + str(self.read()) + ' mm')


	def voltage(self):
		chan = AnalogIn(self.mcp,MCP.P0)
		V = chan.voltage
		return V

	def low(self):
		print("Récupération de la tension à vide")
		self.Vmax = self.voltage()

	def high(self):
		print("Remplir de l'eau jusqu'en haut du capteur")
		isPut = False
		while not isPut:
			rep = input("Rentrer y si c'est fait")
			isPut = (rep=="y")
		self.Vmin = self.voltage()

	def calibrate(self):
		self.low()
		self.high()
		print("Le capteur de niveau d'eau est calibré")