import numpy as np
import pandas as pd

class CSV_reader :

    def __init__(self,file_name):
        self.df = pd.read_csv(file_name,index_col=0)
        self.nbPins = self.df.shape[0]

    def get_pin(self,actuator):
        return(int(self.df.at[actuator,"pin"]))
    def get_GPIO(self,actuator):
        return(int(self.df.at[actuator,"GPIO"]))
    def get_Relay(self,actuator):
        return((self.df.at[actuator,"Relay"]))

    def get_pin_list(self):
        return(list(self.df["pin"]))
    def get_GPIO_list(self):
        return(list(self.df["GPIO"]))
    def get_Relay_list(self):
        return(list(self.df["Relay"]))

    def print_pins(file_name):
        pins_file = open(file_name,'r')
        names,pins = [],[]
        for pin in pins_file.readlines():
            pin = pin.split(" ")
            names.append(pin[0])
            pins.append(int(pin[1]))
        df = pd.DataFrame(pins, index=names, columns = ['pins'])
        df.to_csv("../Files/share_holder.csv")
        return(df)
