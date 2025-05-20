import pandas as pd
import numpy as np
from helper_funcs import main_selector
import os
import config
pd.set_option('display.max_columns', None)

#%% Read data and understand preliminary details
main_loc = main_selector()

# Need to dynamically change the backslashes in the code between mac
# and windows, or find universal character
data = pd.read_csv(main_loc + os.path.normpath(config.base_data_loc))
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
used_dealer_makeup = data.groupby(['franchise_make', 'make_name']).count()['vin'].reset_index()



economy_group = ['Hyundai', 'Nissan', 'Kia', 'FIAT', 'Mitsubishi', 'Scion', 'Saturn',
                 'Suzuki', 'Isuzu']
mainstream_group = ['Jeep', 'Subaru', 'Mazda', 'Chevrolet', 'Chrysler', 'Dodge', 
                    'Honda', 'Ford', 'Volkswagen', 'RAM', 'Toyota', 'Buick', 'Mercury', 'Pontiac',
                    'smart', ]
premium_group = ['Land Rover', 'Alfa Romeo', 'Acura', 'Lexus', 'Cadillac', 'Lincoln', 'Jauguar',
                 'INFINITI', 'GMC', 'Volvo', 'Saab', 'MINI', 'Genesis', 'Tesla', 'Hummer', 'SRT']
luxury_group = ['BMW', 'Mercedes-Benz', 'Audi', 'Porsche', 'Maserati', 'Fisker', 'Lotus',
                'Karma', 'Ariel']
ultra_luxury = ['Ferrari', 'Bentley', 'Lamborghini', 'Rolls-Royce', 'Spyker', 'McLaren',
                'Aston Martin', 'Maybach', 'Pagani', 'Pininfarina', 'Bugatti', 'Koenigsegg']

variable_remove_list = ['vin', 'bed_height', 'city', 'combine_fuel_economy', 'description', 'engine_type',
               'franchise_make', 'front_legroom', 'fuel_tank_volume', 'highway_fuel_economy',
               'interior_color', 'is_certified']

#%% Create some EDA graphs to explain assumptions being made in the data

#%% Clean data and change data types for inference and better data compression

# Clean categorical variables, determine which need to stay as strings,
# Modify the precision of certain number types for compression
