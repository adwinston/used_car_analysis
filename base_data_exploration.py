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

#%%
used_dealer_makeup = data.groupby(by=['franchise_make', 'group']).count()['vin'].reset_index()
franchise_car_count = used_dealer_makeup.groupby(by=['franchise_make'])['vin'].sum()
top_10_vol_franchise = franchise_car_count.sort_values(ascending=False).iloc[:10]
top_11_20_vol_franchise = franchise_car_count.sort_values(ascending=False).iloc[11:21]


pivoted_data = used_dealer_makeup.pivot_table(values='vin', index='franchise_make', aggfunc=np.sum, columns='group')
pivoted_data = pivoted_data.reset_index().rename_axis(None, axis=1).set_index('franchise_make')
pivoted_data['total_count'] = np.sum(pivoted_data, axis=1)
pivoted_data.sort_values(by='total_count', axis=0, ascending=False, inplace=True)
pivoted_data.drop(columns=['total_count'], inplace=True)

# Top 10 franchise graph
pivoted_data[pivoted_data.index.isin(top_10_vol_franchise.index)].plot(kind='bar', stacked=True)

# Top 11-20 franchise graph
pivoted_data[pivoted_data.index.isin(top_11_20_vol_franchise.index)].plot(kind='bar', stacked=True)

# All franchise graph
pivoted_data.plot(kind='bar', stacked=True)
#%% Create some EDA graphs to explain assumptions being made in the data

Plotly graph of fuel economy and horsepower

graph or table breaking down relationship between dealer and the vehicles classes they are selling
# Do a stacked bar chart for the top 10 franchises by used car count
# %%


basic boxplot showing distribution of car price with color
