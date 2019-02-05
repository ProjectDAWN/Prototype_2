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
		self.mcp = MCP.MCP3008(spi, cs)

	def read_waterlevel(self):
		chan = AnalogIn(self.mcp,MCP.P0)
		print('Raw ADC Value: ', chan.value)
		print('ADC Voltage: ' + str(chan.voltage) + 'V')