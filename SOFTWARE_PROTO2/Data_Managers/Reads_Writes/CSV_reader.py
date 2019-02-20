import numpy as np
import pandas as pd
import sys

class CSV_reader :

    def __init__(self,file_name):
        self.df = pd.read_csv(sys.path[0]+"/"+file_name,index_col=0)
        self.nb_index = self.df.shape[0]

    def get(self,id, caracteristic):
        return(self.df.at[id,caracteristic])

    def get_list(self,caracteristic):
        return(list(self.df[caracteristic]))

    def get_infos(self,key):
        return(dict(zip(list(self.df),list(self.df.loc[key]))))
