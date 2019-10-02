import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATAPATH = str(ROOT.joinpath('data')) + '/'


def load_data(level, file, **kwargs):
    '''Provides a very thin wrapper around pd.read_csv,
    allowing for easier filepath munging to get at
    the data you want'''

    path = DATAPATH + level + '/' + file
    df = pd.read_csv(path, **kwargs)
    return df


def package_data(globals, *args):
    '''Packs an arbitrary number of DataFrames into a `_Data` object,
    provided you pass `globals()` as the first argument.
    '''
    # key: varname, val: variable
    items = [[x for x in globals.items() if x[1] is arg][0] for arg in args]
    
    data = _Data()
    
    for varname, variable in items:
        data.__setattr__(varname, variable)
    
    return data

class _Data(object):    
    '''Simple DataFrame container that prints neat information about
    all of your datasets saved to the object
    '''
    def __repr__(self):
        '''What prints to the terminal when calling object
        '''
        attrs = [x for x in self.__dir__() if not x.startswith('__')]
        cols = [self.__getattribute__(attr).columns for attr in attrs]
        outputDict = dict(zip(attrs, cols))
        return str(outputDict)
