import numpy as np
import pandas as pd
import sys


class CSV_writer:
    """CSV file data writer

    Allow to write and modify csv files without considering the
    technology used to do it (here pandas).
    """

    def __init__(self, file_name=None):
        """Constructor of CSV_reader class

        file_name -- [string] name of the file to read which contains the datas
        
        """
        if file_name:
            self.df = pd.read_csv(sys.path[0] + "/" + file_name, index_col=0)
            # think about the case that csv doesn't exist
        else:
            self.df = pd.DataFrame()

        self.nb_index = self.df.shape[0]
        self.file_name = file_name

    def set(self, key, feature, value):
        """Update one value of the DataFrame

        Keyword Arguments:
        key -- [string or int] the line position
        feature -- [string] the column position
        value -- [any] the value to put in

        """
        self.df.at[key, feature] = value

    def set_list(self, feature, list):
        """Update one column of the DataFrame

        Keyword Arguments:
        feature -- [string] the column position
        list -- [list] the values to put in

        """
        self.df[feature] = pd.DataFrame(list)

    def set_infos(self, key, info):
        """Update one line of the DataFrame

        Keyword Arguments:
        key -- [string or int] the line position
        info -- [any] the value to put in

        """
        info = pd.DataFrame(info)  # change to add key in the df
        self.df.update(info)

    def add(self, row_dict):
        """Add an other dataframe to the existing one

        Keyword Arguments:
        other -- [pd.DataFrame] the df to add

        """
        #line = pd.DataFrame(row_dict)
        self.df.append(row_dict, ignore_index=True)
        print(self.df)

    def write(self, file=None, w_mode='w'):
        """Write the DataFrame in a csv, if file is not given, write in self.file_name

        file -- [string] file to write the DataFrame on (default : None)
        w_mode -- [char] python writing mode (default : 'w', ie "write")

        """
        if file:
            target = file
        else:
            target = self.file_name

        self.df.to_csv(sys.path[0] + "/" + target, mode=w_mode)

    def clear_df(self):
        """Replace the df by a new empty DataFrame

        Return the old df

        """
        old_df = self.df
        self.df = pd.DataFrame()
        return old_df

    @property
    def txt_to_pandas(file_name):
        """Return DataFrame from a formated .txt file

        file_name -- [string] formated .txt file to read

        """
        file = open(file_name, 'r')
        names, items = [], []
        for item in file.readlines():
            item = item.split(" ")
            names.append(item[0])
            items.append(int(item[1]))
        df = pd.DataFrame(index=names, columns=['pins'])
        return df
