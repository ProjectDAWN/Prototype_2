import numpy as np
import pandas as pd
import sys

class CSV_reader :

    """CSV file data reader

    Allow to read and use datas in csv files without considering the
    technology used to do it (here pandas).
    """

    def __init__(self,file_name):
        """Constructor of CSV_reader class

        file_name -- [string] name of the file to read which contains the datas
        """
        self.df = pd.read_csv(sys.path[0] + "/" + file_name,index_col=0)
        self.nb_index = self.df.shape[0]

    def get(self,id, caracteristic):
        """Return one value found with its coordinates in DataFrame

        Keyword Arguments:
        id -- [string or int] the line position
        caracteristic -- [string] the column position

        """
        return(self.df.at[id,caracteristic])

    def get_list(self,caracteristic):
        """Return a list of value all the value of one column

        Keyword Arguments:
        caracteristic -- [string] the column position

        """
        return(list(self.df[caracteristic]))

    def get_infos(self,key):
        """Return a dictionnary of {columns:values} of one line

        Keyword Arguments:
        key -- [string or int] the line position

        """
        return(dict(zip(list(self.df),list(self.df.loc[key]))))

    def get_fields(self):
        """Return a list of all the column names of the DataFrame"""
        return(list(self.df))
