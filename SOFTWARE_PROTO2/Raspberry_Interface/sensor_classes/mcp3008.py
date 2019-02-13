import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

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
		self.Vmax = 1.5000
		self.Vmin = 0.3500
		self.Hmax = 213

	def read(self):
		"""Get the water level, it's in millimeter""" 
		chan = AnalogIn(self.mcp,MCP.P0)
		V = chan.voltage
		H = self.Hmax*(self.Vmax-V)/(self.Vmax-self.Vmin)
		return H

	def print(self):
		"""Print the value in terminal"""
		print ("La hauteur immergée vaut" + str(self.read()) + ' mm')