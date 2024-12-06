import os
import shutil
import pandas as pd
from torch_geometric.data import download_url, extract_zip
from utils import apply_column_mapping
from datetime import date
import re


def remove_all_csv(directory):
    """
    Remove all CSV files in the specified directory.
    
    Args:
        directory (str): The directory path where CSV files are located.
    """
    # List all files in the directory
    files = os.listdir(directory)
        # Iterate through each file and remove CSV files
    for file in files:
        if file.endswith(".csv"):
            os.remove(os.path.join(directory, file))

def remove_csv_files_with_substrings(directory, substrings):
    """
    Remove CSV files from the specified directory if their filenames contain any of the specified substrings.
    
    Args:
        directory (str): The directory path where CSV files are located.
        substrings (list): A list of substrings to search for in filenames.
    """
    files = os.listdir(directory)  # current directory
    
    # Iterate through each file and remove CSV files containing any of the substrings
    for file in files:
        if file.endswith(".csv"):
            for substring in substrings:
                if substring in file:
                    os.remove(os.path.join(directory, file))
                    break  # Exit the inner loop once a substring match is found

def rename_csv_files(directory, name_mappings):
    """
    Rename specific CSV files in the specified directory.
    
    Args:
        directory (str): The directory path where CSV files are located.
        name_mappings (list): A list of tuples where each tuple contains the old and new filenames.
    """
    files = os.listdir(directory)  # List files in the specified directory
    
    # Iterate through each file and rename CSV files
    for file in files:
        if file.endswith(".csv"):
            for old_name, new_name in name_mappings:
                if old_name in file:
                    old_path = os.path.join(directory, file)
                    new_path = os.path.join(directory, file.replace(old_name, new_name))
                    try:
                        os.rename(old_path, new_path)
                    except FileExistsError:
                        print(f"File {new_name} already exists. Skipping renaming...")
                    # print("renamed " + old_name + " to " + new_name)
                    break  # Exit the inner loop once a match is found



def create_directory(file_path: str) -> str:
    base_name = os.path.basename(file_path)
    name_without_extension = os.path.splitext(base_name)[0]
    new_dir_name = "processed_data_" + name_without_extension.replace(" ", "_")
    processed_data_path = os.path.join("data", new_dir_name)
    
    try:
        os.makedirs(processed_data_path, exist_ok=True)
        print("Directory '%s' created" % processed_data_path)
    except FileNotFoundError:
        print("Path doesn't exist. Try going to the sockg directory.")
        exit()

    return processed_data_path



def snake_to_camel(column_name):
    components = column_name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def process_sheet(excel_file, sheet_name, excel_path, directory_path):
    if excel_path.split("/")[-1] == "AgCros.xlsx":
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        df.columns = [snake_to_camel(col) for col in df.columns]
        gracenet = True
    else:
        df = pd.read_excel(excel_file, sheet_name=sheet_name, skiprows=7)
        gracenet = False

    df = df.replace(" ", pd.NA)

    df = apply_column_mapping(df, sheet_name, gracenet=gracenet)
    df = df.drop(columns=[col for col in df.columns if col in [
                 'Unnamed: 0', 'id']], errors='ignore')

    df = df.dropna(axis=0, how='all')

    file_name = f'{sheet_name.lower()}.csv'
    file_path = os.path.join(directory_path, file_name)
    df.to_csv(file_path, index=False)


def run_data_processing(excel_path: str,directory_path: str):
    ### Step 1: read xlsx file and seperate them into raw files
    excel_file = pd.ExcelFile(excel_path)
    

    #if want to remove all csv file in preprocessed data
    # remove_all_csv("./data/processed_data")

    # Iterate through each sheet and save as CSV
    for sheet_name in excel_file.sheet_names:
        process_sheet(excel_file, sheet_name, excel_path, directory_path)

    no_needed_filename = [
        "allcellcomments",
        "autocorrect",
        "det_import",
        "dropdownlists",
        "instructions",
        "mapphotos",
        "methods",
        "projectoverview",
        "tablesoverview",
        "validationdata",
        "valuedomains"
        ]
    remove_csv_files_with_substrings(directory_path,no_needed_filename)


    name_mappings = [
        ("experunits", "experimental_units"),
        ("fieldsites","field_sites"),
        ("measbiomasscho","measurements_biomass_cho"),
        ("measbiomassenergy", "measurements_biomass_energy"),
        ("measbiomassminan","measurements_biomass_mineral_analysis"),
        ("measghgflux","measurements_greenhouse_gases_flux"),
        ("measgrazingplants","measurements_grazing_plants"),
        ("measharvestfraction","measurements_harvest_fraction"),
        ("measresiduemgnt","measurements_residue_management"),
        ("meassoilbiol","measurements_soil_biological"),
        ("meassoilchem","measurements_soil_chemical"),
        ("meassoilcover","measurements_soil_cover"),
        ("meassoilphys","measurements_soil_physical"),
        ("meassuppres","measurements_supporting_research"),
        ("mgtamendments","management_amendments"),
        ("mgtgrazing", "management_grazing"),
        ("mgtgrowthstages","management_growth_stages"), 
        ("mgtplanting","management_planting"),
        ("mgtresidue","management_residue"),
        ("mgttillage","management_tillage"),
        ("weatherdaily","weather_daily"),
        ("weatherstation","weather_station")
    ]

    rename_csv_files(directory_path, name_mappings)

    # mappings for AgCros
    name_mappings = [
        ("metaunits", "experimental_units"),
        ("metasites", "field_sites"),
        ("metatreatments", "treatments"),
        ('metapersons', 'persons'),
        ('metalocationoverview', 'overview'),
        ('metacitations', 'citations'),
        ('measyieldnutuptake', 'measurements_yield_nutrient_uptake'),
        ('measwinderosionarea', 'measurements_wind_erosion_area'),
        ('measwaterqualityarea', 'measurements_water_quality_area'),
        ('measwaterqualityconc', 'measurements_water_quality_concentration'),
        ('measnutreff', 'measurements_nutrient_efficiency'),
        ('measgasnutrientloss', 'measurements_gas_nutrient_loss'),
        ('comometeorology', 'weather_daily')
    ]

    rename_csv_files(directory_path, name_mappings)
    

