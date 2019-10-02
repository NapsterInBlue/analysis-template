'''
This file represents the general design pattern for pipelining
data transformations.

Save a renamed copy at this location in this directory to leverage
it for simple reuse, called from your makefile at root
'''

from helpers import handle_io, keep_cols


def process_data(df):
    return df


if __name__ == '__main__':
    df = handle_io(process_data)
