'''Processing taxi ride data'''
import pandas as pd

# Read from Parquet file into Pandas dataframe
df = pd.read_parquet(
    "fhvhv_tripdata_2024-04.parquet",
    engine='pyarrow',
    columns=['request_datetime', 'PULocationID', 'DOLocationID', 'base_passenger_fare',
             'tolls', 'bcf', 'sales_tax', 'congestion_surcharge', 'airport_fee'],
    storage_options=None
)

pd.options.display.show_dimensions = False  # Suppress noisy dimension info

# View only airport dropoffs
print(df.loc[df['DOLocationID'].isin([1, 132, 138])])
