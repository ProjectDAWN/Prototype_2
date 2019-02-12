import sys
path = sys.path[0]+"/.."
sys.path.append(path)
from test_act import test
from Data_Managers.Reads_Writes.CSV_reader import CSV_reader
pin_file = path + "/Files/Actuators.csv"
actuators = CSV_reader(pin_file)

for actuator in actuators.get_list("pin"):
	test(actuator)