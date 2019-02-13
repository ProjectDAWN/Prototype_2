from test_sensor import test
sensor_list = ["pH","conductivity","waterlevel","water_temperature","temperature","humidity"]
for sensor in sensor_list:
	test(sensor)