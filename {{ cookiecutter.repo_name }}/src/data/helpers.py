from contextlib import contextmanager
import sys
from pathlib import Path

import pandas as pd


_projectPath = Path(__file__).resolve().parents[2]
_datadir = _projectPath.joinpath('data/')

def handle_io(fn):
    '''
    Create a wrapper to load and save data after transformation

    Parameters
    ----------
    fn: A function that takes a DataFrame and returns a DataFrame
    '''
    with load_save_wrapper() as df:
        print('Process_data')
        
        df = fn(df)

@contextmanager
def load_save_wrapper():
    '''
    Contextmanager that takes in command line arguments to load a file,
    yields the resulting DataFrame, then saves the transformed data as 
    a .csv
    '''
    inputpath, outputpath =  arg_parser()
    print('Loading Data')
    inputPath = _datadir.joinpath(inputpath)
    outputPath = _datadir.joinpath(outputpath)

    df = pd.read_csv(inputPath)
    
    yield df

    df.to_csv(outputPath, index=False) 
    print('Saving Data')
    

def arg_parser(*args):
    '''
    Parses command line arguments to get:
    '''
    inputpath = sys.argv[1]
    outputpath = sys.argv[2]

    return (inputpath, outputpath) 

def keep_cols(df, keepCols):
    '''
    Trims down the columns of your DataFrame, keeping only the
    columns specified in `keepCols`

    Because the wrappers pass the DataFrame by reference, simply selecting
    a subset of data only creates a local copy and will not be saved.
    '''
    for col in df.columns:
        if col not in keepCols:
            del df[col]
