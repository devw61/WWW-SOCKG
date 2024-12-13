import pandas as pd
import os
import random
import string
import traceback

def create_new_unique_id(input_csv_path, output_csv_path, columns_to_concat, new_id_name: str):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_csv_path)
        # Get the .csv filename without the .csv at the end 
        input_filename = os.path.splitext(os.path.basename(input_csv_path))[0] 

        # Concatenate specified columns and add as a new column using ',' as separator
        concatenated_column = df.get(columns_to_concat).astype(str).apply(','.join, axis=1)

        if df.shape[0] == 0 and df.shape[1] > 0:
            # Create unique identifier in this case with csv file
            df_new = pd.DataFrame({new_id_name: ["Empty"]})
            # Concatenate the new DataFrame with the original DataFrame
            df = pd.concat([df, df_new], ignore_index=True)
            df[new_id_name] = ""
        else:
            df[new_id_name] = concatenated_column 
            # Replace special characters and spaces in the new ID with underscores
            df[new_id_name] = df[new_id_name].str.replace('[^a-zA-Z0-9\.-]+', '_', regex=True) + "_" + input_filename

        # Write the modified data to a new CSV file
        df.to_csv(output_csv_path, index=False)
    except Exception as e:
        # tb = traceback.format_exc()
        # print(f"Error in give_unique_id:\n{tb}")
        print(f"Error in give_unique_id:\n{input_csv_path.split('/')[-1]}:{e}")


def generate_unique_id(df, columns_to_concat, siteID, input_filename, add_filename_to_id):
    concatenated_columns = df.get(columns_to_concat).astype(str).apply(','.join, axis=1).dropna()
    if add_filename_to_id:
        unique_id = siteID + "_" + concatenated_columns + "_" + input_filename
    else:
        unique_id = siteID + "_" + concatenated_columns
    return unique_id.str.replace('[^a-zA-Z0-9\.-]+', '_', regex=True)


def process_dataframe(input_csv_path, output_csv_path, columns_to_concat, new_id_name, siteID, second_ID_name=None, second_column_values=None, add_filename_to_id=False):
    try:
        # Read the CSV file
        df = pd.read_csv(input_csv_path, low_memory=False)
        
        # Get the .csv filename without the .csv at the end
        input_filename = os.path.splitext(os.path.basename(input_csv_path))[0]

        if df.empty:
            # If DataFrame is empty, create the column with empty values
            df[new_id_name] = ""
            if second_ID_name is not None:
                df[second_ID_name] = ""
        else:
            # Generate new IDs
            df[new_id_name] = generate_unique_id(df, columns_to_concat, siteID, input_filename, add_filename_to_id)
            
            if second_ID_name is not None and second_column_values is not None:
                df[second_ID_name] = generate_unique_id(df, second_column_values, siteID, input_filename, add_filename_to_id)

        # Save the DataFrame to a new CSV file
        df.to_csv(output_csv_path, index=False)
    except Exception as e:
        print(f"Error in give_unique_id[{input_csv_path.split('/')[-1]}:{e}]")
        
# Example usage:
# create_new_unique_id("input.csv", "output.csv", ["column1", "column2"], "new_id")


def create_random_unique_ID(input_file, column_name, output_file):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_file)
        
        # Generate unique random strings
        random_strings = []
        existing_strings = set(df[column_name].values.tolist()) if column_name in df else set()
        
        while len(random_strings) < len(df):
            random_string = ''.join(random.choices(string.digits, k=3)) + '-' + ''.join(random.choices(string.digits, k=3)) + '-' + ''.join(random.choices(string.ascii_letters, k=3))
            if random_string not in existing_strings:
                random_strings.append(random_string)
                existing_strings.add(random_string)
        
        # Add the new column to the DataFrame
        df[column_name] = random_strings
        
        # Save the DataFrame to a new CSV file
        df.to_csv(output_file, index=False)
    except Exception as e:
        # tb = traceback.format_exc()
        # print(f"Error in give_unique_id:\n{tb}")
        print(f"Error in give_unique_id:\n{e}")

