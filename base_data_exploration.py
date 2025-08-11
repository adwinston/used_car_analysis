import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
from helper_funcs import main_selector
import os
import config

pd.set_option('display.max_columns', None)
pio.renderers.default = 'plotly_mimetype+notebook'

#%% Read data and understand preliminary details
main_loc = main_selector()

data = pd.read_csv(main_loc + os.path.normpath(config.base_data_loc))
data.describe
data.columns
data.dtypes

#%% Brand groupings for ease of data exploration
economy_group = ['Hyundai', 'Nissan', 'Kia', 'FIAT', 'Mitsubishi', 'Scion', 'Saturn',
                 'Suzuki', 'Isuzu']

mainstream_group = ['Jeep', 'Subaru', 'Mazda', 'Chevrolet', 'Chrysler', 'Dodge', 
                    'Honda', 'Ford', 'Volkswagen', 'RAM', 'Toyota', 'Buick', 'Mercury', 'Pontiac',
                    'smart']

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

#%% Analyze relationships between franchise makes and make of cars being sold
used_dealer_makeup = data.groupby(by=['franchise_make', 'group']).count()['vin'].reset_index()
franchise_car_count = used_dealer_makeup.groupby(by=['franchise_make'])['vin'].sum()
top_10_vol_franchise = franchise_car_count.sort_values(ascending=False).iloc[:10]
top_11_20_vol_franchise = franchise_car_count.sort_values(ascending=False).iloc[11:21]

# Stacked bar charts of different make groups by franchise selling the vehicles
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

# Array of make to make scaled by 10,000 after filtering for minimum
array_of_franchise_make = data.groupby(by=['franchise_make', 'make_name'], as_index=True)['vin'].count().reset_index()
array_of_franchise_make = array_of_franchise_make[array_of_franchise_make['vin'] >= 1000]
array_of_franchise_make['vin'] = array_of_franchise_make['vin'] / 10000
array_of_franchise_make = array_of_franchise_make.pivot(index='franchise_make', columns='make_name', values='vin').fillna(0).reset_index().rename_axis(None, axis=1).set_index('franchise_make')
ax = plt.figure(figsize=(20,20))
sns.heatmap(array_of_franchise_make, annot=True)

# Array of make to make log scaled after filtering for minimum
array_of_franchise_make_2 = data.groupby(by=['franchise_make', 'make_name'], as_index=True)['vin'].count().reset_index()
array_of_franchise_make_2 = array_of_franchise_make_2[array_of_franchise_make_2['vin'] >= 1000]
array_of_franchise_make_2 = array_of_franchise_make_2.assign(vin = np.log(array_of_franchise_make_2['vin']))
array_of_franchise_make_2 = array_of_franchise_make_2.pivot(index='franchise_make', columns='make_name', values='vin').fillna(0).reset_index().rename_axis(None, axis=1).set_index('franchise_make')

ax = plt.figure(figsize=(20,20))
sns.heatmap(array_of_franchise_make_2, annot=True)
#%% Create some EDA graphs to explain assumptions being made in the data

#Plotly graph of fuel economy and horsepower
sample_frame = data.sample(100)
fig = px.scatter(data_frame=sample_frame, x='horsepower', y='highway_fuel_economy', opacity=0.8,
                 hover_data=['make_name', 'model_name', 'engine_type'])
fig.show()

#%% basic boxplot showing distribution of car price with color
data[data['price'] <= 500000].groupby(by=['listing_color']).agg({'price' : ['mean', 'median']})
ax = plt.figure(figsize=(20,10))
sns.boxplot(data=data[data['price'] <= 500000], x='listing_color', y='price')

# Run an ANOVA test
# Can I prove that they means are statistically different? Then the question becomes, but why? The causal part.
# Make a couple visuals that show some confounding going on with potential car color
# Can make focus on car year and then loop in some research from the internet on how
# car colors have trended over time. That way I can create the link between real world
# shifts that intefere with the valuation of car colors. Are they different because the
# brown cars are older on average or because of the color brown itself?