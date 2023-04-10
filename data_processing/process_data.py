import pandas as pd
import os

# Print all columns
pd.set_option('display.max_columns', None)

def make_relative_data(category, file_name, treaty):
    # Get all files in data folder
    files = os.listdir('../data/'+ category )
    
    # Get file in files whose name contains file_name
    file = next((f for f in files if file_name in f), None)
    if file is None:
        raise ValueError(f"No file found matching {file_name}")
    
    # Read in file into a dataframe with the first row as the column names
    climate_data = pd.read_csv(f'../data/{category}/{file}', header=1)
    climate_data.columns.values[0] = "Country ID"
    # Make the second column name "Country"
    climate_data.columns.values[1] = "Country"   
    # Read in treaty data
    treaty_data = pd.read_csv('../data/Governance/Governance.csv', usecols=['Country and area', treaty])
    treaty_data = treaty_data.rename(columns={'Country and area': 'Country'})
    
    # Merge climate data with treaty data on Country column
    climate_data = pd.merge(climate_data, treaty_data, on='Country', how='left')
    climate_data = climate_data.rename(columns={treaty: f"Accepted {treaty}"})

    for year in range(1990, 2019):
        # Make column type float
        # Convert values of "..." to NaN
        climate_data[str(year)] = climate_data[str(year)].replace('...', None)
        # Remove commas from values
        climate_data[str(year)] = climate_data[str(year)].str.replace(',', '')
        climate_data[str(year)] = climate_data[str(year)].astype(float)
        
    for year in range(1990, 2018):
        climate_data[f"{year} Percent Change"] = (climate_data[str(year+1)] - climate_data[str(year)]) / climate_data[str(year)] * 100
    return climate_data

make_relative_data("Air and Climate","CO2_Emissions.csv","Paris Agreement")

