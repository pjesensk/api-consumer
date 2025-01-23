import pandas as pd

def print_arr (arr):
    for item in arr:
        print (item)

def print_dict (d):
    for key,value in d.items():
            print (f"{key}: {value}")

def to_json (df, fpath):
        df.to_json(fpath, orient = 'split', compression = 'infer', index = 'true')

def from_json (fpath):
   return pd.read_json(fpath, orient = 'split', compression = 'infer')