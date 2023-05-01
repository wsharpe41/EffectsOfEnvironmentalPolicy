import pandas as pd
import os

# Print all columns
pd.set_option('display.max_columns', None)

def make_relative_data(category, file_name,header_row=0,end_year=2017):
    treaties = [
        "Basel Convention",
        "CITES",
        "Convention on Biological Diversity",
        "Convention on Migratory Species",
        "Kyoto \nProtocol",
        "Montreal Protocol",
        "Paris Agreement",
        "Ramsar Convention",
        "Rotterdam Convention",
        "Stockholm Convention",
        "UN Convention on the Law of the Sea",
        "UN Convention to Combat Desertification",
        "UN Framework Convention on Climate Change",
        "World \nHeritage Convention"
    ]

    # Get all files in data folder
    files = os.listdir('../data/'+ category )
    
    # Get file in files whose name contains file_name
    file = next((f for f in files if file_name in f), None)
    if file is None:
        raise ValueError(f"No file found matching {file_name}")

    # Read in file into a dataframe with the first row as the column names
    climate_data = pd.read_csv(f'../data/{category}/{file}', header=header_row)
    climate_data.columns.values[0] = "Country ID"
    # Make the second column name "Country"
    climate_data.columns.values[1] = "Country"   
    # Read in treaty data
    # With Country and area and all treaties in treaties
    treaty_data = pd.read_csv('../data/Governance/Governance.csv', usecols=['Country and area'] + treaties)
    treaty_data = treaty_data.rename(columns={'Country and area': 'Country','Kyoto \nProtocol': 'Kyoto Protocol','World \nHeritage Convention': 'World Heritage Convention'})
    # Merge climate data with treaty data on Country column
    climate_data = pd.merge(climate_data, treaty_data, on='Country', how='left')

    for year in range(2000, end_year+1):
        # Make column type float
        # Convert values of "..." to NaN
        climate_data[str(year)] = climate_data[str(year)].replace('...', None)
        climate_data[str(year)] = climate_data[str(year)].replace('…', None)
        # Remove commas from values
        climate_data[str(year)] = climate_data[str(year)].str.replace(',', '')
        climate_data[str(year)] = climate_data[str(year)].astype(float)
        

    # ADD INTERPOLATION HERE
    for year in range(2000, end_year):
        climate_data[f"{year} Percent Change"] = (climate_data[str(year+1)] - climate_data[str(year)]) / climate_data[str(year)] * 100
    
    # Write to csv
    climate_data.to_csv(f'../data/{category}/{file_name[:-4]}_processed.csv', index=False)   
    return climate_data


# This should work for Air and Climate, some Energy and Minerals, water
def process_folder(folder_name,header_row=0,end_year=2017):
    files = os.listdir('../data/'+ folder_name)
    if folder_name!="Air and Climate":
        header_row = 0
    if folder_name == "Inland Water Resources":
        end_year = 2017
    print(files)
    for file in files:
        print(file)
        if ".csv" in file:
            if "Freshwater abstracted as proportion of renewable freshwater resources" in file:
                continue
            if "Water resources.csv" in file:
                continue
            if "_processed" in file:
                continue
            if "Wastewater generation and treatment.csv" in file:
                continue
            if "Public Water Supply.csv" in file:
                continue
            make_relative_data(folder_name,file,header_row,end_year)

#process_folder("Air and Climate")
process_folder("Inland Water Resources")