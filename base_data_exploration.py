import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import plotly.express as px
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


economy_group = ['Hyundai', 'Nissan', 'Kia', 'FIAT', 'Mitsubishi', 'Scion', 'Saturn',
                 'Suzuki', 'Isuzu']
mainstream_group = ['Jeep', 'Subaru', 'Mazda', 'Chevrolet', 'Chrysler', 'Dodge', 
                    'Honda', 'Ford', 'Volkswagen', 'RAM', 'Toyota', 'Buick', 'Mercury', 'Pontiac',
                    'smart', ]
premium_group = ['Land Rover', 'Alfa Romeo', 'Acura', 'Lexus', 'Cadillac', 'Lincoln', 'Jaguar',
                 'INFINITI', 'GMC', 'Volvo', 'Saab', 'MINI', 'Genesis', 'Tesla', 'Hummer', 'SRT']
luxury_group = ['BMW', 'Mercedes-Benz', 'Audi', 'Porsche', 'Maserati', 'Fisker', 'Lotus',
                'Karma', 'Ariel']
ultra_luxury = ['Ferrari', 'Bentley', 'Lamborghini', 'Rolls-Royce', 'Spyker', 'McLaren',
                'Aston Martin', 'Maybach', 'Pagani', 'Pininfarina', 'Bugatti', 'Koenigsegg']

conditions = [data['make_name'].isin(economy_group), data['make_name'].isin(mainstream_group),
              data['make_name'].isin(premium_group), data['make_name'].isin(luxury_group),
              data['make_name'].isin(ultra_luxury)]
choices = ['economy', 'mainstream', 'premium', 'luxury', 'ultra_luxury']

data['group'] = np.select(conditions, choices, default='NA')
data = data[data['group'] != 'NA']
used_dealer_makeup = data.groupby(by=['franchise_make', 'group']).count()['vin'].reset_index()
franchise_car_count = used_dealer_makeup.groupby(by=['franchise_make'])['vin'].sum()
used_dealer_makeup= used_dealer_makeup.merge(right=franchise_car_count, left_on=['franchise_make'], right_on='franchise_make')
used_dealer_makeup.rename(mapper={'vin_x' : 'vehicle_count', 'vin_y' : 'total_franchise_vehicle_count'},
                          axis=1, inplace=True)
#%% Create some EDA graphs to explain assumptions being made in the data

Plotly graph of fuel economy and horsepower

graph or table breaking down relationship between dealer and the vehicles classes they are selling
# Do a stacked bar chart for the top 10 franchises by used car count


basic boxplot showing distribution of car price with color
