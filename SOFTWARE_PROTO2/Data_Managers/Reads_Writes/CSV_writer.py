import numpy as np
import pandas as pd
import sys

class CSV_writer :

    def __init__(self,file_name):
        self.df = pd.read_csv(sys.path[0]+"/"+file_name,index_col=0)
        self.nb_index = self.df.shape[0]
        self.file_name = file_name

    def set(self,id, caracteristic,value):
        self.df.at[id,caracteristic] = value

    def set_list(self,caracteristic,list):
        self.df[caracteristic] = pd.DataFrame(list)

    def set_infos(self,key):
        return(dict(zip(list(self.df),list(self.df.loc[key]))))

    def write():
        self.df.to_csv(sys.path[0]+"/"+self.file_name)

    def txt_to_pandas(file_name,cvs_name):
        file = open(file_name,'r')
        names,items = [],[]
        for item in file.readlines():
            item = item.split(" ")
            names.append(item[0])
            items.append(int(item[1]))
        df = pd.DataFrame(pins, index=names, columns = ['pins'])
        return(df)
