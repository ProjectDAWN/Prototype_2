def read_pins_dict(file_name):
    pins_file = open(file_name,'r')
    pin_dict = dict()
    for pin in pins_file.readlines():
        pin = pin.split()
        dict[pin[0]] = pin[1]
    return(dict)
