import numpy as np
import pandas as pd
import pathlib

# round timestamps to multiples of 3600 (equivalent of 1h)
def round_time(x):
    return int(3600 * round(x/3600))

# round coordinates to (.00, 0.25, .50, .075) decimal values
def round_coordinates(x):

    aux = round(abs(x) - int(abs(x)), 3)

    if aux < 0.125:
        aux = 0.00
    elif aux >= 0.125 and aux < 0.375:
        aux = 0.25
    elif aux >= 0.375 and aux < 0.625:
        aux = 0.50
    elif aux >= 0.625 and aux < 0.875:
        aux = 0.75
    else:
        aux = 1.00

    if x >= 0:
        return int(x) + aux
    else:
        return int(x) - aux

new_data = []

gear = ['drifting_longlines', 'fixed_gear', 'pole_and_line', 'purse_seines', 'trawlers', 'trollers', 'unknown']

for i in gear:

    print('Cleaning gear %s...' %i)

    data_gfw = pd.read_csv('global_fishing_watch/%s.csv' %i)

    new_data.append(pd.DataFrame({
        'time': data_gfw['timestamp'].apply(lambda x: round_time(x)),
        'latitude': data_gfw['lat'].apply(lambda x: round_coordinates(x)),
        'longitude': data_gfw['lon'].apply(lambda x: round_coordinates(x)),
        'distance_from_shore': data_gfw['distance_from_shore'],
        'distance_from_port': data_gfw['distance_from_port'],
        'is_fishing': data_gfw['is_fishing']
        }))
    
    #filepath = pathlib.Path('global_fishing_watch/clean_%s.csv' %i)
    #new_data.to_csv(filepath)

print('Compiling gear...')

data = pd.concat(new_data)

data = data[data.is_fishing != -1]
data = data[(data.latitude >= 40) & (data.latitude <= 67) & (data.longitude >= -68) & (data.longitude <= -48)]
data.sort_values(['time', 'latitude', 'longitude'], ascending=[True, False, True])

filepath = pathlib.Path('global_fishing_watch/clean_gfw.csv')
data.to_csv(filepath, index=False)

print('Done!')