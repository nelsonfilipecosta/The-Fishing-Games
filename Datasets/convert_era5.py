import numpy as np
import pandas as pd
import netCDF4 as nc
import pathlib

new_data = []

years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

for i in years:

    print('Converting year %s...' %i)
    
    data = nc.Dataset('era5/era5_%s.nc' %i)

    time_dim = len(data.dimensions['time'])
    lat_dim = len(data.dimensions['latitude'])
    lon_dim = len(data.dimensions['longitude'])

    time = nc.num2date(data.variables['time'][:], data.variables['time'].units).astype('datetime64[s]').astype('int')   # convert netCDF4 time to Unix timestamp
    lat = data.variables['latitude'][:]
    lon = data.variables['longitude'][:]

    time_grid, lat_grid, lon_grid = [x.flatten() for x in np.meshgrid(time, lat, lon, indexing='ij')]

    u10 = data.variables['u10'][:].flatten()        # 10m_u_component_of_wind
    v10 = data.variables['v10'][:].flatten()        # 10m_v_component_of_wind
    hmax = data.variables['hmax'][:].flatten()      # maximum_individual_wave_height
    mwp =  data.variables['mwp'][:].flatten()       # mean_wave_period
    pp1d = data.variables['pp1d'][:].flatten()      # peak_wave_period
    tmax = data.variables['tmax'][:].flatten()      # period_corresponding_to_maximum_individual_wave_height
    swh = data.variables['swh'][:].flatten()        # significant_height_of_combined_wind_waves_and_swell

    new_data.append(pd.DataFrame({
        'time': time_grid,
        'latitude': lat_grid,
        'longitude': lon_grid,
        '10m_u_component_of_wind': u10,
        '10m_v_component_of_wind': u10,
        'mean_wave_period': mwp,
        'peak_wave_period': pp1d,
        'maximum_individual_wave_height': hmax,
        'period_corresponding_to_maximum_individual_wave_height': tmax,
        'significant_height_of_combined_wind_waves_and_swell': swh
        }))
    
    #filepath = pathlib.Path('era5/era5_%s.csv' %i)
    #new_data.to_csv(filepath)

    print('Done!')

print('Compiling years...')

data = pd.concat(new_data)

filepath = pathlib.Path('era5/era5_compiled.csv')
data.to_csv(filepath, index=False)

print('Done!')