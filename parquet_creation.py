import polars as pl
import pandas as pd
import numpy as np


#%% Read data and understand preliminary details

data = pl.read_csv(r'C:\Users\Alexander\OneDrive\Documents\Career Files\Data Science Career Notes (I did it!)\Data Science Projects\Used Car Dataset\used_cars_data\used_cars_data.csv',
                   infer_schema_length=None)

data.describe
data.columns
data.dtypes
# Check count of columns in data type group
dtyplist = pl.DataFrame(data.dtypes)
dtyplist.group_by('column_0').count()
#%% Clean data and change data types for inference and better data compression

