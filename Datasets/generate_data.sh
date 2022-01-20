#!/bin/sh

python download_era5.py
python convert_era5.py
python clean_gfw.py
python augment_gfw_era5.py