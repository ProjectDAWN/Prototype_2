import numpy as np
import pandas as pd

class CSV_reader :

    def __init__(self,file_name):
        self.df = pd.read_csv(file_name,index_col=0)
        self.nb_index = self.df.shape[0]

    def get(self,actuator, caracteristic):
        return(int(self.df.at[actuator,caracteristic]))

    def get_list(self,caracteristic):
        return(list(self.df[caracteristic]))

    def get_infos(self,key):
        return(dict(zip(list(self.df),list(self.df[key]))

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
