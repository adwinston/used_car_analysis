import pandas as pd
import numpy as np
from helper_funcs import main_selector

pd.set_option('display.max_columns', None)

#%% Read data and understand preliminary details
main_loc = main_selector()

data = pd.read_csv(rf'{main_loc}\data\used_cars_data.csv')

data.describe
data.columns
data.dtypes
unique_vals = data.nunique()
unique_vals[:25]
unique_vals[25:50]
unique_vals[50:]
data.isna().sum()
data.iloc[:, :10].head(10)

#%% Remove uncessary features for prediction and causal inference, this will help reduce file size and complexity

remove_list = ['vin', '']

#%% Clean data and change data types for inference and better data compression

# Clean categorical variables, determine which need to stay as strings,
# Modify the precision of certain number types for compression``