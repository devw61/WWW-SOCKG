import pandas as pd
from constants import column2property, property2columnGRACENET
import shutil
import traceback
import os

def adhoc_load_csv(path: str = None) -> None:
    df = pd.read_csv(path)
    print(df.head())
    df = df[['fieldId', 'weatherDate', 'weatherStationId', 'maxDegC', 'minDegC']]
    df.to_csv('./dataset/weather.csv', index=False)
    return df

def separate_raw_data(path: str = None) -> None:
    df = pd.read_csv(path)
    print(df.head())
    df = df[['fieldId', 'weatherDate', 'weatherStationId', 'maxDegC', 'minDegC']]
    df.to_csv('./dataset/weather.csv', index=False)
    return df


def apply_column_mapping(input_df: pd.DataFrame, sheet_name: str, gracenet: bool = False) -> pd.DataFrame:
    mapping_function = property2columnGRACENET if gracenet else column2property

    rename_dict = {column: mapping_function(
        column, sheet_name) for column in input_df.columns if mapping_function(column, sheet_name) is not None}

    input_df.rename(columns=rename_dict, inplace=True)

    return input_df


def move_column(input_csv: str, output_csv: str, column_to_move: str, compared_column_input_df: str, compared_column_output_df: str):
    try:
        output_df = pd.read_csv(output_csv, low_memory=False)
        input_df = pd.read_csv(input_csv, low_memory=False)

        merged_df = output_df.merge(
            input_df[[compared_column_input_df, column_to_move]],
            left_on=compared_column_output_df,
            right_on=compared_column_input_df,
            how='left',
            suffixes=('_output', '_input')
        )

        merged_df = merged_df.drop_duplicates()

        merged_df.to_csv(output_csv, index=False)
    except Exception as e:
        print(f'error moving columns: {e}')
        # tb = traceback.format_exc()
        # print(f"\n{tb}")


def concat_cols(columns_to_concat: list, directory_path: str):
    try:
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.csv'):
                csv_file_path = os.path.join(directory_path, file_name)
                df = pd.read_csv(csv_file_path, low_memory=False)

                if all(col in df.columns for col in columns_to_concat):
                    # Concatenate specified columns with 'AgCros_' prefix
                    df[columns_to_concat[1]] = df[columns_to_concat].astype(
                        str).agg('_'.join, axis=1).apply(lambda x: f"AgCros_{x}")

                    # Save the updated DataFrame back to the CSV file
                    df.to_csv(csv_file_path, index=False)
    except Exception as e:
        print(f'error moving columns: {e}')
        # tb = traceback.format_exc()
        # print(f"\n{tb}")


def delete_directory(directory_path: str) -> None:
    """
    Delete a directory and its contents
    """
    try:
        shutil.rmtree(directory_path)
    except OSError as e:
        print(f"Error deleting directory: {directory_path} : {e.strerror}")

def update_mgtplanting(directory_path, file_name):
    try:
        move_column(directory_path+file_name,directory_path+'/management_planting_with_UID.csv',
                    'expUnitId', 'fieldId', 'fieldId')
        move_column(directory_path+file_name,directory_path+'/management_planting_with_UID.csv',
                    'crop', 'expUnitId', 'expUnitId')
    except Exception as e:
        print(f'error moving columns: {e}')
        tb = traceback.format_exc()
        print(f"\n{tb}")


def change_value(df,old_value: str,new_value:str, column_name: str):
    try:
        df[column_name] = df[column_name].replace({old_value: new_value})
        return df
    except Exception as e:
        print(f'error fixing value name: {e}')
        tb = traceback.format_exc()
        print(f"\n{tb}")

def run_utils(directory_path):
    # onto = parse_ontology('ontology.ttl')
    # print(onto.serialize(format='turtle').decode('utf-8'))

    # csv = adhoc_load_csv('./dataset/soil_carbon_weather.csv')

    # moving columns so that they are in the right place for mappings in server.py

    try:
        print('moving siteId')
        move_column(directory_path+'/field_sites.csv',directory_path+'/overview.csv','siteId', 'fieldId', 'fieldId')
        move_column(directory_path+'/field_sites.csv',directory_path+'/citations.csv','siteId', 'fieldId', 'fieldId')
        move_column(directory_path+'/field_sites.csv',directory_path+'/persons_with_UID.csv','siteId', 'fieldId', 'fieldId')

        print('moving siteIdDescriptor')
        move_column(directory_path+'/overview.csv',directory_path+'/field_sites.csv','siteIdDescriptor', 'siteId', 'siteId')

        print('moving experimentName')
        move_column(directory_path+'/overview.csv', directory_path+'/treatments.csv','experimentName', 'fieldId', 'fieldId')
        
        print('moving plantFractionCrudeProteinStd_g_per_kg')
        move_column(directory_path+'/measurements_biomass_cho_with_UID.csv',
                    directory_path+'/measurements_harvest_fraction_with_UID.csv','crudeProteinSd_g_per_kg',
                    'expUnitId', 'expUnitId')
        
        
        print('moving weather properties')
        move_column(directory_path+'/field_sites.csv',directory_path+'/weather_daily_with_UID.csv',
                    'elevation_m', 'fieldId', 'fieldId')
        move_column(directory_path+'/field_sites.csv',directory_path+'/weather_daily_with_UID.csv',
                    'longitude_decimal_deg', 'fieldId', 'fieldId')
        move_column(directory_path+'/field_sites.csv',directory_path+'/weather_daily_with_UID.csv',
                    'latitude_decimal_deg', 'fieldId', 'fieldId')
        move_column(directory_path+'/field_sites.csv',directory_path+'/weather_daily_with_UID.csv',
                    'siteId', 'fieldId', 'fieldId')
        
        # print("updating mgtplanting")
        # for file in os.listdir(directory_path):
        #     if file.startswith('measurements'):
        #         update_mgtplanting(directory_path, '/'+file)

        if directory_path != 'data/processed_data_AgCros':
            print('Formatting...')
            concat_cols(['fieldId', 'expUnitId'], directory_path)
            concat_cols(['fieldId', 'treatmentId'], directory_path)

    except Exception as e:
        print(f'error moving columns(utils): {e}')
        # tb = traceback.format_exc()
        # print(f"\n{tb}")
