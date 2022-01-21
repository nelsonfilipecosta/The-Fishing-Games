#!/bin/bash

echo "Verifying folder 'era5'..."
[[ -d era5 ]] || mkdir era5

echo "Verifying folder 'global_fishing_watch'..."
[[ -d global_fishing_watch ]] || mkdir global_fishing_watch

echo "Verifying folder 'data'..."
[[ -d data ]] || mkdir data

echo "Phase 1 -  Download ERA5 Dataset"
python download_era5.py

mv era5_* era5

echo "Phase 2 -  Convert ERA5 Dataset to CSV"
python convert_era5.py

echo "Phase 3 -  Cleaning Global Fishing Watch Dataset"
python clean_gfw.py

echo "Phase 4 -  Augmenting Global Fishing Watch Dataset with ERA5 Dataset"
python augment_gfw.py