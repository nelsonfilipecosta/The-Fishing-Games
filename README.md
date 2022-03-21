# The-Fishing-Games

!!! UNFINISHED PROJECT !!!

## Datasets

Code used to download and convert from netCDF4 to CSV the following hourly weather variables

- time
- latitude
- longitude
- 10m_u_component_of_wind
- 10m_v_component_of_wind
- maximum_individual_wave_height
- mean_wave_period
- peak_wave_period
- period_corresponding_to_maximum_individual_wave_height
- significant_height_of_combined_wind_waves_and_swell

from the [ERA5](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview) dataset between the years 2012 and 2019, as well as the whole anonymized AIS training data from the [Global Fishing Watch](https://globalfishingwatch.org/data-download/datasets/public-training-data-v1) dataset between the same period of time.

Both datasets are then cleaned and merged based on time, latitude and longitude to create a final augmented dataset on which to train machine learning models to predict fishing activity patterns based on weather information.

### Dataset Schema

- time
- latitude
- longitude
- distance_from_shore
- distance_from_port
- 10m_u_component_of_wind
- 10m_v_component_of_wind
- mean_wave_period
- peak_wave_period
- maximum_individual_wave_height
- period_corresponding_to_maximum_individual_wave_height
- significant_height_of_combined_wind_waves_and_swell
- is_fishing

### Code

Simply run the following command 

```
./generate_data.sh
```

to run the whole process.
