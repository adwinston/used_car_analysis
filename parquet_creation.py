import polars as pl
import pandas as pd
import numpy as np
from config import main

#%% Read data and understand preliminary details

data = pl.read_csv(rf'{main}\data\used_cars_data.csv',
                   infer_schema_length=None)

data.describe
data.columns
data.dtypes
# Check count of columns in data type group
dtyplist = pl.DataFrame(data.dtypes)
dtyplist.group_by('column_0').count()
#%% Clean data and change data types for inference and better data compression

# Clean categorical variables, determine which need to stay as strings,
# Modify the precision of certain number types for compression