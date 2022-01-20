import numpy as np
import pandas as pd

#data_gfw = pd.read_csv('global_fishing_watch/fixed_gear.csv')
#data_gfw_new = pd.read_csv('global_fishing_watch/clean_fixed_gear.csv')

'''
print('Global Fishing Watch')
print(data_gfw.info())
print('Total number of MMSI elements: %d' %data_gfw['mmsi'].size)
print('Total number of non-null MMSI elements: %d' %data_gfw['mmsi'].count())
print('Total number of distinct MMSI elements: %d' %data_gfw['mmsi'].nunique())
print('Distinct elements:')
print(data_gfw.mmsi.value_counts())
print('Distinct elements in Canadian waters:')
print(data_gfw.loc[(data_gfw['lat'] >= 40) & (data_gfw['lat'] <= 67) & (data_gfw['lon'] >= -68) & (data_gfw['lon'] <= -48)].mmsi.value_counts())
print('\n')
print('Fishing activity of MMSI 102111574707951:')
print(data_gfw.loc[data_gfw['mmsi']==102111574707951].is_fishing.value_counts())
print('Fishing activity of MMSI 27932326533321:')
print(data_gfw.loc[data_gfw['mmsi']==27932326533321].is_fishing.value_counts())
print('Fishing activity of MMSI 60628870128017:')
print(data_gfw.loc[data_gfw['mmsi']==60628870128017].is_fishing.value_counts())

#a = data_gfw.loc[(data_gfw['mmsi'] >= 6.062886e+13) & (data_gfw['mmsi'] <= 6.062888e+13)]
#print(a['mmsi'].astype(np.int64))

print('\n')
print('Era5')
print(data_era5.head(10))
print('\n')
print('Global Fishing Watch')
print(data_gfw.loc[(data_gfw['lat'] >= 40) & (data_gfw['lat'] <= 67) & (data_gfw['lon'] >= -68) & (data_gfw['lon'] <= -48)][['timestamp','lat','lon']].head(10))
'''

# data_era5 = pd.read_csv('era5/era5_compiled.csv', nrows=10001)
# print(data_era5[['time','latitude','longitude']].head(10000))

# data_gfw_clean = pd.read_csv('global_fishing_watch/clean_gfw.csv')
# print(data_gfw_clean[['time','latitude','longitude','is_fishing']].head(10))

# #print(data_gfw_clean.is_fishing.value_counts())
# #print(data_gfw_clean.time.value_counts())
# #print(data_gfw_clean.latitude.value_counts())
# #print(data_gfw_clean.longitude.value_counts())

# data_gfw_no_duplicates = data_gfw_clean.drop_duplicates(keep='first', inplace=False, ignore_index=True)
# print(data_gfw_clean.is_fishing.value_counts())
# print(data_gfw_no_duplicates.is_fishing.value_counts())



print(data_gfw.is_fishing.value_counts())
print(data.is_fishing.value_counts())
print(data.info())