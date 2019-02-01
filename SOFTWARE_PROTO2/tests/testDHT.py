import adafruit_dht
import board
import time

dht=adafruit_dht.DHT22(board.D6)
dht.temperature
dht.humidity
time.sleep(5)
dht.temperature
dht.humidity