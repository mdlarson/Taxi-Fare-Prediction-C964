'''
Extracts ID and borough from list of NYC Taxi Zones.

This script reads an input CSV file, extracts the columns of interest, and writes them to an output CSV file.
It handles large field sizes by increasing the CSV field size limit.

Columns of Interest:
    - OBJECTID
    - borough

Example:
    If the input CSV file contains the following data:
    ```
    OBJECTID,Shape_Leng,the_geom,Shape_Area,zone,LocationID,borough
    1,0.116357453189,"MULTIPOLYGON (((-74.18445299999996 40.694995999999904, -74.18448899999999 40.69509499999987)))",0.0007823067885,Newark Airport,1,EWR
    2,0.43346966679,"MULTIPOLYGON (((-73.82337597260663 40.63898704717672, -73.82277105438692 40.63557691408512, -73.82265046764824 40.63536884414309, -73.82253791037438 40.6351581797112)))",0.00486634037837,Jamaica Bay,2,Queens
    ```

    The output CSV file will contain:
    ```
    OBJECTID,borough
    1,EWR
    2,Queens
    ```
'''

import csv
import sys

# Increase the field size limit
csv.field_size_limit(sys.maxsize)

# We need to know which Taxi Zones belong to each borough.
# ---
# Taxi Zone data source: https://data.cityofnewyork.us/Transportation/NYC-Taxi-Zones/d3c5-ddgc
# Title: "NYC Taxi Zones"
# Dataset URL: https://data.cityofnewyork.us/api/views/755u-8jsi/rows.csv?accessType=DOWNLOAD
# ---

# File paths
input_file = 'taxi_zones.csv'
output_file = 'taxi_boroughs.csv'

# Define relevant columns
columns_of_interest = ['OBJECTID', 'borough']

# Read input, select columns, write to output
with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
        open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=columns_of_interest)

    # Write header to output
    writer.writeheader()

    # Process rows
    for row in reader:
        filtered_row = {field: row[field] for field in columns_of_interest}
        writer.writerow(filtered_row)
