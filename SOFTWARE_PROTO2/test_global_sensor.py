from test_sensor import test
sensor_list = ["pH","conductivity","water_level","water_temperature","temperature","humidity"]
for sensor in sensor_list:
	test(sensor)
