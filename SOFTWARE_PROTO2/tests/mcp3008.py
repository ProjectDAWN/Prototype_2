import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

class MCP3008:

	def __init__(self):

		# create the spi bus
		self.spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
		# create the cs (chip select)
		self.cs = digitalio.DigitalInOut(board.D5)
 
		# create the mcp object
		self.mcp = MCP.MCP3008(self.spi, self.cs)
		self.Vmax = 1.5000
		self.Vmin = 0.3500
		self.Hmax = 213

	def get(self):
		chan = AnalogIn(self.mcp,MCP.P0)
		V = chan.voltage
		H = self.Hmax*(self.Vmax-V)/(self.Vmax-self.Vmin)
		return H

	def read(self):
		print ("La hauteur immergée vaut" + str(self.H) + ' mm')