def run_give_unique_id(directory_path):
    #This is using csv file after the raw file which the tab name is already renamed
    siteIDs = directory_path.split("/")[-1].split("_")
    for ID in siteIDs:
        if ID[0:2] == "NE" or ID == "AgCros":
             siteID = ID

    #Overview
    #Seperated into multiple classes


    #FieldSites
    # UID: fieldId
    # Already have unique ID


    #Persons
    # UID: persons_firstName_lastName_middleName_suffix
    Persons_file_path = f'{directory_path}/persons.csv'
    Persons_columns_to_concat = ["firstName", "lastName", "middleName", "suffix"]
    create_new_unique_id(Persons_file_path, f"{directory_path}/persons_with_UID.csv",Persons_columns_to_concat, "persons_UID")



    #Citations 
    # UID:publicationIdentifier
    # Already have unique ID


    #Treatments
    # UID: treatmentId
    # Already have unique ID


    #ExperUnits
    # UID: expUnitId
    # some info are store in field site structure
    ExperUnits_file_path = f'{directory_path}/experimental_units.csv'
    ExperUnits_columns_to_concate = ["expUnitId"]
    process_dataframe(ExperUnits_file_path, f"{directory_path}/experimental_units_with_UID.csv",
                      ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)


    #MapPhotos not used

    #Methods not used

    #WeatherStation
    # UID: weatherStationId
    # Already have unique ID


    #WeatherDaily
    # UID: weatherObservationDate
    # Valid UID since weather station is bonded by a relationship and Weather is measured onece per day
    weatherDaily_file_path = f'{directory_path}/weather_daily.csv'
    weatherDaily_columns_to_concate = ["fieldId", "date",]
    process_dataframe(weatherDaily_file_path, f"{directory_path}/weather_daily_with_UID.csv",
                                     weatherDaily_columns_to_concate, "weatherDaily_UID", siteID, add_filename_to_id=False)

    #MgtAmendments
    # UID: management_amendments_siteID_ExpUnitID_date_crop
    MgtAmendments_file_path = f'{directory_path}/management_amendments.csv'
    MgtAmendments_columns_to_concate = ["expUnitId", "startDate", "crop"]
    Pesticide_columns_to_concate = ["totalPesticideAmount_kg_per_ha","pesticideActiveIngredientType", "pesticideTarget", "pesticidePlacement"]
    process_dataframe(MgtAmendments_file_path, f"{directory_path}/management_amendments_with_UID.csv", 
                                     MgtAmendments_columns_to_concate, "mgtAmendments_UID", siteID, "pesticide_UID", 
                                     Pesticide_columns_to_concate)
    process_dataframe(f"{directory_path}/management_amendments_with_UID.csv", 
                                     f"{directory_path}/management_amendments_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)
    #Pesticide UID: totalPesticideAmount_pesticideActiveIngredientType_pesticideTarget_pesticidePlacement



    #MgtPlanting
    # UID: management_planting_siteID_ExpUnitID_Date_crop
    MgtPlanting_file_path = f'{directory_path}/management_planting.csv'
    MgtPlanting_columns_to_concate = ["expUnitId", "startDate", "crop"]
    process_dataframe(MgtPlanting_file_path, f"{directory_path}/management_planting_with_UID.csv", 
                                     MgtPlanting_columns_to_concate, "mgtPlanting_UID",siteID)
    process_dataframe(f"{directory_path}/management_planting_with_UID.csv", 
                                     f"{directory_path}/management_planting_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID",siteID, add_filename_to_id=False)

    #MgtTillage
    # UID: management_tillage_siteID_ExpUnitID_Date_crop
    MgtTillage_file_path = f'{directory_path}/management_tillage.csv'
    MgtTillage_columns_to_concate = ["expUnitId", "startDate", "crop"]
    process_dataframe(MgtTillage_file_path, f"{directory_path}/management_tillage_with_UID.csv", 
                                     MgtTillage_columns_to_concate, "mgtTillage_UID",siteID)
    process_dataframe(f"{directory_path}/management_tillage_with_UID.csv", 
                                     f"{directory_path}/management_tillage_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID",siteID, add_filename_to_id=False)
    
    #MgtGrowthStages
    # UID:  siteID_ExpUnitID_Date_crop
    MgtGrowthStage_file_path = f'{directory_path}/management_growth_stages.csv'
    MgtGrowthStage_columns_to_concate = ["expUnitId","date", "crop"]
    process_dataframe(MgtGrowthStage_file_path, f"{directory_path}/management_growth_stages_with_UID.csv", 
                                     MgtGrowthStage_columns_to_concate, "mgtGrowthStages_UID",siteID)
    process_dataframe(f"{directory_path}/management_growth_stages_with_UID.csv", 
                                     f"{directory_path}/management_growth_stages_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID",siteID, add_filename_to_id=False)

    #MgtResidue
    # UID:  management_growth_stages_siteID_ExpUnitID_Date_crop
    MgtResidue_file_path = f'{directory_path}/management_residue.csv'
    MgtResidue_columns_to_concate = ["expUnitId", "date", "crop"]
    process_dataframe(MgtResidue_file_path, f"{directory_path}/management_residue_with_UID.csv", 
                                     MgtResidue_columns_to_concate, "mgtResidue_UID", siteID)
    process_dataframe(f"{directory_path}/management_residue_with_UID.csv", 
                                     f"{directory_path}/management_residue_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)

    #MgtGrazing
    # UID:  management_grazing_siteID_ExpUnitID_startDate_endDate
    MgtGrazing_file_path = f'{directory_path}/management_grazing.csv'
    MgtGrazing_columns_to_concate = ["expUnitId", "startDate", "endDate"]
    process_dataframe(MgtGrazing_file_path, f"{directory_path}/management_grazing_with_UID.csv", 
                                     MgtGrazing_columns_to_concate, "mgtGrazing_UID", siteID)
    process_dataframe(f"{directory_path}/management_grazing_with_UID.csv", 
                                     f"{directory_path}/management_grazing_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)
    
    #MeasSoilPhys
    # UID: measurements_soil_physical_siteID_ExpUnitID_date_Upper_Lower
    MeasSoilPhys_file_path = f'{directory_path}/measurements_soil_physical.csv'
    MeasSoilPhys_columns_to_concate = ["expUnitId","date", "upperDepth_cm", "lowerDepth_cm"]
    process_dataframe(MeasSoilPhys_file_path, f"{directory_path}/measurements_soil_physical_with_UID.csv", 
                                     MeasSoilPhys_columns_to_concate,"measSoilPhys_UID",siteID)
    process_dataframe(f"{directory_path}/measurements_soil_physical_with_UID.csv", 
                                     f"{directory_path}/measurements_soil_physical_with_UID.csv", 
                                     ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)

    #MeasSoilChem
    # UID: measurements_soil_chemical_siteID_ExpUnitID_Date_Upper_Lower
    MeasSoilChem_file_path = f'{directory_path}/measurements_soil_chemical.csv'
    MeasSoilChem_columns_to_concate = ["expUnitId", "date", "upperDepth_cm", "lowerDepth_cm"]
    process_dataframe(MeasSoilChem_file_path, f'{directory_path}/measurements_soil_chemical_with_UID.csv', 
                                     MeasSoilChem_columns_to_concate, "measSoilChem_UID", siteID)
    process_dataframe(f"{directory_path}/measurements_soil_chemical_with_UID.csv", 
                                     f"{directory_path}/measurements_soil_chemical_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)

    #MeasSoilBiol
    # UID: measurements_soil_biological_siteID_ExpUnitID_Date_Upper_Lower
    MeasSoilBiol_file_path = f'{directory_path}/measurements_soil_biological.csv'
    MeasSoilBiol_columns_to_concate = ["expUnitId", "date", "upperDepth_cm", "lowerDepth_cm"]
    process_dataframe(MeasSoilBiol_file_path, f'{directory_path}/measurements_soil_biological_with_UID.csv', 
                                     MeasSoilBiol_columns_to_concate, "measSoilBiol_UID", siteID)
    process_dataframe(f"{directory_path}/measurements_soil_biological_with_UID.csv", 
                                     f"{directory_path}/measurements_soil_biological_with_UID.csv", ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)

    #MeasSoilCover
    # UID: measurements_soil_cover_siteID_expUnitId_soilCoverMeasuredDate_cropName
    MeasSoilCover_file_path = f'{directory_path}/measurements_soil_cover.csv'
    MeasSoilCover_columns_to_concate = ["expUnitId","date", "crop" ]
    process_dataframe(MeasSoilCover_file_path, f'{directory_path}/measurements_soil_cover_with_UID.csv', 
                                     MeasSoilCover_columns_to_concate, "measSoilCover_UID", siteID)

    #MeasGHGFlux
    # UID: measurements_greenhouse_gases_flux_siteID_ExpUnitID_Date_Time_Crop
    MeasGHGFlux_file_path = f'{directory_path}/measurements_greenhouse_gases_flux.csv'
    MeasGHGFlux_columns_to_concate = ["expUnitId", "date", "time", "crop"]
    gasSample_columns_to_concate = ["chamberPlacement"]
    process_dataframe(MeasGHGFlux_file_path, f"{directory_path}/measurements_greenhouse_gases_flux_with_UID.csv", 
                                     MeasGHGFlux_columns_to_concate, "measGHGFlux_UID", siteID, "gasSample_UID", gasSample_columns_to_concate)
    process_dataframe(f"{directory_path}/measurements_greenhouse_gases_flux_with_UID.csv", 
                                     f"{directory_path}/measurements_greenhouse_gases_flux_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)

    #MeasResidueMgnt
    # UID:  measurements_residue_management_siteID_ExpUnitID_Date_crop
    MeasResidueMgnt_file_path = f'{directory_path}/measurements_residue_management.csv'
    MeasResidueMgnt_columns_to_concate = ["expUnitId", "date", "crop"]
    process_dataframe(MeasResidueMgnt_file_path, f"{directory_path}/measurements_residue_management_with_UID.csv", 
                                     MeasResidueMgnt_columns_to_concate, "measResidueMgnt_UID",siteID)
    process_dataframe(f"{directory_path}/measurements_residue_management_with_UID.csv", 
                                     f"{directory_path}/measurements_residue_management_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)
    
    #MeasHarvestFraction
    # UID:  measurements_harvest_fraction_siteID_ExpUnitID_Date_crop_plantFraction
    MeasHarvestFraction_file_path = f'{directory_path}/measurements_harvest_fraction.csv'
    MeasHarvestFraction_columns_to_concate = ["expUnitId", "date", "crop", "plantFraction"]
    process_dataframe(MeasHarvestFraction_file_path, f"{directory_path}/measurements_harvest_fraction_with_UID.csv",
                                     MeasHarvestFraction_columns_to_concate, "measHarvestFraction_UID", siteID)
    process_dataframe(f"{directory_path}/measurements_harvest_fraction_with_UID.csv", 
                                     f"{directory_path}/measurements_harvest_fraction_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)
    
    #MeasBiomassCHO
    # UID:  measurements_biomass_cho_siteID_ExpUnitID_Date_crop_plantFraction
    MeasBiomassCHO_file_path = f'{directory_path}/measurements_biomass_cho.csv'
    MeasBiomassCHO_columns_to_concate = ["expUnitId", "date", "crop", "plantFraction"]
    process_dataframe(MeasBiomassCHO_file_path, f"{directory_path}/measurements_biomass_cho_with_UID.csv", 
                                     MeasBiomassCHO_columns_to_concate, "measBiomassCHO_UID", siteID)
    process_dataframe(f"{directory_path}/measurements_biomass_cho_with_UID.csv", 
                                     f"{directory_path}/measurements_biomass_cho_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)
    # MeasBiomassCHO_columns_to_concate = ["expUnitId", "Date", "Crop", "Plant Fraction"]

    #MeasBiomassEnergy
    # UID:  measurements_biomass_energy_siteID_ExpUnitID_Date_crop_plantFraction
    MeasBiomassEnergy_file_path = f'{directory_path}/measurements_biomass_energy.csv'
    MeasBiomassEnergy_columns_to_concate = ["expUnitId", "date", "crop", "plantFraction"]
    process_dataframe(MeasBiomassEnergy_file_path, f"{directory_path}/measurements_biomass_energy_with_UID.csv", 
                                     MeasBiomassEnergy_columns_to_concate, "measBiomassEnergy_UID", siteID)
    process_dataframe(f"{directory_path}/measurements_biomass_energy_with_UID.csv", 
                                     f"{directory_path}/measurements_biomass_energy_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)

    #MeasBiomassMinAn
    # UID:  measurements_biomass_mineral_analysis_siteID_ExpUnitID_Date_crop_plantFraction
    MeasBiomassMinAn_file_path = f'{directory_path}/measurements_biomass_mineral_analysis.csv'
    MeasBiomassMinAn_columns_to_concate = ["expUnitId", "date", "crop", "plantFraction"]
    process_dataframe(MeasBiomassMinAn_file_path, f"{directory_path}/measurements_biomass_mineral_analysis_with_UID.csv", 
                                     MeasBiomassMinAn_columns_to_concate, "measBiomassMinAn_UID", siteID)
    process_dataframe(f"{directory_path}/measurements_biomass_mineral_analysis_with_UID.csv", 
                                     f"{directory_path}/measurements_biomass_mineral_analysis_with_UID.csv", 
                                     ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)    

    #MeasGrazingPlants
    # UID:  measurements_grazing_plants_siteID_ExpUnitID_Date
    MeasGrazingPlants_file_path = f'{directory_path}/measurements_grazing_plants.csv'
    MeasGrazingPlants_columns_to_concate = ["expUnitId", "date"]
    process_dataframe(MeasGrazingPlants_file_path, f"{directory_path}/measurements_grazing_plants_with_UID.csv", 
                                     MeasGrazingPlants_columns_to_concate, "measGrazingPlants_UID", siteID)
    process_dataframe(f"{directory_path}/measurements_grazing_plants_with_UID.csv", 
                                     f"{directory_path}/measurements_grazing_plants_with_UID.csv", ExperUnits_columns_to_concate, 
                                     "expUnit_UID", siteID, add_filename_to_id=False)

    #MeasSuppRes (Might have different structure based on different excel files)
    # UID:  miscellaneousMeasurementUniqueId (Created using random UID)
    create_random_unique_ID(directory_path + "/measurements_supporting_research.csv", "miscellaneousMeasurementUniqueId", 
                            directory_path + "/measurements_supporting_research_with_UID.csv")
    process_dataframe(f"{directory_path}/measurements_supporting_research_with_UID.csv", 
                                     f"{directory_path}/measurements_supporting_research_with_UID.csv", 
                                     ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)

    # measyieldnutuptake
    # UID: measurements_yield_nutrient_uptake_ExpUnitID_Date
    measyieldnutuptake_file_path = f'{directory_path}/measurements_yield_nutrient_uptake.csv'
    measyieldnutuptake_columns_to_concate = ["expUnitId", "date"]
    process_dataframe(measyieldnutuptake_file_path, f"{directory_path}/measurements_yield_nutrient_uptake_with_UID.csv",
                                     measyieldnutuptake_columns_to_concate, "measYieldNutUptake_UID", siteID, add_filename_to_id=False)
    process_dataframe(f"{directory_path}/measurements_yield_nutrient_uptake_with_UID.csv",
                                     f"{directory_path}/measurements_yield_nutrient_uptake_with_UID.csv",
                                     ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)
    
    # measwinderosionarea
    # UID: measurements_wind_erosion_area_ExpUnitID_Date
    measwinderosionarea_file_path = f'{directory_path}/measurements_wind_erosion_area.csv'
    measwinderosionarea_columns_to_concate = ["expUnitId", "date"]
    process_dataframe(measwinderosionarea_file_path, f"{directory_path}/measurements_wind_erosion_area_with_UID.csv",
                                     measwinderosionarea_columns_to_concate, "measWindErosionArea_UID", siteID, add_filename_to_id=False)
    process_dataframe(f"{directory_path}/measurements_wind_erosion_area_with_UID.csv",
                                     f"{directory_path}/measurements_wind_erosion_area_with_UID.csv",
                                     ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)
    
    # measwaterqualityarea
    # UID: measurements_water_quality_area_ExpUnitID_Date
    measwaterqualityarea_file_path = f'{directory_path}/measurements_water_quality_area.csv'
    measwaterqualityarea_columns_to_concate = ["expUnitId", "date"]
    process_dataframe(measwaterqualityarea_file_path, f"{directory_path}/measurements_water_quality_area_with_UID.csv",
                                     measwaterqualityarea_columns_to_concate, "measWaterQualityArea_UID", siteID, add_filename_to_id=False)
    process_dataframe(f"{directory_path}/measurements_water_quality_area_with_UID.csv",
                                     f"{directory_path}/measurements_water_quality_area_with_UID.csv",
                                     ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)
    
    # measwaterqualityconc
    # UID: measurements_water_quality_concentration_ExpUnitID_Date
    measwaterqualityconc_file_path = f'{directory_path}/measurements_water_quality_concentration.csv'
    measwaterqualityconc_columns_to_concate = ["expUnitId", "date"]
    process_dataframe(measwaterqualityconc_file_path, f"{directory_path}/measurements_water_quality_concentration_with_UID.csv",
                                     measwaterqualityconc_columns_to_concate, "measWaterQualityConc_UID", siteID, add_filename_to_id=False)
    process_dataframe(f"{directory_path}/measurements_water_quality_concentration_with_UID.csv",
                                     f"{directory_path}/measurements_water_quality_concentration_with_UID.csv",
                                     ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)
    
    # measnutreff
    # UID: measurements_nutrience_efficiency_ExpUnitID_Date
    measnutreff_file_path = f'{directory_path}/measurements_nutrient_efficiency.csv'
    measnutreff_columns_to_concate = ["expUnitId", "date"]
    process_dataframe(measnutreff_file_path, f"{directory_path}/measurements_nutrient_efficiency_with_UID.csv",
                                     measnutreff_columns_to_concate, "measNutrEff_UID", siteID, add_filename_to_id=False)
    process_dataframe(f"{directory_path}/measurements_nutrient_efficiency_with_UID.csv",
                                     f"{directory_path}/measurements_nutrient_efficiency_with_UID.csv",
                                     ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)
   
    # measgasnutrientloss
    # UID: measurements_water_erosion_area_ExpUnitID_Date
    measgasnutrientloss_file_path = f'{directory_path}/measurements_gas_nutrient_loss.csv'
    measgasnutrientloss_columns_to_concate = ["expUnitId", "date"]
    process_dataframe(measgasnutrientloss_file_path, f"{directory_path}/measurements_gas_nutrient_loss_with_UID.csv",
                                     measgasnutrientloss_columns_to_concate, "measGasNutrientLoss_UID", siteID, add_filename_to_id=False)
    process_dataframe(f"{directory_path}/measurements_gas_nutrient_loss_with_UID.csv",
                                     f"{directory_path}/measurements_gas_nutrient_loss_with_UID.csv",
                                     ExperUnits_columns_to_concate, "expUnit_UID", siteID, add_filename_to_id=False)
