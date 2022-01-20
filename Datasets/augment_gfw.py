import numpy as np
import pandas as pd
import pathlib

new_data = []

print('Reading GFW file...')
data_gfw = pd.read_csv('global_fishing_watch/clean_gfw.csv')

print('Reading ERA5 file...')
data_era5 = pd.read_csv('era5/era5_compiled.csv')

n_rows = data_era5.shape[0]     # number of rows in ERA5 dataset
n_partitions = 100              # number of partitions of ERA5 dataset

n = int(n_rows/n_partitions) + 1

print('Merging datasets... (0/%s)' %n_partitions)

data_era5 = pd.read_csv('era5/era5_compiled.csv', nrows=n)
merged_data = pd.merge(data_gfw, data_era5,  how='inner', on=['time', 'latitude', 'longitude'])
new_data.append(merged_data)

# break ERA5 dataset in smaller partitions for RAM management
for i in range(1, n_partitions):
    print('Merging datasets... (%s/%s)' %(i, n_partitions))
    
    data_era5 = pd.read_csv('era5/era5_compiled.csv', skiprows=range(1, i*n), nrows=n)
    merged_data = pd.merge(data_gfw, data_era5,  how='inner', on=['time', 'latitude', 'longitude'])
    new_data.append(merged_data)

print('Compiling datasets...')

data = pd.concat(new_data)

# reorder dataset columns
data = data[['time',
             'latitude',
             'longitude',
             'distance_from_shore',
             'distance_from_port',
             '10m_u_component_of_wind',
             '10m_v_component_of_wind',
             'mean_wave_period',
             'peak_wave_period',
             'maximum_individual_wave_height',
             'period_corresponding_to_maximum_individual_wave_height',
             'significant_height_of_combined_wind_waves_and_swell',
             'is_fishing']]

filepath = pathlib.Path('augmented_data/augmented_data.csv')
data.to_csv(filepath, index=False)

print('Done!')