import numpy as np
import pandas as pd
import sys

class CSV_writer :

    """CSV file data writer

    Allow to write and modify csv files without considering the
    technology used to do it (here pandas).
    """

    def __init__(self,file_name):
        """Constructor of CSV_reader class

        file_name -- [string] name of the file to read which contains the datas
        
        """
        self.df = pd.read_csv(sys.path[0] + "/" + file_name,index_col=0)#think about the case that csv doesn't exist
        self.nb_index = self.df.shape[0]
        self.file_name = file_name

    def set(self,id, caracteristic,value):
        """Update one value of the DataFrame

        Keyword Arguments:
        id -- [string or int] the line position
        caracteristic -- [string] the column position
        value -- [any] the value to put in

        """
        self.df.at[id,caracteristic] = value

    def set_list(self,caracteristic,list):
        """Update one column of the DataFrame

        Keyword Arguments:
        caracteristic -- [string] the column position
        list -- [list] the values to put in

        """
        self.df[caracteristic] = pd.DataFrame(list)

    def set_infos(self,key,infos):
        """Update one line of the DataFrame

        Keyword Arguments:
        key -- [string or int] the line position
        infos -- [any] the value to put in

        """
        infos = pd.DataFrame(infos)#change to add key in the df
        df.update(infos)

    def write(self,file=None):
        """Write the DataFrame in a csv, if file is not given, write in self.file_name

        file -- [string] file to write the DataFrame on (default : None)

        """
        if file:
            target = file
        else:
            target = self.file_name

        self.df.to_csv(sys.path[0] + "/" + target)

    def txt_to_pandas(file_name):
        """Return DataFrame from a formated .txt file

        file_name -- [string] formated .txt file to read

        """
        file = open(file_name,'r')
        names,items = [],[]
        for item in file.readlines():
            item = item.split(" ")
            names.append(item[0])
            items.append(int(item[1]))
        df = pd.DataFrame(pins, index=names, columns = ['pins'])
        return(df)
