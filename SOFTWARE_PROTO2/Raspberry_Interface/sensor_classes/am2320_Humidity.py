import board
import busio
import adafruit_am2320

class AM2320_Humidity:
	"""Class for the am2320 sensor: Get the humidity of the atmosphere"""

	def __init__(self):
		"""Initialize the class & establish the I2C connection between the Raspberry and the sensor"""
		self.i2c = busio.I2C(board.SCL, board.SDA)
		self.am = adafruit_am2320.AM2320(self.i2c)

	def read(self):
		"""Get the value from the sensor. It's a tuple of float (temperature,humidity)"""
		try:
			return self.am.relative_humidity
		except:
			print("error atmosphere humidity")
			return 0