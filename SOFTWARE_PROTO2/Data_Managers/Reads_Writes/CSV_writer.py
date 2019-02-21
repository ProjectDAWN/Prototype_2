import numpy as np
import pandas as pd
import sys

class CSV_writer :
    """Allow to write and modify csv files thanks to pandas library"""
    def __init__(self,file_name):
        """ Initialize with a df"""
        self.df = pd.read_csv(sys.path[0]+"/"+file_name,index_col=0)#think about the case that csv doesn't exist
        self.nb_index = self.df.shape[0]
        self.file_name = file_name

    def set(self,id, caracteristic,value):
        """update 1 value of df

        caracteristic : string

        value : any

        """
        self.df.at[id,caracteristic] = value

    def set_list(self,caracteristic,list):
        """update 1 column of df

        caracteristic : string

        list : list

        """
        self.df[caracteristic] = pd.DataFrame(list)

    def set_infos(self,key,infos):
        """update 1 line of df

        key : string

        infos : dict

        """
        infos = pd.DataFrame(infos)#change to add key in the df
        df.update(infos)

    def write(self,file=None):
        """write the df in a csv, if file is not given, write in self.file_name

        file : string

        """
        if file:
            target = file
        else:
            target = self.file_name

        self.df.to_csv(sys.path[0]+"/"+target)

    def txt_to_pandas(file_name):
        """edit pandas df from a formated txt file

        file_name : string

        """
        file = open(file_name,'r')
        names,items = [],[]
        for item in file.readlines():
            item = item.split(" ")
            names.append(item[0])
            items.append(int(item[1]))
        df = pd.DataFrame(pins, index=names, columns = ['pins'])
        return(df)
