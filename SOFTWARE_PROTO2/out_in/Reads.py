import numpy as np
import pandas as pd

class Actuactors :

    def init(self,file_name):
        self.df = pd.read_csv(file_name)
        
    def print_pins(file_name):
        pins_file = open(file_name,'r')
        names,pins = [],[]
        for pin in pins_file.readlines():
            pin = pin.split(" ")
            names.append(pin[0])
            pins.append(int(pin[1]))
        df = pd.DataFrame(pins, index=names, columns = ['pins'])
        df.to_csv("../Files/share_holder.csv")
