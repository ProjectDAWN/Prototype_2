import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from math import *
import sys
path = sys.path[0]+"/../.."
sys.path.append(path)
from Data_Managers.Reads_Writes.CSV_reader import CSV_reader
system_file = "Files/system.csv"
model = "Prototype_2"

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
		self.system_config = CSV_reader(system_file)

	def read(self):
		"""Get the water level, it's in millimeter"""
		chan = AnalogIn(self.mcp,MCP.P0)
		V = chan.voltage
		Vmax = self.system_config.get(model,"water_level_Vmax")
		Vmin = self.system_config.get(model,"water_level_Vmin")
		Hmax = self.system_config.get(model,"water_level_Hmax")
		H = Hmax*(Vmax-V)/(Vmax-Vmin)
		H = max(0,H)
		return round(H)

	def voltage(self):
		chan = AnalogIn(self.mcp,MCP.P0)
		V = chan.voltage
		return V

	def low(self):
		print("Récupération de la tension à vide")
		#self.Vmax = self.voltage()

	def high(self):
		print("Remplir de l'eau jusqu'en haut du capteur")
		isPut = False
		while not isPut:
			rep = input("Rentrer y si c'est fait")
			isPut = (rep=="y")
		#self.Vmin = self.voltage()

	def calibrate(self):
		self.low()
		self.high()
		print("Le capteur de niveau d'eau est calibré")
