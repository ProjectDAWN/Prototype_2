import board
import busio
import adafruit_am2320

class AM2320:

	def __init__(self):
		self.i2c = busio.I2C(board.SCL, board.SDA)
		self.am = adafruit_am2320.AM2320(self.i2c)

	def get(self):
		return (self.am.temperature,self.am.relative_humidity)

	def read(self):
		print("La température de l'air vaut " + str(self.get[0]) + " °C")
		print("L'humidité de l'air vaut " + str(self.get[1] + " %")