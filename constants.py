import pandas as pd

def property2columnGRACENET(column: str,sheet_name:str) -> str:
    """
    Sheet names :
    'measwaterqualityarea', 'metalocationoverview', 'metapersons', 'measyieldnutuptake', 
    'measwinderosionarea', 'mgtplanting', 'metatreatments', 'measgasnutrientloss', 
    'metasites', 'mgtgrowthstages', 'measbiomassenergy', 'meassoilbiol', 'measbiomasscho', 
    'meassoilphys', 'measwaterqualityconc', 'measgrazingplants', 'comometeorology', 
    'mgtresidue', 'measnutreff', 'metacitations', 'measbiomassminan', 'allcellcomments', 
    'mgttillage', 'meassoilcover', 'mgtamendments', 'meassoilchem', 'mgtgrazing', 
    'metaunits', 'measresiduemgnt', 'measghgflux', 'measharvestfraction'
    """
    if sheet_name == "metalocationoverview":
        mapping = {
            'locationId': 'fieldId',
            "siteDescriptor": "siteIdDescriptor",
            "researchUnit": "researchUnitDescription",
            "locationName": "projectName",
            "locationDescriptor": "experimentName",  
            "fundingSource": "organizationName",
        }
    elif sheet_name == "metasites":
        mapping = {
            'locationId': 'fieldId',
            "Date": "Date",  # not there
            "siteId": "siteId",
            "mlra": "majorLandResourceArea",
            "Field ID": "fieldId",  
            "country": "countryName",
            "stateProvince": "stateProvince",
            "county": "countyName",
            "city": "cityName",
            "postalCode": "postalCodeNumber",
            "latDecDeg": "latitude_decimal_deg",
            "longDecDeg": "longitude_decimal_deg",
            "spatialDescription": "siteSpatialDescription",
            "elevationM": "elevation_m",
            "MAP mm": "siteMeanAnnualPrecipitation_mm",  # not there
            "MAT degC": "siteMeanAnnualTemperature_degC",  # not there
            "nativeVeg": "siteNativeVegetation",
            "siteHistory": "siteHistory",
        }
    elif sheet_name == "metapersons":
        mapping = {
            # orcid?
            'locationId': 'fieldId',
            "primaryContact": "isPrimaryContact",
            "department": "departmentName",
            "organization": "organizationName",
            "Date Created": "dateCreated",  # not there
            "telephone": "phoneNumber",
            "webSite": "website",
            "note": "note",
        }
    elif sheet_name == "metacitations":
        mapping = {
            'locationId': 'fieldId',
            "datePublished": "publicationDate",
            "isPartOf": "bookName",
            "correspondAuthor": "correspondingAuthor",
            "identifierUsdaArs": "identifier",
        }
    elif sheet_name == "metatreatments":
        mapping = {
            'locationId': 'fieldId',
            "nTreatmentDescriptor": "nitrogenTreatmentDescriptor",
        }
    elif sheet_name == "metaunits":
        mapping = {
            "unitId": "expUnitId",
            'locationId': 'fieldId',
            "startDate": "startDate", 
            "endDate": "endDate",
            "changeInManagement": "changeInManagement",
            "soilSeries": "soilSeries",
        }
    elif sheet_name == "mgtamendments":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "startDate": "startDate",
            "crop": "crop",
            "amendPlacement": "amendmentPlacement",
            "amendDepthCm": "amendmentDepth_cm",
            "amendType": "type",
            "totalAmendAmountKgHa": "totalAmendmentAmount_kg_per_ha",
            "totalNAmountKgnHa": "totalNitrogenAmount_kgN_per_ha",
            "totalPAmountKgpHa": "totalPhosphorusAmount_kgP_per_ha",
            "totalKAmountKgkHa": "totalPotassiumAmount_kgK_per_ha",
            "totalPestAmountKgHa": "totalPesticideAmount_kg_per_ha",
            "activeIngredientType": "pesticideActiveIngredientType",
            "pestTarget": "pesticideTarget",
            "pestPlacement": "pesticidePlacement",
            "irrigationAmountCm": "irrigationAmount_cm",
            "irrigationType": "irrigationType",
            "irrigationNMgL": "irrigationNitrogen_mg_per_L",
        }
    elif sheet_name == "mgtplanting":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "treatmentId": "treatmentId",
            "startDate": "startDate",
            "crop": "crop",
            "cultivar": "cultivar",
            "plantingRateSeedsHa": "plantingRate_number_seeds_per_ha",
            "plantingDensityKgHa": "plantingDensity_kg_per_ha",
            "plantingMethod": "plantingMethod",
            "plantingDepthCm": "depth_cm",
            "rowWidthCm": "rowWidth_cm",
        }
    elif sheet_name == "mgttillage":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "treatmentId": "treatmentId",
            "startDate": "startDate",
            "crop": "crop",
            "tillageEvent": "tillageEvent",
            "tillageEventDepthCm": "tillageEventDepth_cm",
            "tillageEventMethod": "tillageEventMethod",
        }
    elif sheet_name == "mgtgrowthstages":
        mapping = {
            "unitId": "expUnitId",
            'locationId': 'fieldId',
            "date": "date",
            "growthStage": "growthStage",
            "crop": "crop",
            "treatmentId": "treatmentId",
        }
    elif sheet_name == "mgtresidue":
        mapping = {
            "unitId": "expUnitId",
            'locationId': 'fieldId',
            "treatmentId": "treatmentId",
            "startDate": "date",
            "crop": "crop",
            "equipmentType": "equipmentType",
            "cuttingHeightMaterialHarvested": "residueCuttingHeight",
            "rowsHarvestedPct": "rowsHarvestedPercent",
            "standAgeYears": "perennialStandAge_years",
            "stageAtHarvest": "stageAtHarvest",
        }
    elif sheet_name == "mgtgrazing":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "treatmentId": "treatmentId",
            "startDate": "startDate",
            "endDate": "endDate",
            "stockingRateNoanimalsHa": "stockingRate_number_animals_per_ha",
            "animalSpecies": "animalSpecies",
            "animalClass": "animalClass",
            "otherEvents": "otherEvents",
            "burnFrequencyYearsBetweenBurns": "yearsBetweenBurns",
            "burnIntensity": "burnIntensity",
        }
    elif sheet_name == "meassoilphys":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "date": "date",
            "treatmentId": "treatmentId",
            "upperCm": "upperDepth_cm",
            "lowerCm": "lowerDepth_cm",
            "sandPct": "sandPercent",
            "siltPct": "siltPercent",
            "clayPct": "clayPercent",
            "bulkDensityGCm3": "bulkDensity_g_per_cm_cubed",
            "wiltingPointPctVolume": "wiltingPoint_percent_volume",
            "fieldCapacityPctVolume": "fieldCapacity_percent_volume",
            "ksatCmSec": "saturatedHydraulicConductivity_cm_per_sec",
            "moistureReleaseCurve": "moistureReleaseCurve",
            "soilHeatFluxMjM2": "soilHeatFlux_MJ_per_m_squared",
            "aggregationPct": "aggregationPercent",
            "h2oStableAggregatesPct": "waterStableAggregatePercent",
            "nearInfraredCGcKg": "nearInfraredCarbon_gC_per_kg",
            "bulkDensityStdGCm3": "bulkDensitySd_g_per_cm_cubed",
            "wiltingPointStdPctVolume": "wiltingPointSd_percent_volume",
            "fieldCapacityStdPctVolume": "fieldCapacitySd_percent_volume",
            "ksatStdCmSec": "saturatedHydraulicConductivitySd_cm_per_sec",
            "soilHeatFluxStdMjM2": "soilHeatFluxSd_MJ_per_m_squared",
            "macroAggregatesStdPct": "macroAggregatesPercentStd",
            "h2oStableAggregatesStdPct": "waterStableAggregatesPercentStd",
            "nearInfraredCStdGcKg": "nearInfraredCarbonSd_gC_per_kg",
        }
    elif sheet_name == "meassoilchem":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "date": "date",
            "treatmentId": "treatmentId",
            "upperCm": "upperDepth_cm",
            "lowerCm": "lowerDepth_cm",
            "tscGcKg": "totalSoilCarbon_gC_per_kg",
            "tsnGnKg": "totalSoilNitrogen_gN_per_kg",
            "inorganicCGcKg": "inorganicCarbon_gC_per_kg",
            "organicCGcKg": "organicCarbon_gC_per_kg",
            "mineralCGcKg": "mineralCarbon_gC_per_kg",
            "cecCmolKg": "cationExchangeCapacity_cmol_per_kg",
            "electricConducSiemensM": "electricalConductivity_siemens_per_m",
            "solubleCMgcKg": "solubleOrganicCarbon_mgC_per_kg",
            "nh4MgnKg": "ammonium_mgN_per_kg",
            "no3MgnKg": "nitrate_mgN_per_kg",
            "pMgpKg": "phosphorus_mgP_per_kg",
            "kMgkKg": "potassium_mgK_per_kg",
            "caMgcaKg": "extractableCalcium_mgCa_per_kg",
            "mgMgmgKg": "extractableMagnesium_mgMg_per_kg",
            "cuMgcuKg": "extractableCopper_mgCu_per_kg",
            "feMgfeKg": "extractableIron_mgFe_per_kg",
            "mnMgmnKg": "extractableManganese_mgMN_per_kg",
            "znMgznKg": "extractableZinc_mgZn_per_kg",
            "mineralizableNGnKg": "mineralizableNitrogen_gN_per_kg",
            "nitriteMgnKg": "nitrites_mgN_per_kg",
            "phStd": "soilPhStd",
            "tscStdGcKg": "totalSoilCarbonSd_gC_per_kg",
            "tsnStdGnKg": "totalSoilNitrogenSd_gN_per_kg",
            "inorganicCStdGcKg": "inorganicCarbonSd_gC_per_kg",
            "organicStdGcKg": "organicCarbonSd_gC_per_kg",
            "mineralCStdGcKg": "mineralCarbonSd_gC_per_kg",
            "cecStdCmolKg": "cationExchangeCapacitySd_cmol_per_kg",
            "electricConducStdSiemensM": "electricalConductivitySd_siemens_per_m",
            "solubleCStdMgcKg": "solubleOrganicCarbonSd_mgC_per_kg",
            "nh4StdMgnKg": "ammoniumSd_mgN_per_kg",
            "no3StdMgnKg": "nitrateSd_mgN_per_kg",
            "pStdMgpKg": "phosphorusSd_mgP_per_kg",
            "kStdMgkKg": "potassiumSd_mgK_per_kg",
            "caStdMgcaKg": "extractableCalciumSd_mgCa_per_kg",
            "mgStdMgmgKg": "extractableMagnesiumSd_mgMg_per_kg",
            "cuStdMgcuKg": "extractableCopperSd_mgCu_per_kg",
            "feStdMgfeKg": "extractableIronSd_mgFe_per_kg",
            "mnStdMgmnKg": "extractableManganeseSd_mgMN_per_kg",
            "znStdMgznKg": "extractableZincSd_mgZn_per_kg",
            "mineralizableNStdGnKg": "mineralizableNitrogenSd_gN_per_kg",
            "nitriteStdMgnKg": "nitritesSd_mgN_per_kg",
        }
    elif sheet_name == "meassoilbiol":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "date": "date",
            "treatmentId": "treatmentId",
            "upperCm": "upperDepth_cm",
            "lowerCm": "lowerDepth_cm",
            "betaGlucosidaseMgKgHr": "glucosidase_mg_per_kg_per_hr",
            "betaGlucosaminidaseNagMgKgHr": "glucosaminidase_mg_per_kg_per_hr",
            "acidPhosphataseMgKgHr": "acidPhosphatase_mg_per_kg_per_hr",
            "alkalinePhosphataseMgKgHr": "alkPhosphatase_mg_per_kg_per_hr",
            "fluoresceinDiacetateHydrolysisMgKgHr": "soilfluoresceinDiacetateHydrol_mg_per_kg_per_hr",
            "glomalinGKg": "glomalin_g_per_kg",
            "FAME": "fattyAcidMethylEsters", # not there
            "PLFA": "phospholipidFattyAcids", # not there
            "DNA": "soilDna", #not there
            "idenPlantMaterialCGKg": "organicPlantMaterial_gC_per_kg",
            "pomCGKg": "particulateOrganicMatter_gC_per_kg",
            "microbialBiomassCMgKg": "carbonMicrobialBiomass_mgC_per_kg",
            "microbialBiomassNMgKg": "nitrogenMicrobialBiomass_mgN_per_kg",
            "netNh4NMgNKgDrySoil": "glucosidaseSd_mg_per_kg_per_hr",
            "betaGlucosaminidaseNagStdMgKgHr": "glucosaminidaseSd_mg_per_kg_per_hr",
            "acidPhosphataseStdMgKgHr": "acidPhosphataseSd_mg_per_kg_per_hr",
            "alkalinePhosphataseStdMgKgHr": "alkPhosphataseSd_mg_per_kg_per_hr",
            "fluoresceinDiacetateHydrolysisStdMgKgHr": "soilfluoresceinDiacetateHydrolSd_mg_per_kg_per_hr",
            "glomalinStdGKg": "glomalinSd_g_per_kg",
            "idenPlantMaterialCStdGKg": "organicPlantMaterialSd_gC_per_kg",
            'pomCStdGKg': 'particulateOrganicMatterSd_gC_per_kg',
            'microbialBiomassCStdMgcKg': 'carbonMicrobialBiomassSd_mgC_per_kg',
            'microbialBiomassNStdMgnKg': 'nitrogenMicrobialBiomassSd_mgN_per_kg',
        }
    elif sheet_name == "meassoilcover":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "crop": "crop",
            "soilWResiduePct": "soilWithResidueCoverPercent",
            "date": "date",
            "timingDescriptor": "soilCoverTimingDescriptor",
        }
    elif sheet_name == "measghgflux":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "date": "date",
            "time": "time",
            "crop": "crop",
            "chamberPlacement": "chamberPlacement",
            "n2oGnHaD": "nitrousOxide_gN_per_ha_per_d",
            "n2oInterpEq0ObsEq1": "isNitrousOxideInterpolated",
            "co2GcHaD": "carbonDioxide_gC_per_ha_per_d",
            "co2InterpEq0ObsEq1": "isCarbonDioxideInterpolated",
            "ch4GcHaD": "methane_gC_per_ha_per_d",
            "ch4InterpEq0ObsEq1": "isMethaneInterpolated",
            "airTempDegc": "airTemperature_degC",
            "soilTempDegc": "soilTemperature_degC",
            "soilMoisturePctVol": "soilMoisture_percent_volume",
            "soilMoistureDepthCm": "soilMoistureDepth_cm",
            "co2StdGcHaD": "carbonDioxideSd_gC_per_ha_per_d",
            "n2oStdGnHaD": "nitrousOxideSd_gN_per_ha_per_d",
            "ch4StdGcHaD": "methaneSd_gC_per_ha_per_d",
            "airTempStdDegc": "airTemperatureSd_degC",
            "soilTempStdDegc": "soilTemperatureSd_degC",
            "soilMoistureStdPctVol": "soilMoistureSd_percent_volume",
        }
    elif sheet_name == "measresiduemgnt":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "date": "date",
            "growthStage": "growthStage",
            "crop": "crop",
            "cornEarHeightCm": "cornEarHeight_cm",
            "aboveGBiomassKgHa": "aboveGroundBiomass_kg_per_ha",
            "unitGrainWeightMg": "unitGrainWeight_mg",
            "grainDryMattKgHa": "grainYield_kg_per_ha",
            "grainMoistPct": "grainMoisturePercent",
            "grainCKgcHa": "grainCarbon_kgC_per_ha",
            "grainNKgnHa": "grainNitrogen_kgN_per_ha",
            "harvNongrainBioKgHa": "driedHarvestedResidue_kg_per_ha",
            "harvResMoistPct": "harvestedResidueMoisturePercent",
            "harvResCKgcHa": "harvestedResidueCarbon_kgC_per_ha",
            "harvResNKgnHa": "harvestedResidueNitrogen_kgN_per_ha",
            "nonharvNongrainBioKgHa": "nonHarvestedResidueMass_kg_per_ha",
            "nonharvResMoistPct": "nonHarvestedResidueMoisturePercent",
            "nonharvResCKgcHa": "nonHarvestedResidueCarbonContent_kgC_per_ha",
            "nonharvResNKgnHa": "nonHarvestedResidueNitrogenContent_kgN_per_ha",
            "rootDryMattKgHa": "rootDryMatter_kg_per_ha",
            "rootMoistPct": "rootMoisturePercent",
            "rootCKgcHa": "rootCarbonContent_kgC_per_ha",
            "rootNKgnHa": "rootNitrogenContent_kgN_per_ha",
            "cornEarHeightStdCm": "cornEarHeightSd_cm",
            "aboveGBiomassStdKgHa": "aboveGroundBiomassSd_kg_per_ha",
            "unitGrainWeightStdMg": "unitGrainWeightSd_mg",
            "grainDryMattStdKgHa": "grainYieldSd_kg_per_ha",
            "grainMoistStdPct": "grainMoisturePercentStd",
            "grainCStdKgcHa": "grainCarbonSd_kgC_per_ha",
            "grainNStdKgnHa": "grainNitrogenSd_kgN_per_ha",
            "harvNongrainBioStdKgHa": "driedHarvestedResidueSd_kg_per_ha",
            "harvResMoistStdPct": "harvestedResidueMoisturePercentStd",
            "harvResCStdKgcHa": "harvestedResidueCarbonSd_kgC_per_ha",
            "harvResNStdKgnHa": "harvestedResidueNitrogenSd_kgN_per_ha",
            "nonharvNongrainBioStdKgHa": "nonHarvestedResidueMassSd_kg_per_ha",
            "nonharvResMoistStdPct": "nonHarvestedResidueMoisturePercentStd",
            "nonharvResCStdKgcHa": "nonHarvestedResidueCarbonContentSd_kgC_per_ha",
            "nonharvResNStdKgnHa": "nonHarvestedResidueNitrogenContentSd_kgN_per_ha",
            "rootDryMattStdKgHa": "rootDryMatterSd_kg_per_ha",
            "rootMoistStdPct": "rootMoisturePercentStd",
            "rootCStdKgcHa": "rootCarbonContentSd_kgC_per_ha",
            "rootNStdKgnHa": "rootNitrogenContentSd_kgN_per_ha",
        }
    elif sheet_name == "measharvestfraction":
        mapping = {
            # what is fresh matt?
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "samplingDate": "date",
            "growthStage": "growthStage",
            "crop": "crop",
            "plantFraction": "plantFraction",
            "fracDryMattKgHa": "dryBiomass_kg_per_ha",
            "fracMoistPct": "moisturePercent",
            "fracCKgcHa": "carbon_kgC_per_ha",
            "fracNKgnHa": "nitrogen_kgN_per_ha",
            "grainWeightMgKernel": "grainWeight_mg_per_kernel",
            "fracDryMattStdKgHa": "dryBiomassSd_kg_per_ha",
            "fracMoistStdPct": "moisturePercentStd",
            "fracCStdKgcHa": "carbonSd_kgC_per_ha",
            "fracNStdKgnHa": "nitrogenSd_kgN_per_ha",
            "grainWeightStdMgKernel": "grainWeightSd_mg_per_lernel",
        }
    elif sheet_name == "measbiomasscho":
        mapping = {
            'locationId': 'fieldId',
            "date": "date",
            'plantFraction': 'plantFraction',
            'growthStage': 'growthStage',
            'crop': 'crop',
            'unitId': 'expUnitId',
            "glucanGKg": "glucan_g_per_kg",
            "xylanGKg": "xylan_g_per_kg",
            "galactanGKg": "galactan_g_per_kg",
            "arabinanGKg": "arabinan_g_per_kg",
            "mannanGKg": "mannan_g_per_kg",
            "ligninGKg": "lignin_g_per_kg",
            "neutralDetFiberGKg": "neutralDetFiber_g_per_kg",
            "acidDetFiberGKg": "acidDetFiber_g_per_kg",
            "acidSolubleLigninGKg": "acidSolubleLignin_g_per_kg",
            "acidInsolubleLigninGKg": "acidInsolubleLignin_g_per_kg",
            "crudeProteinGKg": "crudeProtein_g_per_kg",
            "nonFiberCarbsGKg": "nonFiberCarbs_g_per_kg",
            "ashGKg": "ash_g_per_kg",
            "glucanStdGKg": "glucanSd_g_per_kg",
            "xylanStdGKg": "xylanSd_g_per_kg",
            "galactanStdGKg": "galactanSd_g_per_kg",
            "arabinanStdGKg": "arabinanSd_g_per_kg",
            "mannanStdGKg": "mannanSd_g_per_kg",
            "ligninStdGKg": "ligninSd_g_per_kg",
            "neutralDetFiberStdGKg": "neutralDetFiberSd_g_per_kg",
            "acidDetFiberStdGKg": "acidDetFiberSd_g_per_kg",
            "acidSolubleLigninStdGKg": "acidSolubleLigninSd_g_per_kg",
            "acidInsolubleLigninStdGKg": "acidInsolubleLigninSd_g_per_kg",
            "crudeProteinStdGKg": "crudeProteinSd_g_per_kg",
            "nonFiberCarbsStdGKg": "nonFiberCarbsSd_g_per_kg",
            "ashStdGKg": "ashSd_g_per_kg",
        }
    elif sheet_name == "measbiomassenergy":
        mapping = {
            'locationId': 'fieldId',
            'unitId': 'expUnitId',
            'date': 'date',
            'growthStage': 'growthStage',
            'crop': 'crop',
            'plantFraction': 'plantFraction',
            "ashStdGKg": "mineralMatterSd_g_per_kg",
            'volatileMatterGKg': 'volatileMatter_g_per_kg',
            'mineralMatterGKg': 'mineralMatter_g_per_kg',
            'grossCalorificValueMjKg': 'grossCalorificValue_MJ_per_kg',
            'volatileMatterStdGKg': 'volatileMatterSd_g_per_kg',
            'grossCalorificValueStdMjKg': 'grossCalorificValueSd_MJ_per_kg',
        }
    elif sheet_name == "measbiomassminan":
        mapping = {
            'locationId': 'fieldId',
            'unitId': 'expUnitId',
            'date': 'date',
            'growthStage': 'growthStage',
            'crop': 'crop',
            'plantFraction': 'plantFraction',
            "cConcentrationGKg": "carbonConcentration_g_per_kg",
            "nConcentrationGKg": "nitrogenConcentration_g_per_kg",
            "pConcentrationGKg": "phosphorusConcentration_g_per_kg",
            "kConcentrationGKg": "potassiumConcentration_g_per_kg",
            "caConcentrationGKg": "calciumConcentration_g_per_kg",
            "mgConcentrationGKg": "magnesiumConcentration_g_per_kg",
            "sConcentrationGKg": "sulfurConcentration_g_per_kg",
            "naConcentrationGKg": "sodiumConcentration_g_per_kg",
            "clConcentrationGKg": "chlorineConcentration_g_per_kg",
            "alConcentrationMgKg": "aluminumConcentration_mg_per_kg",
            "bConcentrationMgKg": "boronConcentration_mg_per_kg",
            "cuConcentrationMgKg": "copperConcentration_mg_per_kg",
            "feConcentrationMgKg": "ironConcentration_mg_per_kg",
            "mnConcentrationMgKg": "manganeseConcentration_mg_per_kg",
            "znConcentrationMgKg": "zincConcentration_mg_per_kg",
            "cConcentrationStdGKg": "carbonConcentrationSd_g_per_kg",
            "nConcentrationStdGKg": "nitrogenConcentrationSd_g_per_kg",
            "pConcentrationStdGKg": "phosphorusConcentrationSd_g_per_kg",
            "kConcentrationStdGKg": "potassiumConcentrationSd_g_per_kg",
            "caConcentrationStdGKg": "calciumConcentrationSd_g_per_kg",
            "mgConcentrationStdGKg": "magnesiumConcentrationSd_g_per_kg",
            "sConcentrationStdGKg": "sulfurConcentrationSd_g_per_kg",
            "naConcentrationStdGKg": "sodiumConcentrationSd_g_per_kg",
            "clConcentrationStdGKg": "chlorineConcentrationSd_g_per_kg",
            "alConcentrationStdMgKg": "aluminumConcentrationSd_mg_per_kg",
            "bConcentrationStdMgKg": "boronConcentrationSd_mg_per_kg",
            "cuConcentrationStdMgKg": "copperConcentrationSd_mg_per_kg",
            "feConcentrationStdMgKg": "ironConcentrationSd_mg_per_kg",
            "mnConcentrationStdMgKg": "manganeseConcentrationSd_mg_per_kg",
            "znConcentrationStdMgKg": "zincConcentrationSd_mg_per_kg",
        }
    elif sheet_name == "measgrazingplants":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            "date": "date",
            "speciesMix": "speciesMix",
            "growthStage": "growthStage",
            "broadleafVsGrass": "broadleafOrGrass",
            "abovegrBioKgHaDry": "aboveGroundBiomassDry_kg_per_ha",
            "surfaceLitterKgHaDry": "aurfaceLitterDry_kg_per_ha",
            "standingDeadKgHaDry": "atandingDeadDry_kg_per_ha",
            "laiKgHaDry": "leafAreaIndexDry_kg_per_ha",
            "biomassNPct": "biomassNitrogenPercentage",
            "ligninPct": "ligninPercentage",
            "groundCoverPct": "groundCoverPercentage",
            "abovegrBioCKgcHa": "aboveGroundBiomassCarbon_kgC_per_ha",
            "abovegrBioNKgnHa": "aboveGroundBiomassNitrogen_kgN_per_ha",
            "belowgrBioCKgcHa": "belowGroundBiomassCarbon_kgC_per_ha",
            "belowgrBioNKgnHa": "belowGroundBiomassNitrogen_kgN_per_ha",
            "anppCKgcHaYr": "abovegroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr",
            "anppNKgnHaYr": "abovegroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr",
            "bnppCKgcHaYr": "belowgroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr",
            "bnppNKgnHaYr": "belowgroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr",
            "abovegrBioStdKgHaDry": "aboveGroundBiomassDrySd_kg_per_ha",
            "surfaceLitterStdKgHaDry": "aurfaceLitterDrySd_kg_per_ha",
            "standingDeadStdKgHaDry": "atandingDeadDrySd_kg_per_ha",
            "laiStdKgHa": "leafAreaIndexDrySd_kg_per_ha",
            "biomassNStdPct": "biomassNitrogenPercentageStd",
            "ligninStdPct": "ligninPercentageStd",
            "groundCoverStdPct": "groundCoverPercentageStd",
            "abovegrBioCStdKgcHa": "aboveGroundBiomassCarbonSd_kgC_per_ha",
            "abovegrBioNStdKgnHa": "aboveGroundBiomassNitrogenSd_kgN_per_ha",
            "belowgrBioCStdKgcHa": "belowGroundBiomassCarbonSd_kgC_per_ha",
            "belowgrBioNStdKgnHa": "belowGroundBiomassNitrogenSd_kgN_per_ha",
            "anppCStdKgcHaYr": "abovegroundNetPrimaryProductivityCarbonSd_kgC_per_ha_per_yr",
            "anppNStdKgnHaYr": "abovegroundNetPrimaryProductivityNitrogenSd_kgN_per_ha_per_yr",
            "bnppCStdKgcHaYr": "belowgroundNetPrimaryProductivityCarbonSd_kgC_per_ha_per_yr",
            "bnppNStdKgnHaYr": "belowgroundNetPrimaryProductivityNitrogenSd_kgN_per_ha_per_yr",
        }
    elif sheet_name == "comometeorology":
        mapping =  {
                "Site ID": "siteId",
                "locationId": "fieldId",
                "unitId": "expUnitId",
                "treatmentId": "weatherStationId", 
                "elevation_m": "elevation_m",
                "date": "date",
                "tempMaxDegc": "tempMax_degC",
                "tempMinDegc": "tempMin_degC",
                "precipMmD": "precipitation_mm_per_d",
                "badValueFlag": "weatherBadValueFlag",
                "rhPct": "relativeHumidityPercent",
                "Dew Point degC": "dewPointDegc", # not there
                'windSpeedMS': 'windSpeed_m_per_s',  
                'solarRadiationVegMjM2D': 'solarRadiationVegetatedGround_MJ_per_m_squared_per_d',
                'solarRadiationBareMjM2D': 'solarRadiationBareSoil_MJ_per_m_squared_per_d',
                'soilTemp5CmDegc': 'soilTemp5cm_degC',
                'soilTemp10CmDegc': 'soilTemp10cm_degC',
                'windDirectionDegFromN': 'windDirectionDegFromNorth',
                'openPanEvapMmD': 'openPanEvaporation_mm_per_d',
                'closedPanEvapMmD': 'closedPanEvaporation_mm_per_d',
                'atmosNDepositionKgHaD': 'atmosphericNitrogenDeposition_kg_per_ha_per_d',
                'totalNetRadiationMjM2D': 'totalSolarRadiationBareSoil_MJ_per_m_squared_per_d',
                'snowMmD': 'snow_mm_per_d',
                "Site ID": "siteId",
        }

        # NEED TO CHECK THESE ARE CORRECT
    elif sheet_name == "measnutreff":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            'fractionNKgnHa' : 'fracNitrogen_kg_ha',
            'nitrogen15UseEfficiencyKgnHa': 'nitrogenUseEfficiency_kg_ha', # 15?
            'agronomicEfficiencyKgKg': 'agronomicEfficiency_kg_kg',
            'nutrientEfficiencyRatioKgKg': 'nutrientEfficiencyRatio_kg_kg',
        }
    elif sheet_name == "measwaterqualityarea":
        mapping = {
            'locationId': 'fieldId',
            "unitId": "expUnitId",
            'erosionTSedimentHa': 'erosionSediment_t_ha',
            'erosionTotalSuspendedSolidsTHa': 'erosionTotalSuspendedSolids_t_ha',
            'erosionTSedimentHaStd': 'erosionSedimentSd_t_ha',
            'erosionTotalSuspendedSolidsTHaStd': 'erosionTotalSuspendedSolidsSd_t_ha',
            'erosionTotalSolidsTHaStd': 'erosionTotalSolidsSd_t_ha',
            'erosionTotalSolidstHa': 'erosionTotalSolids_t_ha',
            'soilOrganicMatterKgHaStd': 'soilOrganicMatterSd_kg_ha',
            'soilOrganicMatterKgHa': 'soilOrganicMatter_kg_ha',
            'soilOrganicCarbonKgCHa':'soilOrganicCarbon_kgC_ha',
            'soilOrganicCarbonKgCHaStd': 'soilOrganicCarbonSd_kgC_ha',
            'waterMm': 'water_mm',
            'waterMmStd': 'waterSd_mm',
            'kgTotalNHa' : 'totalNitrogen_kg_ha',
            'kgTotalPHa': 'totalPhosphoru_kg_ha',
            'kgNh4NHa' : 'ammoniumNitroge_kg_ha',
            'kgNo3NHa': 'nitrateNitrogen_kg_ha',
            'totalDissolvedNKgNHa': 'totalDissolvedNitrogen_kgN_ha',
            'kgTotalDissolvedPHa': 'totalDissolvedPhosphorus_kgP_ha',
            'kgTotalClHa': 'totalChloride_kg_ha',
            'ecMsCm':'electricalConductivity_ms_cm', 
            'dissolvedKgKHa': 'dissolvedPotassium_kgK_ha',
            'dissolvedKgSHa': 'dissolvedSulfur_kgS_ha',
            'dissolvedKgCaHa': 'dissolvedCalcium_kgCa_ha',
            'dissolvedKgMgHa': 'dissolvedMagnesium_kgMg_ha',
            'dissolvedGCuHa': 'dissolvedCopper_gCu_ha', # is this correction
            'dissolvedGFeHa': 'dissolvedIron_gFe_ha',
            'dissolvedGMnHa': 'dissolvedManganese_gMn_ha',
            'dissolvedGZnHa': 'dissolvedZinc_gZn_ha',
            'dissolvedGBHa': 'dissolvedBoron_gB_ha',
            'dissolvedGMoHa': 'dissolvedMolybdenum_gMo_ha',
            'dissolvedKgAlHa': 'dissolvedAluminum_kg_al_ha',
            'dissolvedKgNaHa': 'dissolvedSodium_kgNa_ha',
            'dissolvedKgSiHa': 'dissolvedSilicon_kgSi_ha',
            'kgTotalNHaStd': 'totalNitrogenSd_kgN_ha',
            'kgTotalPHaStd': 'totalPhosphorusSd_kgP_ha',
            'kgNh4NHaStd': 'inorganicNitrogenSd_kgN_ha',
            'kgNo3NHaStd': 'nitrateSd_kgN_ha',
            'totalDissolvedNKgNHaStd': 'totalDissolvedNitrogenSd_kgN_ha',
            'kgTotalDissolvedPHaStd': 'totalDissolvedPhosphorusSd_jgP_ha',
            'kgTotalClHaStd': 'totalChlorideSd_kg_cl_ha',
            'ecMsCmStd':'electricalConductivitySd_ms_cm',
            'dissolvedKgKHaStd': 'dissolvedPotassiumSd_kgK_ha',
            'dissolvedKgSHaStd': 'dissolvedSulfurSd_kgS_ha',
            'dissolvedKgCaHaStd': 'dissolvedCalciumSd_kgCa_ha',
            'dissolvedKgMgHaStd': 'dissolvedMagnesiumSd_kgMg_ha',
            'dissolvedGCuHaStd': 'dissolvedCopperSd_gCu_ha',
            'dissolvedGFeHaStd': 'dissolvedIronSd_gFe_ha',
            'dissolvedGMnHaStd': 'dissolvedManganeseSd_gMn_ha',
            'dissolvedGZnHaStd': 'dissolvedZincSd_gZn_ha',
            'dissolvedGBHaStd': 'dissolvedBoronSd_gB_ha',
            'dissolvedGMoHaStd': 'dissolvedMolybdenumSd_gMo_ha',
            'dissolvedKgAlHaStd': 'dissolvedAluminumSd_kg_al_ha',
            'dissolvedKgNaHaStd': 'dissovledSodiumSd_kgNa_ha',
            'dissolvedKgSiHaStd': 'dissovledSiliconSd_kgSi_ha',
        }
    elif sheet_name == "measwaterqualityconc":
        mapping = {
            'locationId': 'fieldId',
            'unitId': 'expUnitId',
            'samplingDepthCm': 'samplingDepth_cm',
            'erosionKgSediment':'erosionSediment_kg',
            'erosionKgSuspendedSolids': 'erosionSuspendedSolids_kg',
            'erosionTotalSolidsKg': 'erosionTotalSolids_kg',
            'waterMm': 'water_mm',
            'waterMmStd': 'waterSd_mm',
            'mgNo3NL': 'nitrate_mg_l',
            'erosionKgSedimentStd': 'erosionSedimentSd_kg',
            'erosionTotalSuspendedSolidsKg': 'erosionTotalSuspendedSolids_kg',
            'erosionTotalSuspendedSolidsKgStd': 'erosionTotalSuspendedSolidsSd_kg',
            'erosionTotalSolidsKgStd': 'erosionTotalSolidsSd_kg',
            'totalDissolvedNMgL': 'totalDissolvedNitrogen_mgN_l',
            'mgTotalDissolvedPL': 'totalDissolvedPhosphorus_mgP_l',
            'mgClL': 'chloride_mg_l',
            'ecMsCm': 'electricalConductivity_ms_cm', # is this correct ?
            'mgTotalNL': 'totalNitrogen_mg_l',
            'mgTotalPL': 'totalPhosphorus_mg_l',
            'mgNh4NL': 'InorganicNitrogen_mg_l',
            'soilOrganicMatterMgSomL': 'soilOrganicMatter_mgSom_l',
            'soilOrganicCarbonMgCL': 'soilOrganicCarbon_mg_c_l',
            'dissolvedMgKL': 'dissolvedPotassium_mgK_l',
            'dissolvedMgSL': 'dissolvedSulfur_mgS_l',
            'dissolvedMgCaL': 'dissolvedCalcium_mgCa_l',
            'dissolvedMgMgL': 'dissolvedMagnesium_mgMg_l',
            'dissolvedUgCuL': 'dissolvedCopper_ugCu_l',
            'dissolvedUgFeL': 'dissolvedIron_ugFe_l',
            'dissolvedUgMnL': 'dissolvedManganese_ugMn_l',
            'dissolvedUgZnL': 'dissolvedZinc_ugZn_l',
            'dissolvedUgBL': 'dissolvedBoron_ugB_l',
            'dissolvedUgMoL': 'dissolvedMolybdenum_ugMo_l',
            'dissolvedMgAlL': 'dissolvedAluminum_mg_al_l',
            'dissolvedMgNaL': 'dissolvedSodium_mgNa_l',
            'dissolvedMgSiL': 'dissolvedSilicon_mgSi_l',
            'soilOrganicMatterMgSomLStd': 'soilOrganicMatterSd_mgSom_l',
            'soilOrganicCarbonMgCLStd': 'soilOrganicCarbonSd_mg_c_l',
            'mgTotalNLStd': 'totalNitrogenSd_mg_l',
            'mgTotalPLStd': 'totalPhosphorusSd_mg_l',
            'mgNh4NLStd': 'InorganicNitrogenSd_mg_l',
            'mgNo3NLStd': 'nitrateSd_mg_l',
            'totalDissolvedNMgLStd': 'totalDissolvedNitrogenSd_mgN_l',
            'mgTotalDissolvedPLStd': 'totalDissolvedPhosphorusSd_mgP_l',
            'mgClLStd': 'chlorideSd_mg_l',
            'ecMsCmStd': 'electricalConductivitySd_ms_cm',
            'dissolvedMgKLStd': 'dissolvedPotassiumSd_mgK_l',
            'dissolvedMgSLStd': 'dissolvedSulfurSd_mgS_l',
            'dissolvedMgCaLStd': 'dissolvedCalciumSd_mgCa_l',
            'dissolvedMgMgLStd': 'dissolvedMagnesiumSd_mgMg_l',
            'dissolvedUgCuLStd': 'dissolvedCopperSd_ugCu_l',
            'dissolvedUgFeLStd': 'dissolvedIronSd_ugFe_l',
            'dissolvedUgMnLStd': 'dissolvedManganeseSd_ugMn_l',
            'dissolvedUgZnLStd': 'dissolvedZincSd_ugZn_l',
            'dissolvedUgBLStd': 'dissolvedBoronSd_ugB_l',
            'dissolvedUgMoLStd': 'dissolvedMolybdenumSd_ugMo_l',
            'dissolvedMgAlLStd': 'dissolvedAluminumSd_mg_al_l',
            'dissolvedMgNaLStd': 'dissolvedSodiumSd_mgNa_l',
            'dissolvedMgSiLStd': 'dissolvedSiliconSd_mgSi_l',

        }
    elif sheet_name == 'measyieldnutuptake':
        mapping = {
            'locationId': 'fieldId',
            'unitId': 'expUnitId',
            'samplingDate': 'date',
            'fracDryMattKgHaYnu': 'fracCropProductivity_kg_ha',
            'grainWeightMgKernelYnu': 'grainWeightKernelYnu_mg',
            'fracMoistPctYnu': 'fracMoisturePercent',
            'fracCKgcHaYnu': 'fracCarbon_kgC_ha',
            'fracNKgnHaYnu': 'fracNitrogen_kgN_ha',
            'fracPKgpHa': 'fracPhosphorus_kgP_ha',
            'fracKKgkHa': 'fracPotassium_kgK_ha',
            'fracSKgsHa': 'fracSulfur_kgS_ha',
            'fracCaKgcaHa': 'fracCalcium_kgCa_ha',
            'fracMgKgmgHa': 'fracMagnesium_kgMg_ha',
            'fracCuGcuHa': 'fracCopper_gCu_ha',
            'fracFeGfeHa': 'fracIron_gFe_ha',
            'fracMnGmnHa': 'fracManganese_gMn_ha',
            'fracZnGznHa': 'fracZinc_gZn_ha',
            'fracBGbHa': 'fracBoron_gB_ha',
            'fracMoGmoHa': 'fracMolybdenum_gMo_ha',
            'fracDryMattStdKgHaYnu': 'fracProductivitySd_kg_ha',
            'fracMoistStdPctYnu': 'fracMoisturePercentStd',
            'fracCStdKgcHaYnu': 'fracCarbonSd_kgC_ha',
            'fracNStdKgnHaYnu': 'fracNitrogenSd_kgN_ha',
            'fracPStdKgpHa': 'fracPhosphorusSd_kgP_ha',
            'fracKStdKgkHa': 'fracPotassiumSd_kgK_ha',
            'fracSStdKgsHa': 'fracSulfurSd_kgS_ha',
            'fracCaStdKgcaHa': 'fracCalciumSd_kgCa_ha',
            'fracMgStdKgmgHa': 'fracMagnesiumSd_kgMg_ha',
            'fracCuStdGcuHa': 'fracCopperSd_gCu_ha',
            'fracFeStdGfeHa': 'fracIronSd_gFe_ha',
            'fracMnStdGmnHa': 'fracManganeseSd_gMn_ha',
            'fracZnStdGznHa': 'fracZincSd_gZn_ha',
            'fracBStdGbHa': 'fracBoronSd_gB_ha',
            'fracMoStdGmoHa': 'fracMolybdenumSd_gMo_ha',
            'grainWeightStdMgKernelYnu': 'grainWeightKernelYnuSd_mg',
        }
    elif sheet_name == 'measwinderosionarea':
        mapping = {
            'locationId': 'fieldId',
            'unitId': 'expUnitId',
            'soilTHa': 'soil_t_ha',
            'soilTHaStd': 'soilSd_t_ha',
            'soilOrganicMatterKgHa': 'soilOrganicMatter_kg_ha',
            'soilOrganicCarbonKgCHa': 'soilOrganicCarbon_kg_ha',
            'soilOrganicMatterKgHaStd': 'soilOrganicMatterSd_kg_ha',
            'soilOrganicCarbonKgCHaStd': 'soilOrganicCarbonSd_kgC_ha',
            'ecMsCm': 'electricalConductivity_ms_cm', # is this correct ?
            'kgTotalNHa': 'totalNitrogen_kg_ha',
            'kgNh4NHa': 'inorganicNitrogen_kgN_ha',
            'kgNo3NHa': 'nitrate_kg_ha',
            'kgPHa': 'phosphorus_kg_ha',
            'kgKHa': 'potassium_kg_ha',
            'kgSHa': 'sulfur_kg_ha',
            'kgCaHa': 'calcium_kg_ha',
            'kgMgHa': 'magnesium_kg_ha',
            'gCuHa': 'copper_g_ha',
            'gFeHa': 'iron_g_ha',
            'gMnHa': 'manganese_g_ha',
            'gZnHa': 'zinc_g_ha',
            'gBHa': 'boron_g_ha',
            'gMoHa': 'molybdenum_g_ha',
            'kgAlHa': 'aluminum_kg_ha',
            'kgNaHa': 'sodium_kg_ha',
            'kgSiHa': 'silicon_kg_ha',
            'ecMsCmStd': 'electricalConductivitySd_ms_cm',
            'kgTotalNHaStd': 'totalNitrogenSd_kgN_ha',
            'kgNh4NHaStd': 'inorganicNitrogenSd_kgN_ha',
            'kgNo3NHaStd': 'nitrateSd_kgN_ha',
            'kgPHaStd': 'phosphorusSd_kg_ha',
            'kgKHaStd': 'potassiumSd_kg_ha',
            'kgSHaStd': 'sulfurSd_kg_ha',
            'kgCaHaStd': 'calciumSd_kg_ha',
            'kgMgHaStd': 'magnesiumSd_kg_ha',
            'gCuHaStd': 'copperSd_g_ha',
            'gFeHaStd': 'ironSd_g_ha',
            'gMnHaStd': 'manganeseSd_g_ha',
            'gZnHaStd': 'zincSd_g_ha',
            'gBHaStd': 'boronSd_g_ha',
            'gMoHaStd': 'molybdenumSd_g_ha',
            'kgAlHaStd': 'aluminumSd_kg_ha',
            'kgNaHaStd': 'sodiumSd_kg_ha',
            'kgSiHaStd': 'siliconSd_kg_ha',
        }
    elif sheet_name == 'measgasnutrientloss':
        mapping = {
            'locationId': 'fieldId',
            'unitId': 'expUnitId',
            'noxNGHaDay': 'nitrousOxides_g_ha',
            'n2NGHaDay': 'nitrogenGas_g_ha',
            'n2oNGHaDay': 'nitrousOxide_g_ha',
            'nh3NKgHaDay': 'ammoniaNitrogen_kg_ha',
            'noxNStdGHaDay': 'nitrousOxidesSd_g_ha',
            'n2NStdGHaDay': 'nitrogenGasSd_g_ha',
            'n2oNStdGHaDay': 'nitrousOxideSd_g_ha',
            'nh3NStdKgHaDay': 'ammoniaNitrogenSd_kg_ha',
        }
    else :
        mapping = {}
    
    return mapping.get(column, None)

def column2property(column: str,sheet_name:str) -> str:
    """
    Converts a column name to a property name.
    """
    if sheet_name == "Overview":
        mapping = {
            "Site ID": "siteId",
            "Site ID descriptor": "siteIdDescriptor",
            "Research Unit": "researchUnitDescription",
            "Project Name": "projectName",
            "Experiment Name": "experimentName",
            "Funding Source": "organizationName",
            "Start Date": "startDate",
            "End Date": "endDate",
            "Duration of Study": "durationOfStudy",
        }
    elif sheet_name == "FieldSites":
        mapping = {
            "Date": "Date",
            "Site ID": "siteId",
            "MLRA": "majorLandResourceArea",
            "Field ID": "fieldId",
            "Country": "countryName",
            "State/Province": "stateProvince",
            "County": "countyName",
            "City": "cityName",
            "Postal Code": "postalCodeNumber",
            "Latitude decimal deg": "latitude_decimal_deg",
            "Longitude decimal deg": "longitude_decimal_deg",
            "Spatial Description": "siteSpatialDescription",
            "Elevation m": "elevation_m",
            "MAP mm": "siteMeanAnnualPrecipitation_mm",
            "MAT degC": "siteMeanAnnualTemperature_degC",
            "Native Veg": "siteNativeVegetation",
            "Site History": "siteHistory",
        }
    elif sheet_name == "Persons":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Site ID": "siteId",
            "Treatment ID": "treatmentId",
            "Last Name": "lastName",
            "First Name": "firstName",
            "Middle Name": "middleName",
            "Suffix": "suffix",
            "Role in Study": "roleInStudy",
            "Primary Contact": "isPrimaryContact",
            "Department": "departmentName",
            "Organization": "organizationName",
            "Date Created": "dateCreated",
            "Profession": "profession",
            "Email": "email",
            "Telephone": "phoneNumber",
            "Web Site": "website",
            "note": "note",
        }

    # Citations

    elif sheet_name == "Citations":
        mapping = {
            "Site ID": "siteId",
            "Date Published": "publicationDate",
            "Type": "citationType",
            "title": "title",
            "Is Part Of": "bookName",
            "author": "author",
            "Correspond Author": "correspondingAuthor",
            "identifier": "identifier",
            "description": "description",
            "citation": "citation",
        }


    elif sheet_name == "Treatments":
        mapping = {
            "Treatment ID": "treatmentId",
            "Start Date": "startDate",
            "Treatment Descriptor": "treatmentDescriptor",
            "Rotation Descriptor": "rotationDescriptor",
            "Tillage Descriptor": "tillageDescriptor",
            "N Treatment Descriptor": "nitrogenTreatmentDescriptor",
            "Project Scenario": "projectScenario",
            "Fertilizer Amendment Class": "fertilizerAmendmentClass",
            "Cover Crop": "coverCrop",
            "Residue Removal": "residueRemoval",
            "Irrigation": "irrigation",
            "Organic Management": "organicManagement",
            "Grazing Rate": "grazingRate",
        }

    elif sheet_name == "ExperUnits":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Field ID": "fieldId",
            "Start Date": "startDate",
            "End Date": "endDate",
            "End Date": "endDate",
            "Start Date": "startDate",
            "Soil Series": "soilSeries",
            "Landscape Position": "landscapePosition",
            "Soil Classification": "soilClassification",
            "Slope %": "fieldSlopePercent",
            "Exp Unit Size m2": "expUnitSize_m_squared",
            "Treatment ID": "treatmentId",
        }

    elif sheet_name == "WeatherStation":
        mapping = {
            "Site ID": "siteId",
            "Field ID": "fieldId",
            "Date": "date",
            "Weather Station ID": "weatherStationId",
            "Distance from Field m": "weatherStationDistanceFromField_m",
            "Direction from Field": "weatherStationDirectionFromField",
            "Weather Station URL": "weatherStationUrl",
            "Weather Latitude decimal deg": "weatherStationlatitude_decimal_deg",
            "Weather Longitude decimal deg": "weatherStationlongitude_decimal_deg",
            "Weather Elevation m": "elevation_m",
        }

    # WeatherDaily

    elif sheet_name == "WeatherDaily":
        mapping = {
            "Site ID": "siteId",
            "Field ID": "fieldId",
            "Weather Date": "date",
            "Temp Max degC": "tempMax_degC",
            "Temp Min degC": "tempMin_degC",
            "Precip mm/d": "precipitation_mm_per_d",
            "Bad Value Flag": "weatherBadValueFlag",
            "RH %": "relativeHumidityPercent",
            "Dew Point degC": "dewPointDegc",
            'Wind Speed m/s': 'windSpeed_m_per_s',
            'Solar Radiation Veg MJ/m2/d': 'solarRadiationVegetatedGround_MJ_per_m_squared_per_d',
            'Solar Radiation Bare MJ/m2/d': 'solarRadiationBareSoil_MJ_per_m_squared_per_d',
            'Soil Temp 5cm degC': 'soilTemp5cm_degC',
            'Soil Temp 10cm degC': 'soilTemp10cm_degC',
            'Wind Direction deg from N': 'windDirectionDegFromNorth',
            'Open Pan Evap mm/d': 'openPanEvaporation_mm_per_d',
            'Closed Pan Evap mm/d': 'closedPanEvaporation_mm_per_d',
            'Atmos N Deposition kg/ha/d': 'atmosphericNitrogenDeposition_kg_per_ha_per_d',
            'Total Net Radiation MJ/m2/d': 'totalSolarRadiationBareSoil_MJ_per_m_squared_per_d',
            'Snow mm/d': 'snow_mm_per_d',
        }
    elif sheet_name == "MgtAmendments":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Treatment ID": "treatmentId",
            "Date": "date",
            "Crop": "crop",
            "Amend Placement": "amendmentPlacement",
            "Amend Depth cm": "amendmentDepth_cm",
            "Amend Type": "type",
            "Total Amend Amount kg/ha": "totalAmendmentAmount_kg_per_ha",
            "Total N Amount kgN/ha": "totalNitrogenAmount_kgN_per_ha",
            "Total P Amount kgP/ha": "totalPhosphorusAmount_kgP_per_ha",
            "Total K Amount kgK/ha": "totalPotassiumAmount_kgK_per_ha",
            "Total Pest Amount kg/ha": "totalPesticideAmount_kg_per_ha",
            "Active Ingredient Type": "pesticideActiveIngredientType",
            "Pest Target": "pesticideTarget",
            "Pest Placement": "pesticidePlacement",
            "Irrigation Amount cm": "irrigationAmount_cm",
            "Irrigation Type": "irrigationType",
            "Irrigation N mg/L": "irrigationNitrogen_mg_per_L",
        }
    elif sheet_name == "MgtPlanting":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Treatment ID": "treatmentId",
            "Date": "date",
            "Crop": "crop",
            "Cultivar": "cultivar",
            "Planting Rate #seeds/ha": "plantingRate_number_seeds_per_ha",
            "Planting Density kg/ha": "plantingDensity_kg_per_ha",
            "Planting Method": "plantingMethod",
            "Planting Depth cm": "depth_cm",
            "Row Width cm": "rowWidth_cm",
        }
    elif sheet_name == "MgtTillage":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Treatment ID": "treatmentId",
            "Date": "date",
            "Crop": "crop",
            "Tillage Event": "tillageEvent",
            "Tillage Event Depth cm": "tillageEventDepth_cm",
            "Tillage Event Method": "tillageEventMethod",
        }
    elif sheet_name == "MgtGrowthStages":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Date": "date",
            "Growth Stage": "growthStage",
            "Crop": "crop",
            "Treatment ID": "treatmentId",
        }
    elif sheet_name == "MgtResidue":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Treatment ID": "treatmentId",
            "Date": "date",
            "Crop": "crop",
            "Equipment Type": "equipmentType",
            "Cutting Height/Material Harvested": "residueCuttingHeight",
            "Rows Harvested %": "rowsHarvestedPercent",
            "Stand Age years": "perennialStandAge_years",
            "Stage at Harvest": "stageAtHarvest",
        }
    elif sheet_name == "MgtGrazing":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Treatment ID": "treatmentId",
            "Start Date": "date",
            "End Date": "date",
            "Stocking Rate #animals/ha": "stockingRate_number_animals_per_ha",
            "Animal Species": "animalSpecies",
            "Animal Class": "animalClass",
            "Other Events": "otherEvents",
            "Burn Frequency years between burns": "yearsBetweenBurns",
            "Burn Intensity": "burnIntensity",
        }
    elif sheet_name == "MeasSoilPhys":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Date": "date",
            "Treatment ID": "treatmentId",
            "Upper cm": "upperDepth_cm",
            "Lower cm": "lowerDepth_cm",
            "Sand %": "sandPercent",
            "Silt %": "siltPercent",
            "Clay %": "clayPercent",
            "Bulk Density g/cm3": "bulkDensity_g_per_cm_cubed",
            "Wilting Point % volume": "wiltingPoint_percent_volume",
            "Field Capacity % volume": "fieldCapacity_percent_volume",
            "Ksat cm/sec": "saturatedHydraulicConductivity_cm_per_sec",
            "Moisture Release Curve": "moistureReleaseCurve",
            "Soil Heat Flux MJ/m2": "soilHeatFlux_MJ_per_m_squared",
            "Aggregation %": "aggregationPercent",
            "H2O Stable Aggregates %": "waterStableAggregatePercent",
            "Near-Infrared C gC/kg": "nearInfraredCarbon_gC_per_kg",
            "Bulk Density STD g/cm3": "bulkDensitySd_g_per_cm_cubed",
            "Wilting Point STD % volume": "wiltingPointSd_percent_volume",
            "Field Capacity STD % volume": "fieldCapacitySd_percent_volume",
            "Ksat STD cm/sec": "saturatedHydraulicConductivitySd_cm_per_sec",
            "Soil Heat Flux STD MJ/m2": "soilHeatFluxSd_MJ_per_m_squared",
            "Macro Aggregates STD %": "macroAggregatesPercentStd",
            "H2O Stable Aggregates STD %": "waterStableAggregatesPercentStd",
            "Near-Infrared C STD gC/kg": "nearInfraredCarbonSd_gC_per_kg",
        }
    elif sheet_name == "MeasSoilChem":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Date": "date",
            "Treatment ID": "treatmentId",
            "Upper cm": "upperDepth_cm",
            "Lower cm": "lowerDepth_cm",
            "pH": "soilPh",
            "TSC gC/kg": "totalSoilCarbon_gC_per_kg",
            "TSN gN/kg": "totalSoilNitrogen_gN_per_kg",
            "Inorganic C gC/kg": "inorganicCarbon_gC_per_kg",
            "Organic C gC/kg": "organicCarbon_gC_per_kg",
            "Mineral C gC/kg": "mineralCarbon_gC_per_kg",
            "CEC cmol/kg": "cationExchangeCapacity_cmol_per_kg",
            "Electric Conduc siemens/m": "electricalConductivity_siemens_per_m",
            "Soluble C mgC/kg": "solubleOrganicCarbon_mgC_per_kg",
            "NH4 mgN/kg": "ammonium_mgN_per_kg",
            "NO3 mgN/kg": "nitrate_mgN_per_kg",
            "P mgP/kg": "phosphorus_mgP_per_kg",
            "K mgK/kg": "potassium_mgK_per_kg",
            "Ca mgCa/kg": "extractableCalcium_mgCa_per_kg",
            "Mg mgMg/kg": "extractableMagnesium_mgMg_per_kg",
            "Cu mgCu/kg": "extractableCopper_mgCu_per_kg",
            "Fe mgFe/kg": "extractableIron_mgFe_per_kg",
            "Mn mgMN/kg": "extractableManganese_mgMN_per_kg",
            "Zn mgZn/kg": "extractableZinc_mgZn_per_kg",
            "Mineralizable N gN/kg": "mineralizableNitrogen_gN_per_kg",
            "Nitrite mgN/kg": "nitrites_mgN_per_kg",
            "pH STD": "soilPhStd",
            "TSC STD gC/kg": "totalSoilCarbonSd_gC_per_kg",
            "TSN STD gN/kg": "totalSoilNitrogenSd_gN_per_kg",
            "Inorganic C STD gC/kg": "inorganicCarbonSd_gC_per_kg",
            "Organic STD gC/kg": "organicCarbonSd_gC_per_kg",
            "Mineral C STD gC/kg": "mineralCarbonSd_gC_per_kg",
            "CEC STD cmol/kg": "cationExchangeCapacitySd_cmol_per_kg",
            'Electric Conduc STD siemens/m': 'electricalConductivitySd_siemens_per_m',
            'Soluble C STD mgC/kg': 'solubleOrganicCarbonSd_mgC_per_kg',
            'NH4 STD mgN/kg': 'ammoniumSd_mgN_per_kg',
            'NO3 STD mgN/kg': 'nitrateSd_mgN_per_kg',
            'P STD mgP/kg': 'phosphorusSd_mgP_per_kg',
            'K STD mgK/kg': 'potassiumSd_mgK_per_kg',
            'Ca STD mgCa/kg': 'extractableCalciumSd_mgCa_per_kg',
            'Mg STD mgMg/kg': 'extractableMagnesiumSd_mgMg_per_kg',
            'Cu STD mgCu/kg': 'extractableCopperSd_mgCu_per_kg',
            'Fe STD mgFe/kg': 'extractableIronSd_mgFe_per_kg',
            'Mn STD mgMN/kg': 'extractableManganeseSd_mgMN_per_kg',
            'Zn STD mgZn/kg': 'extractableZincSd_mgZn_per_kg',
            'Mineralizable N STD gN/kg': 'mineralizableNitrogenSd_gN_per_kg',
            'Nitrite STD mgN/kg': 'nitritesSd_mgN_per_kg',
        }
    elif sheet_name == "MeasSoilBiol":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Date": "date",
            "Treatment ID": "treatmentId",
            "Upper cm": "upperDepth_cm",
            "Lower cm": "lowerDepth_cm",
            "Glucosidase mg/kg/hr": "glucosidase_mg_per_kg_per_hr",
            "Glucosaminidase mg/kg/hr": "glucosaminidase_mg_per_kg_per_hr",
            "Acid Phosphatase mg/kg/hr": "acidPhosphatase_mg_per_kg_per_hr",
            "Alk Phosphatase mg/kg/hr": "alkPhosphatase_mg_per_kg_per_hr",
            "Fluorescein Diacetate Hydrol mg/kg/hr": "soilfluoresceinDiacetateHydrol_mg_per_kg_per_hr",
            "Glomalin g/kg": "glomalin_g_per_kg",
            "FAME": "fattyAcidMethylEsters",
            "PLFA": "phospholipidFattyAcids",
            "DNA": "soilDna",
            "Iden Plant Material gC/kg": "organicPlantMaterial_gC_per_kg",
            "POM gC/kg": "particulateOrganicMatter_gC_per_kg",
            "Microbe Bio C mgC/kg": "carbonMicrobialBiomass_mgC_per_kg",
            "Microbe Bio N mgN/kg": "nitrogenMicrobialBiomass_mgN_per_kg",
            "Glucosidase STD mg/kg/hr": "glucosidaseSd_mg_per_kg_per_hr",
            "Glucosaminidase STD mg/kg/hr": "glucosaminidaseSd_mg_per_kg_per_hr",
            "Acid Phosphatase STD mg/kg/hr": "acidPhosphataseSd_mg_per_kg_per_hr",
            "Alk Phosphatase STD mg/kg/hr": "alkPhosphataseSd_mg_per_kg_per_hr",
            "Fluorescein Diacetate Hydrol STD mg/kg/hr": "soilfluoresceinDiacetateHydrolSd_mg_per_kg_per_hr",
            "Glomalin STD g/kg": "glomalinSd_g_per_kg",
            "Iden Plant Material STD gC/kg": "organicPlantMaterialSd_gC_per_kg",
            'POM STD gC/kg': 'particulateOrganicMatterSd_gC_per_kg',
            'Microbe Bio C STD mgC/kg': 'carbonMicrobialBiomassSd_mgC_per_kg',
            'Microbe Bio N STD mgN/kg': 'nitrogenMicrobialBiomassSd_mgN_per_kg',
        }
    elif sheet_name == "MeasSoilCover":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Treatment ID": "treatmentId",
            "Crop": "crop",
            "Soil w/ Residue %": "soilWithResidueCoverPercent",
            "Date": "date",
            "Timing Descriptor": "soilCoverTimingDescriptor",
        }
    elif sheet_name == "MeasGHGFlux":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Date": "date",
            "Time": "time",
            "Treatment ID": "treatmentId",
            "Crop": "crop",
            "Chamber Placement": "chamberPlacement",
            "N2O gN/ha/d": "nitrousOxide_gN_per_ha_per_d",
            "N2O Interp=0 Obs=1": "isNitrousOxideInterpolated",
            "CO2 gC/ha/d": "carbonDioxide_gC_per_ha_per_d",
            "CO2 Interp=0 Obs=1": "isCarbonDioxideInterpolated",
            "CH4 gC/ha/d": "methane_gC_per_ha_per_d",
            "CH4 Interp=0 Obs=1": "isMethaneInterpolated",
            "Air Temp degC": "airTemperature_degC",
            "Soil Temp degC": "soilTemperature_degC",
            "Soil Moisture % vol": "soilMoisture_percent_volume",
            "Soil Moisture Depth cm": "soilMoistureDepth_cm",
            "N2O STD gN/ha/d": "nitrousOxideSd_gN_per_ha_per_d",
            "CO2 STD gC/ha/d": "carbonDioxideSd_gC_per_ha_per_d",
            "CH4 STD gC/ha/d": "methaneSd_gC_per_ha_per_d",
            "Air Temp STD degC": "airTemperatureSd_degC",
            "Soil Temp STD degC": "soilTemperatureSd_degC",
            "Soil Moisture STD % vol": "soilMoistureSd_percent_volume",
        }
    elif sheet_name == "MeasResidueMgnt":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Date": "date",
            "Treatment ID": "treatmentId",
            "Growth Stage": "growthStage",
            "Crop": "crop",
            "Harvested Frac": "harvestedFrac",
            "Corn Ear Height cm": "cornEarHeight_cm",
            "Above G Biomass kg/ha": "aboveGroundBiomass_kg_per_ha",
            "Unit Grain Weight mg": "unitGrainWeight_mg",
            "Grain Dry Matt kg/ha": "grainYield_kg_per_ha",
            "Grain Moist %": "grainMoisturePercent",
            "Grain C kgC/ha": "grainCarbon_kgC_per_ha",
            "Grain N kgN/ha": "grainNitrogen_kgN_per_ha",
            "Harv NonGrain Bio kg/ha": "driedHarvestedResidue_kg_per_ha",
            "Harv Res Moist %": "harvestedResidueMoisturePercent",
            "Harv Res C kgC/ha": "harvestedResidueCarbon_kgC_per_ha",
            "Harv Res N kgN/ha": "harvestedResidueNitrogen_kgN_per_ha",
            "NonHarv NonGrain Bio kg/ha": "nonHarvestedResidueMass_kg_per_ha",
            "NonHarv Res Moist %": "nonHarvestedResidueMoisturePercent",
            "NonHarv Res C kgC/ha": "nonHarvestedResidueCarbonContent_kgC_per_ha",
            "NonHarv Res N kgN/ha": "nonHarvestedResidueNitrogenContent_kgN_per_ha",
            "Root Dry Matt kg/ha": "rootDryMatter_kg_per_ha",
            "Root Moist %": "rootMoisturePercent",
            "Root C kgC/ha": "rootCarbonContent_kgC_per_ha",
            "Root N kgN/ha": "rootNitrogenContent_kgN_per_ha",
            "Corn Ear Height STD cm": "cornEarHeightSd_cm",
            "Above G Biomass STD kg/ha": "aboveGroundBiomassSd_kg_per_ha",
            "Unit Grain Weight STD mg": "unitGrainWeightSd_mg",
            "Grain Dry Matt STD kg/ha": "grainYieldSd_kg_per_ha",
            "Grain Moist STD %": "grainMoisturePercentStd",
            "Grain C STD kgC/ha": "grainCarbonSd_kgC_per_ha",
            "Grain N STD kgN/ha": "grainNitrogenSd_kgN_per_ha",
            "Harv NonGrain Bio STD kg/ha": "driedHarvestedResidueSd_kg_per_ha",
            "Harv Res Moist STD %": "harvestedResidueMoisturePercentStd",
            "Harv Res C STD kgC/ha": "harvestedResidueCarbonSd_kgC_per_ha",
            "Harv Res N STD kgN/ha": "harvestedResidueNitrogenSd_kgN_per_ha",
            "NonHarv NonGrain Bio STD kg/ha": "nonHarvestedResidueMassSd_kg_per_ha",
            "NonHarv Res Moist STD %": "nonHarvestedResidueMoisturePercentStd",
            "NonHarv Res C STD kgC/ha": "nonHarvestedResidueCarbonContentSd_kgC_per_ha",
            "NonHarv Res N STD kgN/ha": "nonHarvestedResidueNitrogenContentSd_kgN_per_ha",
            "Root Dry Matt STD kg/ha": "rootDryMatterSd_kg_per_ha",
            "Root Moist STD %": "rootMoisturePercentStd",
            "Root C STD kgC/ha": "rootCarbonContentSd_kgC_per_ha",
            "Root N STD kgN/ha": "rootNitrogenContentSd_kgN_per_ha",
        }
    elif sheet_name == "MeasHarvestFraction":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Sampling Date": "date",
            "Treatment ID": "treatmentId",
            "Growth Stage": "growthStage",
            "Crop": "crop",
            "Plant Fraction": "plantFraction",
            "Frac Dry Matt kg/ha": "dryBiomass_kg_per_ha",
            "Frac Moist %": "moisturePercent",
            "Frac C kgC/ha": "carbon_kgC_per_ha",
            "Frac N kgN/ha": "nitrogen_kgN_per_ha",
            "Grain Weight mg/kernel": "grainWeight_mg_per_kernel",
            "Frac Dry Matt STD kg/ha": "dryBiomassSd_kg_per_ha",
            "Frac Moist STD %": "moisturePercentStd",
            "Frac C STD kgC/ha": "carbonSd_kgC_per_ha",
            "Frac N STD kgN/ha": "nitrogenSd_kgN_per_ha",
            "Grain Weight STD mg/kernel": "grainWeightSd_mg_per_lernel",
        }
    elif sheet_name == "MeasBiomassCHO":
        mapping = {
            "Date": "date",
            'Plant Fraction': 'plantFraction',
            'Growth Stage': 'growthStage',
            'Crop': 'crop',
            'Exp Unit ID': 'expUnitId',
            'Treatment ID': 'treatmentId',
            "Glucan g/kg": "glucan_g_per_kg",
            "Xylan g/kg": "xylan_g_per_kg",
            "Galactan g/kg": "galactan_g_per_kg",
            "Arabinan g/kg": "arabinan_g_per_kg",
            "Mannan g/kg": "mannan_g_per_kg",
            "Lignin g/kg": "lignin_g_per_kg",
            "Neutral Det Fiber g/kg": "neutralDetFiber_g_per_kg",
            "Acid Det Fiber g/kg": "acidDetFiber_g_per_kg",
            "Acid Soluble Lignin g/kg": "acidSolubleLignin_g_per_kg",
            "Acid Insoluble Lignin g/kg": "acidInsolubleLignin_g_per_kg",
            "Crude Protein g/kg": "crudeProtein_g_per_kg",
            "Non-fiber Carbs g/kg": "nonFiberCarbs_g_per_kg",
            "Ash g/kg": "ash_g_per_kg",
            "Glucan STD g/kg": "glucanSd_g_per_kg",
            "Xylan STD g/kg": "xylanSd_g_per_kg",
            "Galactan STD g/kg": "galactanSd_g_per_kg",
            "Arabinan STD g/kg": "arabinanSd_g_per_kg",
            "Mannan STD g/kg": "mannanSd_g_per_kg",
            "Lignin STD g/kg": "ligninSd_g_per_kg",
            "Neutral Det Fiber STD g/kg": "neutralDetFiberSd_g_per_kg",
            "Acid Det Fiber STD g/kg": "acidDetFiberSd_g_per_kg",
            "Acid Soluble Lignin STD g/kg": "acidSolubleLigninSd_g_per_kg",
            "Acid Insoluble Lignin STD g/kg": "acidInsolubleLigninSd_g_per_kg",
            "Crude Protein STD g/kg": "crudeProteinSd_g_per_kg",
            "Non-fiber Carbs STD g/kg": "nonFiberCarbsSd_g_per_kg",
            "Ash STD g/kg": "ashSd_g_per_kg",
        }
    elif sheet_name == "MeasBiomassEnergy":
        mapping = {
            'Exp Unit ID': 'expUnitId',
            'Date': 'date',
            'Treatment ID': 'treatmentId',
            'Growth Stage': 'growthStage',
            'Crop': 'crop',
            'Plant Fraction': 'plantFraction',
            "Ash STD g/kg": "mineralMatterSd_g_per_kg",
            'Volatile Matter g/kg': 'volatileMatter_g_per_kg',
            'Mineral Matter g/kg': 'mineralMatter_g_per_kg',
            'Gross Calorific Value MJ/kg': 'grossCalorificValue_MJ_per_kg',
            'Volatile Matter STD g/kg': 'volatileMatterSd_g_per_kg',
            'Gross Calorific Value STD MJ/kg': 'grossCalorificValueSd_MJ_per_kg',
        }
    elif sheet_name == "MeasBiomassMinAn":
        mapping = {
            'Exp Unit ID': 'expUnitId',
            'Date': 'date',
            'Treatment ID': 'treatmentId',
            'Growth Stage': 'growthStage',
            'Crop': 'crop',
            'Plant Fraction': 'plantFraction',
            "C Concentration g/kg": "carbonConcentration_g_per_kg",
            "N Concentration g/kg": "nitrogenConcentration_g_per_kg",
            "P Concentration g/kg": "phosphorusConcentration_g_per_kg",
            "K Concentration g/kg": "potassiumConcentration_g_per_kg",
            "Ca Concentration g/kg": "calciumConcentration_g_per_kg",
            "Mg Concentration g/kg": "magnesiumConcentration_g_per_kg",
            "S Concentration g/kg": "sulfurConcentration_g_per_kg",
            "Na Concentration g/kg": "sodiumConcentration_g_per_kg",
            "Cl Concentration g/kg": "chlorineConcentration_g_per_kg",
            "Al Concentration mg/kg": "aluminumConcentration_mg_per_kg",
            "B Concentration mg/kg": "boronConcentration_mg_per_kg",
            "Cu Concentration mg/kg": "copperConcentration_mg_per_kg",
            "Fe Concentration mg/kg": "ironConcentration_mg_per_kg",
            "Mn Concentration mg/kg": "manganeseConcentration_mg_per_kg",
            "Zn Concentration mg/kg": "zincConcentration_mg_per_kg",
            "C Concentration STD g/kg": "carbonConcentrationSd_g_per_kg",
            "N Concentration STD g/kg": "nitrogenConcentrationSd_g_per_kg",
            "P Concentration STD g/kg": "phosphorusConcentrationSd_g_per_kg",
            "K Concentration STD g/kg": "potassiumConcentrationSd_g_per_kg",
            "Ca Concentration STD g/kg": "calciumConcentrationSd_g_per_kg",
            "Mg Concentration STD g/kg": "magnesiumConcentrationSd_g_per_kg",
            "S Concentration  STD g/kg": "sulfurConcentrationSd_g_per_kg",
            "Na Concentration STD g/kg": "sodiumConcentrationSd_g_per_kg",
            "Cl Concentration STD g/kg": "chlorineConcentrationSd_g_per_kg",
            "Al Concentration STD mg/kg": "aluminumConcentrationSd_mg_per_kg",
            "B Concentration STD mg/kg": "boronConcentrationSd_mg_per_kg",
            "Cu Concentration STD mg/kg": "copperConcentrationSd_mg_per_kg",
            "Fe Concentration STD mg/kg": "ironConcentrationSd_mg_per_kg",
            "Mn Concentration STD mg/kg": "manganeseConcentrationSd_mg_per_kg",
            "Zn Concentration STD mg/kg": "zincConcentrationSd_mg_per_kg",
        }
    elif sheet_name == "MeasGrazingPlants":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Date": "date",
            "Treatment ID": "treatmentId",
            "Species Mix": "speciesMix",
            "Growth Stage": "growthStage",
            "Broadleaf vs Grass": "broadleafOrGrass",
            "AboveGr Bio kg/ha (dry)": "aboveGroundBiomassDry_kg_per_ha",
            "Surface Litter kg/ha (dry)": "aurfaceLitterDry_kg_per_ha",
            "Standing Dead kg/ha (dry)": "atandingDeadDry_kg_per_ha",
            "LAI kg/ha (dry)": "leafAreaIndexDry_kg_per_ha",
            "Biomass N %": "biomassNitrogenPercentage",
            "Lignin %": "ligninPercentage",
            "Ground Cover %": "groundCoverPercentage",
            "AboveGr Bio C kgC/ha": "aboveGroundBiomassCarbon_kgC_per_ha",
            "AboveGr Bio N kgN/ha": "aboveGroundBiomassNitrogen_kgN_per_ha",
            "BelowGr Bio C kgC/ha": "belowGroundBiomassCarbon_kgC_per_ha",
            "BelowGr Bio N kgN/ha": "belowGroundBiomassNitrogen_kgN_per_ha",
            "ANPP C kgC/ha/yr": "abovegroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr",
            "ANPP N kgN/ha/yr": "abovegroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr",
            "BNPP C kgC/ha/yr": "belowgroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr",
            "BNPP N kgN/ha/yr": "belowgroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr",
            "AboveGr Bio kg/ha (dry).1": "aboveGroundBiomassDrySd_kg_per_ha",
            "Surface Litter STD kg/ha (dry)": "aurfaceLitterDrySd_kg_per_ha",
            "Standing Dead STD kg/ha (dry)": "atandingDeadDrySd_kg_per_ha",
            "LAI STD kg/ha": "leafAreaIndexDrySd_kg_per_ha",
            "Biomass N STD %": "biomassNitrogenPercentageStd",
            "Lignin STD %": "ligninPercentageStd",
            "Ground Cover STD %": "groundCoverPercentageStd",
            "AboveGr Bio C STD kgC/ha": "aboveGroundBiomassCarbonSd_kgC_per_ha",
            "AboveGr Bio N STD kgN/ha": "aboveGroundBiomassNitrogenSd_kgN_per_ha",
            "BelowGr Bio C STD kgC/ha": "belowGroundBiomassCarbonSd_kgC_per_ha",
            "BelowGr Bio N STD kgN/ha": "belowGroundBiomassNitrogenSd_kgN_per_ha",
            "ANPP C STD kgC/ha/yr": "abovegroundNetPrimaryProductivityCarbonSd_kgC_per_ha_per_yr",
            "ANPP N STD kgN/ha/yr": "abovegroundNetPrimaryProductivityNitrogenSd_kgN_per_ha_per_yr",
            "BNPP C STD kgC/ha/yr": "belowgroundNetPrimaryProductivityCarbonSd_kgC_per_ha_per_yr",
            "BNPP N STD kgN/ha/yr": "belowgroundNetPrimaryProductivityNitrogenSd_kgN_per_ha_per_yr",
        }
    elif sheet_name == "MeasSuppRes":
        mapping = {
            "Exp Unit ID": "expUnitId",
            "Treatment ID": "treatmentId",
            "Date": "miscellaneousMeasurementDate",
            "What is Measured": "miscellaneousMeasurementDescription",
            "Measurement Value": "miscellaneousMeasurementValue",
            "Measurement Units": "miscellaneousMeasurementUnits",
        }
    else :
        # print("could not find sheet name in constants.py")
        # print("")
        mapping = {}

    return mapping.get(column, None)


def create_mappings(directory_path: str, mappings: dict = {}) -> dict:
    
    raw_path = repr(directory_path).replace("'", "")

    
    # ----------entities------------- 

    '''
    
    entity_struct = {
        '@fileName': r'csvfile',
        '@uniqueId':'identifier',
        'dataProperty':'dataProperty',
    }
    mappings['Entity'] = entity_struct
    
    '''
    #39 total classes
    #Overview

    version_struct = {
        '@fileName': 'kg/version.csv',
        '@uniqueId': 'versionDate',
        'versionDate': 'versionDate',
    }
    mappings['Version'] = version_struct

    experiment_struct = {
        '@fileName': raw_path + r'/overview.csv',
        '@uniqueId': 'experimentName',
        'experimentName': 'experimentName',
        'startDate': 'startDate',
        'endDate': 'endDate',  
        'durationOfStudy': 'durationOfStudy',
        'projectName': 'projectName',
    }
    mappings['Experiment'] = experiment_struct

    organization_struct = {
        '@fileName': raw_path + r'/overview.csv',
        '@uniqueId': 'organizationName',
        'organizationName': 'organizationName',
    }
    mappings['Organization'] = organization_struct

    project_struct = {
        '@fileName': raw_path + r'/overview.csv',
        '@uniqueId': 'projectName',
        'projectName': 'projectName',
    }
    mappings['Project'] = project_struct

    research_unit_struct = { 
        '@fileName': raw_path + r'/overview.csv',
        '@uniqueId': 'researchUnitDescription',
        'researchUnitDescription': 'researchUnitDescription',
    }
    mappings['ResearchUnit'] = research_unit_struct


    site_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@uniqueId': 'siteId',
        'siteId': 'siteId',
        'majorLandResourceArea': 'majorLandResourceArea',
        'siteHistory':'siteHistory',
        'postalCodeNumber':'postalCodeNumber',
        'siteMeanAnnualPrecipitation_mm': 'siteMeanAnnualPrecipitation_mm',
        'siteMeanAnnualTemperature_degC': 'siteMeanAnnualTemperature_degC',
        'siteNativeVegetation': 'siteNativeVegetation',
        'siteSpatialDescription': 'siteSpatialDescription',
        'siteIdDescriptor': 'siteIdDescriptor'
    }

    mappings['Site'] = site_struct
    # FieldSites

    city_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@uniqueId': 'cityName',
        'cityName': 'cityName',
    }
    mappings['City'] = city_struct

    county_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@uniqueId': 'countyName',
        'countyName': 'countyName',
    }
    mappings['County'] = county_struct

    field_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@uniqueId': 'fieldId',
        'fieldId': 'fieldId',
        'elevation_m': 'elevation_m',
        'latitude_decimal_deg': 'latitude_decimal_deg',
        'longitude_decimal_deg': 'longitude_decimal_deg',
    }
    mappings['Field'] = field_struct

    state_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@uniqueId': 'stateProvince',
        'stateProvince': 'stateProvince',
    }
    mappings['State'] = state_struct

    country_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@uniqueId': 'countryName',
        'countryName': 'countryName',
    }
    mappings['Country'] = country_struct

    #Persons

    person_struct = {
        '@fileName': raw_path + r'/persons_with_UID.csv',
        '@uniqueId': 'persons_UID',
        'email': 'email',
        'firstName': 'firstName',
        'isPrimaryContact': 'isPrimaryContact',
        'lastName': 'lastName',
        'middleName': 'middleName',
        'note': 'note',
        'website': 'website',
        'phoneNumber': 'phoneNumber',
        'profession': 'profession',
        'roleInStudy': 'roleInStudy',
        'suffix': 'suffix',
        'persons_UID': 'persons_UID',
        'organizationName': 'organizationName',
    }
    mappings['Person'] = person_struct

    department_struct = {
        '@fileName': raw_path + r'/persons_with_UID.csv',
        '@uniqueId': 'departmentName',
        'departmentName': 'departmentName',
    }
    mappings['Department'] = department_struct

    #Citations

    publication_struct = {
    '@fileName': raw_path + r'/citations.csv',
    '@uniqueId': 'identifier',
    'title': 'title',
    'citationType': 'citationType',
    'publicationDate': 'publicationDate',
    'description': 'description',
    'citation': 'citation',
    'identifier': 'identifier',
    'author': 'author',
    'correspondingAuthor': 'correspondingAuthor'
    }

    mappings['Publication'] = publication_struct

    book_chapter_struct = {
        '@fileName': raw_path + r'/citations.csv',
        '@uniqueId': 'bookName',
        'bookName': 'bookName',
    }
    mappings['Book'] = book_chapter_struct    

    #Treatments

    treatment_struct = {
        '@fileName': raw_path + r'/treatments.csv',
        '@uniqueId': 'treatmentId',
        'treatmentDescriptor': 'treatmentDescriptor',
        'residueRemoval': 'residueRemoval',
        'organicManagement': 'organicManagement',
        'projectScenario': 'projectScenario',
        'nitrogenTreatmentDescriptor': 'nitrogenTreatmentDescriptor',
        'grazingRate': 'grazingRate',
        'irrigation': 'irrigation',
        'coverCrop': 'coverCrop',
        'fertilizerAmendmentClass': 'fertilizerAmendmentClass',
        'tillageDescriptor': 'tillageDescriptor',
        'tileDrainage': 'tileDrainage',
        'treatmentId': 'treatmentId',
    }
    mappings['Treatment'] = treatment_struct

    rotation_struct = {
        '@fileName': raw_path + r'/treatments.csv',
        '@uniqueId': 'rotationDescriptor',
        'rotationDescriptor': 'rotationDescriptor',
    }
    mappings['Rotation'] = rotation_struct

    tillage_struct = {
        '@fileName': raw_path + r'/management_tillage_with_UID.csv',
        '@uniqueId': 'mgtTillage_UID',
        'startDate': 'startDate',
        'endDate': 'endDate',
        'tillageEvent': 'tillageEvent',
        'tillageEventDepth_cm': 'tillageEventDepth_cm',
        'tillageEventMethod': 'tillageEventMethod',
        'mgtTillage_UID': 'mgtTillage_UID',
    }
    mappings['Tillage'] = tillage_struct
    #here

    #ExperUnits

    experimental_unit_struct = {
        '@fileName': raw_path + r'/experimental_units_with_UID.csv',
        '@uniqueId': 'expUnit_UID',
        'expUnitId': 'expUnitId',
        'changeInManagement': 'changeInManagement', ###
        'landscapePosition': 'landscapePosition',
        'expUnitSize_m_squared': 'expUnitSize_m_squared',
        'fieldSlopePercent': 'fieldSlopePercent',
        'expUnit_UID': 'expUnit_UID', # do we need this?
        'startDate': 'startDate',
        'endDate': 'endDate',
    }
    mappings['ExperimentalUnit'] = experimental_unit_struct

    soil_struct = {
        '@fileName': raw_path + r'/experimental_units_with_UID.csv',
        '@uniqueId': 'soilClassification',
        'soilSeries': 'soilSeries',
        'soilClassification': 'soilClassification',
    }
    mappings['Soil'] = soil_struct

    #WeatherStation
    weather_station_struct = {
        '@fileName': raw_path + r'/weather_station.csv',
        '@uniqueId': 'weatherStationId',
        'weatherStationId': 'weatherStationId',
        'date': 'date',
        'weatherStationDistanceFromField_m': 'weatherStationDistanceFromField_m',
        'weatherStationDirectionFromField': 'weatherStationDirectionFromField',
        'weatherStationUrl': 'weatherStationUrl',
        'weatherStationlatitude_decimal_deg': 'weatherStationlatitude_decimal_deg',
        'weatherStationlongitude_decimal_deg': 'weatherStationlongitude_decimal_deg',
        'elevation_m': 'elevation_m',
    }
    if 'AgCros' in directory_path:
        weather_station_struct['@fileName'] = raw_path + r'/weather_daily_with_UID.csv'
    mappings['WeatherStation'] = weather_station_struct
    #WeatherDaily

    weather_observation_struct = {
        '@fileName': raw_path + r'/weather_daily_with_UID.csv',
        '@uniqueId': 'weatherDaily_UID',
        'weatherDaily_UID': 'weatherDaily_UID',
        'weatherStationId': 'weatherStationId',
        'date': 'date',
        'weatherStationId': 'weatherStationId',
        'tempMax_degC': 'tempMax_degC',
        'tempMin_degC': 'tempMin_degC',
        'precipitation_mm_per_d': 'precipitation_mm_per_d',
        'weatherBadValueFlag': 'weatherBadValueFlag',
        'relativeHumidityPercent': 'relativeHumidityPercent',
        'dewPointDegc': 'dewPointDegc',
        'windSpeed_m_per_s': 'windSpeed_m_per_s',
        'solarRadiationVegetatedGround_MJ_per_m_squared_per_d': 'solarRadiationVegetatedGround_MJ_per_m_squared_per_d',
        'solarRadiationBareSoil_MJ_per_m_squared_per_d': 'solarRadiationBareSoil_MJ_per_m_squared_per_d',
        'soilTemp5cm_degC': 'soilTemp5cm_degC',
        'soilTemp10cm_degC': 'soilTemp10cm_degC',
        'windDirectionDegFromNorth': 'windDirectionDegFromNorth',
        'openPanEvaporation_mm_per_d': 'openPanEvaporation_mm_per_d',
        'closedPanEvaporation_mm_per_d': 'closedPanEvaporation_mm_per_d',
        'atmosphericNitrogenDeposition_kg_per_ha_per_d': 'atmosphericNitrogenDeposition_kg_per_ha_per_d',
        'totalSolarRadiationBareSoil_MJ_per_m_squared_per_d': 'totalSolarRadiationBareSoil_MJ_per_m_squared_per_d',
        'snow_mm_per_d': 'snow_mm_per_d'
    }
    mappings['WeatherObservation'] = weather_observation_struct

    #MgtAmendments

    amendment_struct = {
        '@fileName': raw_path + r'/management_amendments_with_UID.csv',
        '@uniqueId': 'mgtAmendments_UID',
        'mgtAmendments_UID': 'mgtAmendments_UID',
        'irrigationNitrogen_mg_per_L': 'irrigationNitrogen_mg_per_L',
        'crop': 'crop',
        'treatmentId': 'treatmentId',
        'startDate': 'startDate',
        'endDate': 'endDate',
        'amendmentDepth_cm': 'amendmentDepth_cm',
        'irrigationAmount_cm': 'irrigationAmount_cm',
        'irrigationType': 'irrigationType',
        'amendmentPlacement': 'amendmentPlacement',
        'totalNitrogenAmount_kgN_per_ha': 'totalNitrogenAmount_kgN_per_ha',
        'totalPhosphorusAmount_kgP_per_ha': 'totalPhosphorusAmount_kgP_per_ha',
        'totalPotassiumAmount_kgK_per_ha': 'totalPotassiumAmount_kgK_per_ha',
        'type': 'type',
        'totalAmendmentAmount_kg_per_ha': 'totalAmendmentAmount_kg_per_ha',
    }
    mappings['Amendment'] = amendment_struct

    pesticide_struct = {
        '@fileName': raw_path + r'/management_amendments_with_UID.csv',
        '@uniqueId': 'pesticide_UID',
        'pesticideActiveIngredientType': 'pesticideActiveIngredientType',
        'pesticidePlacement': 'pesticidePlacement',
        'pesticideTarget': 'pesticideTarget',
        'totalPesticideAmount_kg_per_ha': 'totalPesticideAmount_kg_per_ha',
        'pesticide_UID': 'pesticide_UID',
    }
    mappings['Pesticide'] = pesticide_struct

    #MgtPlanting

    planting_event_struct = {
        '@fileName': raw_path + r'/management_planting_with_UID.csv',
        '@uniqueId': 'mgtPlanting_UID',
        'mgtPlanting_UID': 'mgtPlanting_UID',
        'expUnitId': 'expUnitId',
        'startDate': 'startDate',
        'endDate': 'endDate',
        'treatmentId': 'treatmentId',
        'crop': 'crop',
        'cultivar': 'cultivar',
        'rowWidth_cm': 'rowWidth_cm',
        'depth_cm': 'depth_cm',
        'plantingMethod': 'plantingMethod',
        'plantingDensity_kg_per_ha': 'plantingDensity_kg_per_ha',
        'plantingRate_number_seeds_per_ha': 'plantingRate_number_seeds_per_ha',
    }
    mappings['PlantingEvent'] = planting_event_struct

    #MgtGrowthStages
    Crop_Growth_Stage_struct = {
        '@fileName': raw_path + r'/management_growth_stages_with_UID.csv',
        '@uniqueId': 'mgtGrowthStages_UID',
        'mgtGrowthStages_UID': 'mgtGrowthStages_UID',
        'date': 'date',
        'growthStage': 'growthStage',
        'crop': 'crop',
        'treatmentId': 'treatmentId',
    }
    mappings['CropGrowthStage'] = Crop_Growth_Stage_struct

    #MgtResidue

    Residue_Management_Event_struct = {
        '@fileName': raw_path + r'/management_residue_with_UID.csv',
        '@uniqueId': 'mgtResidue_UID',
        'mgtResidue_UID': 'mgtResidue_UID',
        'crop': 'crop',
        'treatmentId': 'treatmentId',
        'equipmentType': 'equipmentType',
        'residueCuttingHeight': 'residueCuttingHeight', #Multiple ranges?
        'rowsHarvestedPercent': 'rowsHarvestedPercent',
        'perennialStandAge_years': 'perennialStandAge_years',
        'stageAtHarvest': 'stageAtHarvest',
        'date': 'date',
    }
    mappings['ResidueManagementEvent'] = Residue_Management_Event_struct

    #MgtGrazing

    Grazing_Management_Event_struct = {
        '@fileName': raw_path + r'/management_grazing_with_UID.csv',
        '@uniqueId': 'mgtGrazing_UID',
        'mgtGrazing_UID': 'mgtGrazing_UID',
        'startDate': 'startDate',
        'endDate': 'endDate',
        'treatmentId': 'treatmentId',
        'stockingRate_number_animals_per_ha': 'stockingRate_number_animals_per_ha',
        'animalSpecies': 'animalSpecies',
        'animalClass': 'animalClass',
        'otherEvents': 'otherEvents',
        'yearsBetweenBurns': 'yearsBetweenBurns',
        'burnIntensity': 'burnIntensity',
    }
    mappings['GrazingManagementEvent'] = Grazing_Management_Event_struct


    #MeasSoilPhys 

    soil_physical_sample_struct = {
        '@fileName': raw_path + r'/measurements_soil_physical_with_UID.csv',
        '@uniqueId': 'measSoilPhys_UID',
        'measSoilPhys_UID': 'measSoilPhys_UID',
        'date': 'date',
        'treatmentId': 'treatmentId',
        'upperDepth_cm': 'upperDepth_cm',
        'lowerDepth_cm': 'lowerDepth_cm',
        'sandPercent': 'sandPercent',
        'siltPercent': 'siltPercent',
        'clayPercent': 'clayPercent',
        'bulkDensity_g_per_cm_cubed': 'bulkDensity_g_per_cm_cubed',
        'wiltingPoint_percent_volume': 'wiltingPoint_percent_volume',
        'fieldCapacity_percent_volume': 'fieldCapacity_percent_volume',
        'saturatedHydraulicConductivity_cm_per_sec': 'saturatedHydraulicConductivity_cm_per_sec',
        'moistureReleaseCurve': 'moistureReleaseCurve',
        'soilHeatFlux_MJ_per_m_squared': 'soilHeatFlux_MJ_per_m_squared',
        'aggregationPercent': 'aggregationPercent',
        'waterStableAggregatePercent': 'waterStableAggregatePercent',
        'nearInfraredCarbon_gC_per_kg': 'nearInfraredCarbon_gC_per_kg',
        'bulkDensitySd_g_per_cm_cubed': 'bulkDensitySd_g_per_cm_cubed',
        'wiltingPointSd_percent_volume': 'wiltingPointSd_percent_volume',
        'fieldCapacitySd_percent_volume': 'fieldCapacitySd_percent_volume',
        'saturatedHydraulicConductivitySd_cm_per_sec': 'saturatedHydraulicConductivitySd_cm_per_sec',
        'soilHeatFluxSd_MJ_per_m_squared': 'soilHeatFluxSd_MJ_per_m_squared',
        'macroAggregatesPercentStd': 'macroAggregatesPercentStd',
        'waterStableAggregatesPercentStd': 'waterStableAggregatesPercentStd',
        'nearInfraredCarbonSd_gC_per_kg': 'nearInfraredCarbonSd_gC_per_kg',

    }
    mappings['SoilPhysicalSample'] = soil_physical_sample_struct
    
    # MeasSoilChem
    soil_chemical_sample_struct = {
        '@fileName': raw_path + r'/measurements_soil_chemical_with_UID.csv',
        '@uniqueId': 'measSoilChem_UID',
        'measSoilChem_UID': 'measSoilChem_UID',
        'date': 'date',
        'upperDepth_cm': 'upperDepth_cm',
        'lowerDepth_cm': 'lowerDepth_cm',
        'ph': 'ph',
        'treatmentId': 'treatmentId',
        'totalSoilCarbon_gC_per_kg': 'totalSoilCarbon_gC_per_kg',
        'totalSoilNitrogen_gN_per_kg': 'totalSoilNitrogen_gN_per_kg',
        'inorganicCarbon_gC_per_kg': 'inorganicCarbon_gC_per_kg',
        'organicCarbon_gC_per_kg': 'organicCarbon_gC_per_kg',
        'mineralCarbon_gC_per_kg': 'mineralCarbon_gC_per_kg',
        'cationExchangeCapacity_cmol_per_kg': 'cationExchangeCapacity_cmol_per_kg',
        'electricalConductivity_siemens_per_m': 'electricalConductivity_siemens_per_m',
        'solubleOrganicCarbon_mgC_per_kg': 'solubleOrganicCarbon_mgC_per_kg',
        'ammonium_mgN_per_kg': 'ammonium_mgN_per_kg',
        'nitrate_mgN_per_kg': 'nitrate_mgN_per_kg',
        'phosphorus_mgP_per_kg': 'phosphorus_mgP_per_kg',
        'potassium_mgK_per_kg': 'potassium_mgK_per_kg',
        'extractableCalcium_mgCa_per_kg': 'extractableCalcium_mgCa_per_kg',
        'extractableMagnesium_mgMg_per_kg': 'extractableMagnesium_mgMg_per_kg',
        'extractableCopper_mgCu_per_kg': 'extractableCopper_mgCu_per_kg',
        'extractableIron_mgFe_per_kg': 'extractableIron_mgFe_per_kg',
        'extractableManganese_mgMN_per_kg': 'extractableManganese_mgMN_per_kg',
        'extractableZinc_mgZn_per_kg': 'extractableZinc_mgZn_per_kg',
        'mineralizableNitrogen_gN_per_kg': 'mineralizableNitrogen_gN_per_kg',
        'nitrites_mgN_per_kg': 'nitrites_mgN_per_kg',
        'phStd': 'phStd',
        'totalSoilCarbonSd_gC_per_kg': 'totalSoilCarbonSd_gC_per_kg',
        'totalSoilNitrogenSd_gN_per_kg': 'totalSoilNitrogenSd_gN_per_kg',
        'inorganicCarbonSd_gC_per_kg': 'inorganicCarbonSd_gC_per_kg',
        'organicCarbonSd_gC_per_kg': 'organicCarbonSd_gC_per_kg',
        'mineralCarbonSd_gC_per_kg': 'mineralCarbonSd_gC_per_kg',
        'cationExchangeCapacitySd_cmol_per_kg': 'cationExchangeCapacitySd_cmol_per_kg',
        'electricalConductivitySd_siemens_per_m': 'electricalConductivitySd_siemens_per_m',
        'solubleOrganicCarbonSd_mgC_per_kg': 'solubleOrganicCarbonSd_mgC_per_kg',
        'ammoniumSd_mgN_per_kg': 'ammoniumSd_mgN_per_kg',
        'nitrateSd_mgN_per_kg': 'nitrateSd_mgN_per_kg',
        'phosphorusSd_mgP_per_kg': 'phosphorusSd_mgP_per_kg',
        'potassiumSd_mgK_per_kg': 'potassiumSd_mgK_per_kg',
        'extractableCalciumSd_mgCa_per_kg': 'extractableCalciumSd_mgCa_per_kg',
        'extractableMagnesiumSd_mgMg_per_kg': 'extractableMagnesiumSd_mgMg_per_kg',
        'extractableCopperSd_mgCu_per_kg': 'extractableCopperSd_mgCu_per_kg',
        'extractableIronSd_mgFe_per_kg': 'extractableIronSd_mgFe_per_kg',
        'extractableManganeseSd_mgMN_per_kg': 'extractableManganeseSd_mgMN_per_kg',
        'extractableZincSd_mgZn_per_kg': 'extractableZincSd_mgZn_per_kg',
        'mineralizableNitrogenSd_gN_per_kg': 'mineralizableNitrogenSd_gN_per_kg',
        'nitritesSd_mgN_per_kg': 'nitritesSd_mgN_per_kg',
        
    }
    mappings['SoilChemicalSample'] = soil_chemical_sample_struct
    
    
    # MeasSoilBiol
    soil_biol_sample_struct = {
        '@fileName': raw_path + r'/measurements_soil_biological_with_UID.csv',
        '@uniqueId': 'measSoilBiol_UID',
        'measSoilBiol_UID': 'measSoilBiol_UID',
        'date': 'date',
        'treatmentId': 'treatmentId',
        'upperDepth_cm': 'upperDepth_cm',
        'lowerDepth_cm': 'lowerDepth_cm',
        'glucosidase_mg_per_kg_per_hr': 'glucosidase_mg_per_kg_per_hr',
        'glucosaminidase_mg_per_kg_per_hr': 'glucosaminidase_mg_per_kg_per_hr',
        'acidPhosphatase_mg_per_kg_per_hr': 'acidPhosphatase_mg_per_kg_per_hr',
        'alkPhosphatase_mg_per_kg_per_hr': 'alkPhosphatase_mg_per_kg_per_hr',
        'soilfluoresceinDiacetateHydrol_mg_per_kg_per_hr': 'soilfluoresceinDiacetateHydrol_mg_per_kg_per_hr',
        'glomalin_g_per_kg': 'glomalin_g_per_kg',
        'fattyAcidMethylEsters': 'fattyAcidMethylEsters',
        'phospholipidFattyAcids': 'phospholipidFattyAcids',
        'soilDna': 'soilDna',
        'organicPlantMaterial_gC_per_kg': 'organicPlantMaterial_gC_per_kg',
        'particulateOrganicMatter_gC_per_kg': 'particulateOrganicMatter_gC_per_kg',
        'carbonMicrobialBiomass_mgC_per_kg': 'carbonMicrobialBiomass_mgC_per_kg',
        'nitrogenMicrobialBiomass_mgN_per_kg': 'nitrogenMicrobialBiomass_mgN_per_kg',
        'glucosidaseSd_mg_per_kg_per_hr': 'glucosidaseSd_mg_per_kg_per_hr',
        'glucosaminidaseSd_mg_per_kg_per_hr': 'glucosaminidaseSd_mg_per_kg_per_hr',
        'acidPhosphataseSd_mg_per_kg_per_hr': 'acidPhosphataseSd_mg_per_kg_per_hr',
        'alkPhosphataseSd_mg_per_kg_per_hr': 'alkPhosphataseSd_mg_per_kg_per_hr',
        'soilfluoresceinDiacetateHydrolSd_mg_per_kg_per_hr': 'soilfluoresceinDiacetateHydrolSd_mg_per_kg_per_hr',
        'glomalinSd_g_per_kg': 'glomalinSd_g_per_kg',
        'organicPlantMaterialSd_gC_per_kg': 'organicPlantMaterialSd_gC_per_kg',
        'particulateOrganicMatterSd_gC_per_kg': 'particulateOrganicMatterSd_gC_per_kg',
        'carbonMicrobialBiomassSd_mgC_per_kg': 'carbonMicrobialBiomassSd_mgC_per_kg',
        'nitrogenMicrobialBiomassSd_mgN_per_kg': 'nitrogenMicrobialBiomassSd_mgN_per_kg',
        }
    mappings['SoilBiologicalSample'] = soil_biol_sample_struct

    #MeasSoilCover

    soil_cover_struct = {
        '@fileName': raw_path + r'/measurements_soil_cover_with_UID.csv',
        '@uniqueId': 'measSoilCover_UID',
        'measSoilCover_UID': 'measSoilCover_UID',
        'soilCoverTimingDescriptor': 'soilCoverTimingDescriptor',
        'soilWithResidueCoverPercent': 'soilWithResidueCoverPercent',
        'date': 'date',
    }
    mappings['SoilCover'] = soil_cover_struct
    
    #MeasGHGFlux

    gas_sample_struct = {
        '@fileName': raw_path + r'/measurements_greenhouse_gases_flux_with_UID.csv',
        '@uniqueId': 'measGHGFlux_UID',
        'measGHGFlux_UID': 'measGHGFlux_UID',
        'chamberPlacement': 'chamberPlacement',
        'date': 'date',
        'time': 'time',
        'treatmentId': 'treatmentId',
        'nitrousOxide_gN_per_ha_per_d': 'nitrousOxide_gN_per_ha_per_d',
        'isNitrousOxideInterpolated': 'isNitrousOxideInterpolated',
        'carbonDioxide_gC_per_ha_per_d': 'carbonDioxide_gC_per_ha_per_d',
        'isCarbonDioxideInterpolated': 'isCarbonDioxideInterpolated',
        'methane_gC_per_ha_per_d': 'methane_gC_per_ha_per_d',
        'isMethaneInterpolated': 'isMethaneInterpolated',
        'airTemperature_degC': 'airTemperature_degC',
        'nitrousOxideSd_gN_per_ha_per_d': 'nitrousOxideSd_gN_per_ha_per_d', # not sure what happened but these two switched in the data USDA sent
        'carbonDioxideSd_gC_per_ha_per_d': 'carbonDioxideSd_gC_per_ha_per_d',
        'methaneSd_gC_per_ha_per_d': 'methaneSd_gC_per_ha_per_d',
        'airTemperatureSd_degC': 'airTemperatureSd_degC',
        'soilTemperature_degC': 'soilTemperature_degC',
        'soilMoisture_percent_volume': 'soilMoisture_percent_volume',
        'soilMoistureDepth_cm': 'soilMoistureDepth_cm',
        'soilTemperatureSd_degC': 'soilTemperatureSd_degC',
        'soilMoistureSd_percent_volume': 'soilMoistureSd_percent_volume',
        'crop': 'crop',
    }
    mappings['GasSample'] = gas_sample_struct

    #MeasResidueMgnt

    harvest_struct = {
        '@fileName': raw_path + r'/measurements_residue_management_with_UID.csv',
        '@uniqueId': 'measResidueMgnt_UID',
        'measResidueMgnt_UID': 'measResidueMgnt_UID',
        'crop': 'crop',
        'treatmentId': 'treatmentId',
        'unitGrainWeightSd_mg': 'unitGrainWeightSd_mg',
        'cornEarHeightSd_cm': 'cornEarHeightSd_cm',
        'grainMoisturePercentStd': 'grainMoisturePercentStd',
        'driedHarvestedResidueSd_kg_per_ha': 'driedHarvestedResidueSd_kg_per_ha',
        'grainCarbonSd_kgC_per_ha': 'grainCarbonSd_kgC_per_ha',
        'grainNitrogenSd_kgN_per_ha': 'grainNitrogenSd_kgN_per_ha',
        'aboveGroundBiomassSd_kg_per_ha': 'aboveGroundBiomassSd_kg_per_ha',
        'harvestedResidueCarbonSd_kgC_per_ha': 'harvestedResidueCarbonSd_kgC_per_ha',
        'harvestedResidueMoisturePercentStd': 'harvestedResidueMoisturePercentStd',
        'grainYieldSd_kg_per_ha': 'grainYieldSd_kg_per_ha',
        'harvestedResidueNitrogenSd_kgN_per_ha': 'harvestedResidueNitrogenSd_kgN_per_ha',
        'driedHarvestedResidue_kg_per_ha': 'driedHarvestedResidue_kg_per_ha',
        'grainMoisturePercent': 'grainMoisturePercent',
        'aboveGroundBiomass_kg_per_ha': 'aboveGroundBiomass_kg_per_ha',
        'cornEarHeight_cm': 'cornEarHeight_cm',
        'date': 'date',
        'harvestedFrac': 'harvestedFrac',
        'grainCarbon_kgC_per_ha': 'grainCarbon_kgC_per_ha',
        'grainNitrogen_kgN_per_ha': 'grainNitrogen_kgN_per_ha',
        'grainYield_kg_per_ha': 'grainYield_kg_per_ha',
        'harvestedResidueCarbon_kgC_per_ha': 'harvestedResidueCarbon_kgC_per_ha',
        'harvestedResidueMoisturePercent': 'harvestedResidueMoisturePercent',
        'harvestedResidueNitrogen_kgN_per_ha': 'harvestedResidueNitrogen_kgN_per_ha',
        'growthStage': 'growthStage',
        'unitGrainWeight_mg': 'unitGrainWeight_mg',
        'nonHarvestedResidueCarbonContentSd_kgC_per_ha': 'nonHarvestedResidueCarbonContentSd_kgC_per_ha',
        'nonHarvestedResidueNitrogenContentSd_kgN_per_ha': 'nonHarvestedResidueNitrogenContentSd_kgN_per_ha',
        'nonHarvestedResidueNitrogenContent_kgN_per_ha': 'nonHarvestedResidueNitrogenContent_kgN_per_ha',
        'nonHarvestedResidueMass_kg_per_ha': 'nonHarvestedResidueMass_kg_per_ha',
        'nonHarvestedResidueMoisturePercentStd': 'nonHarvestedResidueMoisturePercentStd',
        'nonHarvestedResidueCarbonContent_kgC_per_ha': 'nonHarvestedResidueCarbonContent_kgC_per_ha',
        'nonHarvestedResidueMassSd_kg_per_ha': 'nonHarvestedResidueMassSd_kg_per_ha',
        'nonHarvestedResidueMoisturePercent': 'nonHarvestedResidueMoisturePercent',
        'rootMoisturePercent': 'rootMoisturePercent',
        'rootDryMatter_kg_per_ha': 'rootDryMatter_kg_per_ha',
        'rootNitrogenContentSd_kgN_per_ha': 'rootNitrogenContentSd_kgN_per_ha',
        'rootCarbonContent_kgC_per_ha': 'rootCarbonContent_kgC_per_ha',
        'rootMoisturePercentStd': 'rootMoisturePercentStd',
        'rootDryMatterSd_kg_per_ha': 'rootDryMatterSd_kg_per_ha',
        'rootCarbonContentSd_kgC_per_ha': 'rootCarbonContentSd_kgC_per_ha',
        'rootNitrogenContent_kgN_per_ha': 'rootNitrogenContent_kgN_per_ha',
    }
    mappings['Harvest'] = harvest_struct

    #MeasHarvestFraction

    plant_fraction_struct = {
        '@fileName': raw_path + r'/measurements_harvest_fraction_with_UID.csv',
        '@uniqueId': 'measHarvestFraction_UID',
        'measHarvestFraction_UID': 'measHarvestFraction_UID',
        'date': 'date',
        'growthStage': 'growthStage',
        'crop': 'crop',
        'treatmentId': 'treatmentId',
        'plantFraction': 'plantFraction',
        'dryBiomass_kg_per_ha': 'dryBiomass_kg_per_ha',
        'moisturePercent': 'moisturePercent',
        'carbon_kgC_per_ha': 'carbon_kgC_per_ha',
        'nitrogen_kgN_per_ha': 'nitrogen_kgN_per_ha',
        'grainWeight_mg_per_kernel': 'grainWeight_mg_per_kernel',
        'dryBiomassSd_kg_per_ha': 'dryBiomassSd_kg_per_ha',
        'moisturePercentStd': 'moisturePercentStd',
        'carbonSd_kgC_per_ha': 'carbonSd_kgC_per_ha',
        'nitrogenSd_kgN_per_ha': 'nitrogenSd_kgN_per_ha',
        'grainWeightSd_mg_per_lernel': 'grainWeightSd_mg_per_lernel',
    }
    mappings['HarvestFraction'] = plant_fraction_struct

    #MeasBiomassCHO
    biomass_cho_struct ={
        '@fileName': raw_path + r'/measurements_biomass_cho_with_UID.csv',
        '@uniqueId': 'measBiomassCHO_UID',
        'measBiomassCHO_UID': 'measBiomassCHO_UID',
        'plantFraction': 'plantFraction',
        'growthStage': 'growthStage',
        'date': 'date',
        'crop': 'crop',
        'treatmentId': 'treatmentId',
        'glucan_g_per_kg': 'glucan_g_per_kg',
        'xylan_g_per_kg': 'xylan_g_per_kg',
        'galactan_g_per_kg': 'galactan_g_per_kg',
        'arabinan_g_per_kg': 'arabinan_g_per_kg',
        'mannan_g_per_kg': 'mannan_g_per_kg',
        'lignin_g_per_kg': 'lignin_g_per_kg',
        'neutralDetFiber_g_per_kg': 'neutralDetFiber_g_per_kg',
        'acidDetFiber_g_per_kg': 'acidDetFiber_g_per_kg',
        'acidSolubleLignin_g_per_kg': 'acidSolubleLignin_g_per_kg',
        'acidInsolubleLignin_g_per_kg': 'acidInsolubleLignin_g_per_kg',
        'crudeProtein_g_per_kg': 'crudeProtein_g_per_kg',
        'nonFiberCarbs_g_per_kg': 'nonFiberCarbs_g_per_kg',
        'ash_g_per_kg': 'ash_g_per_kg',
        'glucanSd_g_per_kg': 'glucanSd_g_per_kg',
        'xylanSd_g_per_kg': 'xylanSd_g_per_kg',
        'galactanSd_g_per_kg': 'galactanSd_g_per_kg',
        'arabinanSd_g_per_kg': 'arabinanSd_g_per_kg',
        'mannanSd_g_per_kg': 'mannanSd_g_per_kg',
        'ligninSd_g_per_kg': 'ligninSd_g_per_kg',
        'neutralDetFiberSd_g_per_kg': 'neutralDetFiberSd_g_per_kg',
        'acidDetFiberSd_g_per_kg': 'acidDetFiberSd_g_per_kg',
        'acidSolubleLigninSd_g_per_kg': 'acidSolubleLigninSd_g_per_kg',
        'acidInsolubleLigninSd_g_per_kg': 'acidInsolubleLigninSd_g_per_kg',
        'crudeProteinSd_g_per_kg': 'crudeProteinSd_g_per_kg',
        'nonFiberCarbsSd_g_per_kg': 'nonFiberCarbsSd_g_per_kg',
        'ashSd_g_per_kg': 'ashSd_g_per_kg',
    }
    mappings['BioMassCarbohydrate'] = biomass_cho_struct

    #MeasBiomassEnergy
    biomass_energy_struct ={
        '@fileName': raw_path + r'/measurements_biomass_energy_with_UID.csv',
        '@uniqueId': 'measBiomassEnergy_UID',
        'measBiomassEnergy_UID': 'measBiomassEnergy_UID',
        'crop': 'crop',
        'treatmentId': 'treatmentId',
        'plantFraction': 'plantFraction',
        'growthStage': 'growthStage',
        'mineralMatterSd_g_per_kg': 'mineralMatterSd_g_per_kg',
        'date': 'date',
        'volatileMatter_g_per_kg': 'volatileMatter_g_per_kg',
        'mineralMatter_g_per_kg': 'mineralMatter_g_per_kg',
        'grossCalorificValue_MJ_per_kg': 'grossCalorificValue_MJ_per_kg',
        'volatileMatterSd_g_per_kg': 'volatileMatterSd_g_per_kg',
        'grossCalorificValueSd_MJ_per_kg': 'grossCalorificValueSd_MJ_per_kg',
    }
    mappings['BioMassEnergy'] = biomass_energy_struct

    #MeasBiomassMinAn
    biomass_min_an_struct = {
        '@fileName': raw_path + r'/measurements_biomass_mineral_analysis_with_UID.csv',
        '@uniqueId': 'measBiomassMinAn_UID',
        'measBiomassMinAn_UID': 'measBiomassMinAn_UID',
        'plantFraction': 'plantFraction',
        'growthStage': 'growthStage',
        'crop': 'crop',
        'treatmentId': 'treatmentId',
        'carbonConcentration_g_per_kg': 'carbonConcentration_g_per_kg',
        'nitrogenConcentration_g_per_kg': 'nitrogenConcentration_g_per_kg',
        'phosphorusConcentration_g_per_kg': 'phosphorusConcentration_g_per_kg',
        'potassiumConcentration_g_per_kg': 'potassiumConcentration_g_per_kg',
        'calciumConcentration_g_per_kg': 'calciumConcentration_g_per_kg',
        'magnesiumConcentration_g_per_kg': 'magnesiumConcentration_g_per_kg',
        'sulfurConcentration_g_per_kg': 'sulfurConcentration_g_per_kg',
        'sodiumConcentration_g_per_kg': 'sodiumConcentration_g_per_kg',
        'chlorineConcentration_g_per_kg': 'chlorineConcentration_g_per_kg',
        'aluminumConcentration_mg_per_kg': 'aluminumConcentration_mg_per_kg',
        'boronConcentration_mg_per_kg': 'boronConcentration_mg_per_kg',
        'copperConcentration_mg_per_kg': 'copperConcentration_mg_per_kg',
        'ironConcentration_mg_per_kg': 'ironConcentration_mg_per_kg',
        'manganeseConcentration_mg_per_kg': 'manganeseConcentration_mg_per_kg',
        'zincConcentration_mg_per_kg': 'zincConcentration_mg_per_kg',
        'carbonConcentrationSd_g_per_kg': 'carbonConcentrationSd_g_per_kg',
        'nitrogenConcentrationSd_g_per_kg': 'nitrogenConcentrationSd_g_per_kg',
        'phosphorusConcentrationSd_g_per_kg': 'phosphorusConcentrationSd_g_per_kg',
        'potassiumConcentrationSd_g_per_kg': 'potassiumConcentrationSd_g_per_kg',
        'calciumConcentrationSd_g_per_kg': 'calciumConcentrationSd_g_per_kg',
        'magnesiumConcentrationSd_g_per_kg': 'magnesiumConcentrationSd_g_per_kg',
        'sulfurConcentrationSd_g_per_kg': 'sulfurConcentrationSd_g_per_kg',
        'sodiumConcentrationSd_g_per_kg': 'sodiumConcentrationSd_g_per_kg',
        'chlorineConcentrationSd_g_per_kg': 'chlorineConcentrationSd_g_per_kg',
        'aluminumConcentrationSd_mg_per_kg': 'aluminumConcentrationSd_mg_per_kg',
        'boronConcentrationSd_mg_per_kg': 'boronConcentrationSd_mg_per_kg',
        'copperConcentrationSd_mg_per_kg': 'copperConcentrationSd_mg_per_kg',
        'ironConcentrationSd_mg_per_kg': 'ironConcentrationSd_mg_per_kg',
        'manganeseConcentrationSd_mg_per_kg': 'manganeseConcentrationSd_mg_per_kg',
        'zincConcentrationSd_mg_per_kg': 'zincConcentrationSd_mg_per_kg',
        'date': 'date'
    }
    mappings['BioMassMineral'] = biomass_min_an_struct

    #MeasGrazingPlants

    grazingStruct = {
        '@fileName':  raw_path + r'/measurements_grazing_plants_with_UID.csv',
        '@uniqueId': 'measGrazingPlants_UID',
        'measGrazingPlants_UID': 'measGrazingPlants_UID',
        'speciesMix': 'speciesMix',
        'broadleafOrGrass': 'broadleafOrGrass',
        'growthStage': 'growthStage',
        'treatmentId': 'treatmentId',
        'aboveGroundBiomassDry_kg_per_ha': 'aboveGroundBiomassDry_kg_per_ha',
        'aurfaceLitterDry_kg_per_ha': 'aurfaceLitterDry_kg_per_ha',
        'atandingDeadDry_kg_per_ha': 'atandingDeadDry_kg_per_ha',
        'leafAreaIndexDry_kg_per_ha': 'leafAreaIndexDry_kg_per_ha',
        'biomassNitrogenPercentage': 'biomassNitrogenPercentage',
        'ligninPercentage': 'ligninPercentage',
        'groundCoverPercentage': 'groundCoverPercentage',
        'aboveGroundBiomassCarbon_kgC_per_ha': 'aboveGroundBiomassCarbon_kgC_per_ha',
        'aboveGroundBiomassNitrogen_kgN_per_ha': 'aboveGroundBiomassNitrogen_kgN_per_ha',
        'belowGroundBiomassCarbon_kgC_per_ha': 'belowGroundBiomassCarbon_kgC_per_ha',
        'belowGroundBiomassNitrogen_kgN_per_ha': 'belowGroundBiomassNitrogen_kgN_per_ha',
        'abovegroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr': 'abovegroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr',
        'abovegroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr': 'abovegroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr',
        'belowgroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr': 'belowgroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr',
        'belowgroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr': 'belowgroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr',
        'aboveGroundBiomassDrySd_kg_per_ha': 'aboveGroundBiomassDrySd_kg_per_ha',
        'aurfaceLitterDrySd_kg_per_ha': 'aurfaceLitterDrySd_kg_per_ha',
        'atandingDeadDrySd_kg_per_ha': 'atandingDeadDrySd_kg_per_ha',
        'leafAreaIndexDrySd_kg_per_ha': 'leafAreaIndexDrySd_kg_per_ha',
        'biomassNitrogenPercentageStd': 'biomassNitrogenPercentageStd',
        'ligninPercentageStd': 'ligninPercentageStd',
        'groundCoverPercentageStd': 'groundCoverPercentageStd',
        'aboveGroundBiomassCarbonSd_kgC_per_ha': 'aboveGroundBiomassCarbonSd_kgC_per_ha',
        'aboveGroundBiomassNitrogenSd_kgN_per_ha': 'aboveGroundBiomassNitrogenSd_kgN_per_ha',
        'belowGroundBiomassCarbonSd_kgC_per_ha': 'belowGroundBiomassCarbonSd_kgC_per_ha',
        'belowGroundBiomassNitrogenSd_kgN_per_ha': 'belowGroundBiomassNitrogenSd_kgN_per_ha',
        'abovegroundNetPrimaryProductivityCarbonSd_kgC_per_ha_per_yr': 'abovegroundNetPrimaryProductivityCarbonSd_kgC_per_ha_per_yr',
        'abovegroundNetPrimaryProductivityNitrogenSd_kgN_per_ha_per_yr': 'abovegroundNetPrimaryProductivityNitrogenSd_kgN_per_ha_per_yr',
        'belowgroundNetPrimaryProductivityCarbonSd_kgC_per_ha_per_yr': 'belowgroundNetPrimaryProductivityCarbonSd_kgC_per_ha_per_yr',
        'belowgroundNetPrimaryProductivityNitrogenSd_kgN_per_ha_per_yr': 'belowgroundNetPrimaryProductivityNitrogenSd_kgN_per_ha_per_yr',
        'date': 'date',
    }
    mappings['Grazing'] = grazingStruct

    #MeasSuppRes

    miscellaneous_measurement_struct = {
        '@fileName':  raw_path + r'/measurements_supporting_research_with_UID.csv',
        '@uniqueId': 'miscellaneousMeasurementUniqueId',
        'miscellaneousMeasurementUniqueId': 'miscellaneousMeasurementUniqueId',
        'miscellaneousMeasurementUnits': 'miscellaneousMeasurementUnits',
        'miscellaneousMeasurementDate': 'miscellaneousMeasurementDate',
        'miscellaneousMeasurementDescription': 'miscellaneousMeasurementDescription',
        'miscellaneousMeasurementValue': 'miscellaneousMeasurementValue',
    }
    mappings['MiscellaneousMeasurement'] = miscellaneous_measurement_struct

    measurement_nutrient_efficiency_struct = {
        '@fileName': raw_path + r'/measurements_nutrient_efficiency_with_UID.csv',
        '@uniqueId': 'measNutrEff_UID',
        'measNutrEff_UID': 'measNutrEff_UID',
        'fieldId': 'fieldId',
        'expUnitId': 'expUnitId',
        'date': 'date',
        'expUnit_UID': 'expUnit_UID',
        'treatmentId': 'treatmentId',
        'growthStage': 'growthStage',
        'crop': 'crop',
        'plantFraction': 'plantFraction',
        'fracNitrogen_kg_ha': 'fracNitrogen_kg_ha',
        'nitrogenUseEfficiencyPct': 'nitrogenUseEfficiencyPct',
        'agronomicEfficiency_kg_kg': 'agronomicEfficiency_kg_kg',
        'nutrientEfficiencyRatio_kg_kg': 'nutrientEfficiencyRatio_kg_kg',
        'nitrogenUseEfficiency_kg_ha': 'nitrogenUseEfficiency_kg_ha'
    }
    mappings['NutrientEfficiency'] = measurement_nutrient_efficiency_struct

    measurements_yield_nutrient_uptake_struct = {
        '@fileName': raw_path + r'/measurements_yield_nutrient_uptake_with_UID.csv',
        '@uniqueId': 'measYieldNutUptake_UID',
        'measYieldNutUptake_UID': 'measYieldNutUptake_UID', 
        'fieldId': 'fieldId',
        'expUnitId': 'expUnitId',
        'date': 'date',
        'expUnit_UID': 'expUnit_UID',
        'treatmentId': 'treatmentId',
        'growthStage': 'growthStage',
        'crop': 'crop',
        'plantFraction': 'plantFraction',
        'modelIfSimulated': 'modelIfSimulated',
        'fracCropProductivity_kg_ha': 'fracCropProductivity_kg_ha',
        'fracMoisturePercent': 'fracMoisturePercent',
        'fracCarbon_kgC_ha': 'fracCarbon_kgC_ha',
        'fracNitrogen_kgN_ha': 'fracNitrogen_kgN_ha',
        'fracPhosphorus_kgP_ha': 'fracPhosphorus_kgP_ha',
        'fracPotassium_kgK_ha': 'fracPotassium_kgK_ha',
        'fracSulfur_kgS_ha': 'fracSulfur_kgS_ha',
        'fracCalcium_kgCa_ha': 'fracCalcium_kgCa_ha',
        'fracMagnesium_kgMg_ha': 'fracMagnesium_kgMg_ha',
        'fracCopper_gCu_ha': 'fracCopper_gCu_ha',
        'fracIron_gFe_ha': 'fracIron_gFe_ha',
        'fracManganese_gMn_ha': 'fracManganese_gMn_ha',
        'fracZinc_gZn_ha': 'fracZinc_gZn_ha',
        'fracBoron_gB_ha': 'fracBoron_gB_ha',
        'fracMolybdenum_gMo_ha': 'fracMolybdenum_gMo_ha',
        'grainWeightKernelYnu_mg': 'grainWeightKernelYnu_mg',
        'fracProductivitySd_kg_ha': 'fracProductivitySd_kg_ha',
        'fracMoisturePercentStd': 'fracMoisturePercentStd',
        'fracCarbonSd_kgC_ha': 'fracCarbonSd_kgC_ha',
        'fracNitrogenSd_kgN_ha': 'fracNitrogenSd_kgN_ha',
        'fracPhosphorusSd_kgP_ha': 'fracPhosphorusSd_kgP_ha',
        'fracPotassiumSd_kgK_ha': 'fracPotassiumSd_kgK_ha',
        'fracSulfurSd_kgS_ha': 'fracSulfurSd_kgS_ha',
        'fracCalciumSd_kgCa_ha': 'fracCalciumSd_kgCa_ha',
        'fracMagnesiumSd_kgMg_ha': 'fracMagnesiumSd_kgMg_ha',
        'fracCopperSd_gCu_ha': 'fracCopperSd_gCu_ha',
        'fracIronSd_gFe_ha': 'fracIronSd_gFe_ha',
        'fracManganeseSd_gMn_ha': 'fracManganeseSd_gMn_ha',
        'fracZincSd_gZn_ha': 'fracZincSd_gZn_ha',
        'fracBoronSd_gB_ha': 'fracBoronSd_gB_ha',
        'fracMolybdenumSd_gMo_ha': 'fracMolybdenumSd_gMo_ha',
        'grainWeightKernelYnuSd_mg': 'grainWeightKernelYnuSd_mg',
    }
    mappings['YieldNutrientUptake'] = measurements_yield_nutrient_uptake_struct
    #here
    measurements_wind_erosion_area_struct = {
        '@fileName': raw_path + r'/measurements_wind_erosion_area_with_UID.csv',
        '@uniqueId': 'measWindErosionArea_UID',
        'measWindErosionArea_UID': 'measWindErosionArea_UID',
        'fieldId': 'fieldId',
        'expUnitId': 'expUnitId',
        'expUnit_UID': 'expUnit_UID',
        'date': 'date',
        'time': 'time',
        'treatmentId': 'treatmentId',
        'growthStage': 'growthStage',
        'crop': 'crop',
        'samplingStartStopInterval': 'samplingStartStopInterval',
        'modelIfSimulated': 'modelIfSimulated',
        'erosionMethod': 'erosionMethod',
        'lossesOrDeposition': 'lossesOrDeposition',
        'soil_t_ha': 'soil_t_ha',
        'soilOrganicMatter_kg_ha': 'soilOrganicMatter_kg_ha',
        'soilOrganicCarbon_kg_ha': 'soilOrganicCarbon_kg_ha',
        'ph': 'ph',
        'electricalConductivity_ms_cm': 'electricalConductivity_ms_cm',
        'totalNitrogen_kg_ha': 'totalNitrogen_kg_ha',
        'inorganicNitrogen_kgN_ha': 'inorganicNitrogen_kgN_ha',
        'nitrate_kg_ha': 'nitrate_kg_ha',
        'phosphorus_kg_ha': 'phosphorus_kg_ha',
        'potassium_kg_ha': 'potassium_kg_ha',
        'sulfur_kg_ha': 'sulfur_kg_ha',
        'calcium_kg_ha': 'calcium_kg_ha',
        'magnesium_kg_ha': 'magnesium_kg_ha',
        'copper_g_ha': 'copper_g_ha',
        'iron_g_ha': 'iron_g_ha',
        'manganese_g_ha': 'manganese_g_ha',
        'zinc_g_ha': 'zinc_g_ha',
        'boron_g_ha': 'boron_g_ha',
        'molybdenum_g_ha': 'molybdenum_g_ha',
        'aluminum_kg_ha': 'aluminum_kg_ha',
        'sodium_kg_ha': 'sodium_kg_ha',
        'silicon_kg_ha': 'silicon_kg_ha',
        'soilSd_t_ha': 'soilSd_t_ha',
        'soilOrganicMatterSd_kg_ha': 'soilOrganicMatterSd_kg_ha',
        'soilOrganicCarbonSd_kgC_ha': 'soilOrganicCarbonSd_kgC_ha',
        'phStd': 'phStd',
        'electricalConductivitySd_ms_cm': 'electricalConductivitySd_ms_cm',
        'totalNitrogenSd_kgN_ha': 'totalNitrogenSd_kgN_ha',
        'inorganicNitrogenSd_kgN_ha': 'inorganicNitrogenSd_kgN_ha',
        'nitrateSd_kgN_ha': 'nitrateSd_kgN_ha',
        'phosphorusSd_kg_ha': 'phosphorusSd_kg_ha',
        'potassiumSd_kg_ha': 'potassiumSd_kg_ha',
        'sulfurSd_kg_ha': 'sulfurSd_kg_ha',
        'calciumSd_kg_ha': 'calciumSd_kg_ha',
        'magnesiumSd_kg_ha': 'magnesiumSd_kg_ha',
        'copperSd_g_ha': 'copperSd_g_ha',
        'ironSd_g_ha': 'ironSd_g_ha',
        'manganeseSd_g_ha': 'manganeseSd_g_ha',
        'zincSd_g_ha': 'zincSd_g_ha',
        'boronSd_g_ha': 'boronSd_g_ha',
        'molybdenumSd_g_ha': 'molybdenumSd_g_ha',
        'aluminumSd_kg_ha': 'aluminumSd_kg_ha',
        'sodiumSd_kg_ha': 'sodiumSd_kg_ha',
        'siliconSd_kg_ha': 'siliconSd_kg_ha',
    }
    mappings['WindErosionArea'] = measurements_wind_erosion_area_struct

    measurements_water_quality_area_struct = {
        '@fileName': raw_path + r'/measurements_water_quality_area_with_UID.csv',
        '@uniqueId': 'measWaterQualityArea_UID',
        'measWaterQualityArea_UID': 'measWaterQualityArea_UID',
        'fieldId': 'fieldId',
        'expUnitId': 'expUnitId',
        'date': 'date',
        'time': 'time',
        'expUnit_UID': 'expUnit_UID',
        'treatmentId': 'treatmentId',
        'growthStage': 'growthStage',
        'crop': 'crop',
        'samplingStartStopInterval': 'samplingStartStopInterval',
        'modelIfSimulated': 'modelIfSimulated',
        'surfaceOrLeaching': 'surfaceOrLeaching',
        'lossesOrDeposition': 'lossesOrDeposition',
        'erosionMethod': 'erosionMethod',
        'soilOrganicMatter_kg_ha': 'soilOrganicMatter_kg_ha',  # new
        'erosionSediment_t_ha': 'erosionSediment_t_ha', # what does T mean?
        'erosionTotalSuspendedSolids_t_ha': 'erosionTotalSuspendedSolids_t_ha',
        'erosionTotalSolids_t_ha': 'erosionTotalSolids_t_ha',
        'soilOrganicMatter_kg_ha': 'soilOrganicMatter_kg_ha',
        'soilOrganicCarbon_kgC_ha': 'soilOrganicCarbon_kgC_ha',
        'water_mm': 'water_mm',
        'totalNitrogen_kg_ha': 'totalNitrogen_kg_ha',
        'totalPhosphoru_kg_ha': 'totalPhosphoru_kg_ha',
        'ammoniumNitroge_kg_ha': 'ammoniumNitroge_kg_ha',
        'nitrateNitrogen_kg_ha': 'nitrateNitrogen_kg_ha',
        'totalDissolvedNitrogen_kgN_ha': 'totalDissolvedNitrogen_kgN_ha',
        'totalDissolvedPhosphorus_kgP_ha': 'totalDissolvedPhosphorus_kgP_ha',
        'totalChloride_kg_ha': 'totalChloride_kg_ha',
        'ph': 'ph',
        'electricalConductivity_ms_cm': 'electricalConductivity_ms_cm',
        'dissolvedPotassium_kgK_ha': 'dissolvedPotassium_kgK_ha',
        'dissolvedSulfur_kgS_ha': 'dissolvedSulfur_kgS_ha',
        'dissolvedCalcium_kgCa_ha': 'dissolvedCalcium_kgCa_ha',
        'dissolvedMagnesium_kgMg_ha': 'dissolvedMagnesium_kgMg_ha',
        'dissolvedCopper_gCu_ha': 'dissolvedCopper_gCu_ha',
        'dissolvedIron_gFe_ha': 'dissolvedIron_gFe_ha',
        'dissolvedManganese_gMn_ha': 'dissolvedManganese_gMn_ha',
        'dissolvedZinc_gZn_ha': 'dissolvedZinc_gZn_ha',
        'dissolvedBoron_gB_ha': 'dissolvedBoron_gB_ha',
        'dissolvedMolybdenum_gMo_ha': 'dissolvedMolybdenum_gMo_ha',
        'dissolvedAluminum_kg_al_ha': 'dissolvedAluminum_kg_al_ha',
        'dissolvedSodium_kgNa_ha': 'dissolvedSodium_kgNa_ha',
        'dissolvedSilicon_kgSi_ha': 'dissolvedSilicon_kgSi_ha',
        'erosionSedimentSd_t_ha': 'erosionSedimentSd_t_ha', # T?
        'erosionTotalSuspendedSolidsSd_t_ha': 'erosionTotalSuspendedSolidsSd_t_ha',
        'erosionTotalSolidsSd_t_ha': 'erosionTotalSolidsSd_t_ha',
        'soilOrganicMatterSd_kg_ha': 'soilOrganicMatterSd_kg_ha',
        'soilOrganicCarbonSd_kgC_ha': 'soilOrganicCarbonSd_kgC_ha',
        'waterSd_mm': 'waterSd_mm',
        'totalNitrogenSd_kgN_ha': 'totalNitrogenSd_kgN_ha',
        'totalPhosphorusSd_kgP_ha': 'totalPhosphorusSd_kgP_ha',
        'inorganicNitrogenSd_kgN_ha': 'inorganicNitrogenSd_kgN_ha',
        'nitrateSd_kgN_ha': 'nitrateSd_kgN_ha',
        'totalDissolvedNitrogenSd_kgN_ha': 'totalDissolvedNitrogenSd_kgN_ha',
        'totalDissolvedPhosphorusSd_jgP_ha': 'totalDissolvedPhosphorusSd_jgP_ha',
        'totalChlorideSd_kg_cl_ha': 'totalChlorideSd_kg_cl_ha',
        'phStd': 'phStd',
        'electricalConductivitySd_ms_cm': 'electricalConductivitySd_ms_cm',
        'dissolvedPotassiumSd_kgK_ha': 'dissolvedPotassiumSd_kgK_ha',
        'dissolvedSulfurSd_kgS_ha': 'dissolvedSulfurSd_kgS_ha',
        'dissolvedCalciumSd_kgCa_ha': 'dissolvedCalciumSd_kgCa_ha',
        'dissolvedMagnesiumSd_kgMg_ha': 'dissolvedMagnesiumSd_kgMg_ha',
        'dissolvedCopperSd_gCu_ha': 'dissolvedCopperSd_gCu_ha',
        'dissolvedIronSd_gFe_ha': 'dissolvedIronSd_gFe_ha',
        'dissolvedManganeseSd_gMn_ha': 'dissolvedManganeseSd_gMn_ha',
        'dissolvedZincSd_gZn_ha': 'dissolvedZincSd_gZn_ha',
        'dissolvedBoronSd_gB_ha': 'dissolvedBoronSd_gB_ha',
        'dissolvedMolybdenumSd_gMo_ha': 'dissolvedMolybdenumSd_gMo_ha',
        'dissolvedAluminumSd_kg_al_ha': 'dissolvedAluminumSd_kg_al_ha',
        'dissovledSodiumSd_kgNa_ha': 'dissovledSodiumSd_kgNa_ha',
        'dissovledSiliconSd_kgSi_ha': 'dissovledSiliconSd_kgSi_ha',
    }
    mappings['WaterQualityArea'] = measurements_water_quality_area_struct

    measurements_water_quality_concentration_struct = {
        '@fileName': raw_path + r'/measurements_water_quality_concentration_with_UID.csv',
        '@uniqueId': 'measWaterQualityConc_UID',
        'measWaterQualityConc_UID': 'measWaterQualityConc_UID',
        'fieldId': 'fieldId',
        'expUnitId': 'expUnitId',
        'date': 'date',
        'time': 'time',
        'expUnit_UID': 'expUnit_UID',
        'treatmentId': 'treatmentId',
        'growthStage': 'growthStage',
        'crop': 'crop',
        'samplingStartStopInterval': 'samplingStartStopInterval',
        'modelIfSimulated': 'modelIfSimulated',
        'surfaceOrLeaching': 'surfaceOrLeaching',
        'samplingDepth_cm': 'samplingDepth_cm',
        'lossesOrDeposition': 'lossesOrDeposition',
        'erosionMethod': 'erosionMethod',
        'erosionSediment_kg': 'erosionSediment_kg',
        'erosionTotalSuspendedSolids_kg': 'erosionTotalSuspendedSolids_kg',
        'erosionTotalSolids_kg': 'erosionTotalSolids_kg',
        'soilOrganicMatter_mgSom_l': 'soilOrganicMatter_mgSom_l',
        'soilOrganicCarbon_mg_c_l': 'soilOrganicCarbon_mg_c_l',
        'water_mm': 'water_mm',
        'totalNitrogen_mg_l': 'totalNitrogen_mg_l',
        'totalPhosphorus_mg_l': 'totalPhosphorus_mg_l',
        'InorganicNitrogen_mg_l': 'InorganicNitrogen_mg_l',
        'nitrate_mg_l': 'nitrate_mg_l',
        'totalDissolvedNitrogen_mgN_l': 'totalDissolvedNitrogen_mgN_l',
        'totalDissolvedPhosphorus_mgP_l': 'totalDissolvedPhosphorus_mgP_l',
        'chloride_mg_l': 'chloride_mg_l',
        'ph': 'ph',
        'electricalConductivity_ms_cm': 'electricalConductivity_ms_cm',
        'dissolvedPotassium_mgK_l': 'dissolvedPotassium_mgK_l',
        'dissolvedSulfur_mgS_l': 'dissolvedSulfur_mgS_l',
        'dissolvedCalcium_mgCa_l': 'dissolvedCalcium_mgCa_l',
        'dissolvedMagnesium_mgMg_l': 'dissolvedMagnesium_mgMg_l',
        'dissolvedCopper_ugCu_l': 'dissolvedCopper_ugCu_l',
        'dissolvedIron_ugFe_l': 'dissolvedIron_ugFe_l',
        'dissolvedManganese_ugMn_l': 'dissolvedManganese_ugMn_l',
        'dissolvedZinc_ugZn_l': 'dissolvedZinc_ugZn_l',
        'dissolvedBoron_ugB_l': 'dissolvedBoron_ugB_l',
        'dissolvedMolybdenum_ugMo_l': 'dissolvedMolybdenum_ugMo_l',
        'dissolvedAluminum_mg_al_l': 'dissolvedAluminum_mg_al_l',
        'dissolvedSodium_mgNa_l': 'dissolvedSodium_mgNa_l',
        'dissolvedSilicon_mgSi_l': 'dissolvedSilicon_mgSi_l',
        'erosionSedimentSd_kg': 'erosionSedimentSd_kg',
        'erosionTotalSuspendedSolidsSd_kg': 'erosionTotalSuspendedSolidsSd_kg',
        'erosionTotalSolidsSd_kg': 'erosionTotalSolidsSd_kg',
        'soilOrganicMatterSd_mgSom_l': 'soilOrganicMatterSd_mgSom_l',
        'soilOrganicCarbonSd_mg_c_l': 'soilOrganicCarbonSd_mg_c_l',
        'waterSd_mm': 'waterSd_mm',
        'totalNitrogenSd_mg_l': 'totalNitrogenSd_mg_l',
        'totalPhosphorusSd_mg_l': 'totalPhosphorusSd_mg_l',
        'InorganicNitrogenSd_mg_l': 'InorganicNitrogenSd_mg_l',
        'nitrateSd_mg_l': 'nitrateSd_mg_l',
        'totalDissolvedNitrogenSd_mgN_l': 'totalDissolvedNitrogenSd_mgN_l',
        'totalDissolvedPhosphorusSd_mgP_l': 'totalDissolvedPhosphorusSd_mgP_l',
        'chlorideSd_mg_l': 'chlorideSd_mg_l',
        'phStd': 'phStd',
        'electricalConductivitySd_ms_cm': 'electricalConductivitySd_ms_cm',
        'dissolvedPotassiumSd_mgK_l': 'dissolvedPotassiumSd_mgK_l',
        'dissolvedSulfurSd_mgS_l': 'dissolvedSulfurSd_mgS_l',
        'dissolvedCalciumSd_mgCa_l': 'dissolvedCalciumSd_mgCa_l',
        'dissolvedMagnesiumSd_mgMg_l': 'dissolvedMagnesiumSd_mgMg_l',
        'dissolvedCopperSd_ugCu_l': 'dissolvedCopperSd_ugCu_l',
        'dissolvedIronSd_ugFe_l': 'dissolvedIronSd_ugFe_l',
        'dissolvedManganeseSd_ugMn_l': 'dissolvedManganeseSd_ugMn_l',
        'dissolvedZincSd_ugZn_l': 'dissolvedZincSd_ugZn_l',
        'dissolvedBoronSd_ugB_l': 'dissolvedBoronSd_ugB_l',
        'dissolvedMolybdenumSd_ugMo_l': 'dissolvedMolybdenumSd_ugMo_l',
        'dissolvedAluminumSd_mg_al_l': 'dissolvedAluminumSd_mg_al_l',
        'dissolvedSodiumSd_mgNa_l': 'dissolvedSodiumSd_mgNa_l',
        'dissolvedSiliconSd_mgSi_l': 'dissolvedSiliconSd_mgSi_l',
    }
    mappings['WaterQualityConc'] = measurements_water_quality_concentration_struct

    measurements_gas_nutrient_loss_struct = {
        '@fileName': raw_path + r'/measurements_gas_nutrient_loss_with_UID.csv',
        '@uniqueId': 'measGasNutrientLoss_UID',
        'measGasNutrientLoss_UID': 'measGasNutrientLoss_UID',
        'fieldId': 'fieldId',
        'expUnitId': 'expUnitId',
        'date': 'date',
        'time': 'time',
        'expUnit_UID': 'expUnit_UID',
        'treatmentId': 'treatmentId',
        'growthStage': 'growthStage',
        'crop': 'crop',
        'samplingStartStopInterval': 'samplingStartStopInterval',
        'modelIfSimulated': 'modelIfSimulated',
        'nitrousOxides_g_ha': 'nitrousOxides_g_ha',
        'nitrogenGas_g_ha': 'nitrogenGas_g_ha',
        'nitrousOxide_g_ha': 'nitrousOxide_g_ha',
        'ammoniaNitrogen_kg_ha': 'ammoniaNitrogen_kg_ha',
        'nitrousOxidesSd_g_ha': 'nitrousOxidesSd_g_ha',
        'nitrogenGasSd_g_ha': 'nitrogenGasSd_g_ha',
        'nitrousOxideSd_g_ha': 'nitrousOxideSd_g_ha',
        'ammoniaNitrogenSd_kg_ha': 'ammoniaNitrogenSd_kg_ha',
    }
    mappings['GasNutrientLoss'] = measurements_gas_nutrient_loss_struct
    

    # ---------relations------------- #

    '''
    
    objectProperty_struct = {
        '@fileName': raw_path + r'/file.csv'
        '@from': 'domainUniqueId',
        '@to': 'rangeUniqueId',
        'objectProperty': 'rangeUniqueId',
    }
    mappings['objectProperty'] = objectProperty_struct

    '''

    #Overview

    fundsExperiment_struct = {
        '@fileName': raw_path + r'/overview.csv',
        '@from': 'organizationName',
        '@to': 'projectName',
        'fundsExperiment': 'projectName',
    }
    mappings['fundsExperiment'] = fundsExperiment_struct

    happenedInSite_struct = {
        '@fileName': raw_path + r'/overview.csv',
        '@from': 'experimentName',
        '@to': 'siteId',
        'happenedInSite': 'siteId',
    }
    mappings['happenedInSite'] = happenedInSite_struct

    happenedAtResearchUnit_struct = {
        '@fileName': raw_path + r'/overview.csv',
        '@from': 'experimentName',
        '@to': 'researchUnitDescription',
        'happenedAtResearchUnit': 'researchUnitDescription',
    }
    mappings['happenedAtResearchUnit'] = happenedAtResearchUnit_struct

    #FieldSites

    hasCounty_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@from': 'stateProvince',
        '@to': 'countyName',
        'hasCounty': 'countyName',
    }
    mappings['hasCounty'] = hasCounty_struct

    hasState_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@from': 'countryName',
        '@to': 'stateProvince',
        'hasState': 'stateProvince',
    }
    mappings['hasState'] = hasState_struct
    
    hasCity_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@from': 'countyName',
        '@to': 'cityName',
        'hasCity': 'cityName',
    }
    mappings['hasCity'] = hasCity_struct


    hasField_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@from': 'siteId',
        '@to': 'fieldId',
        'hasField': 'fieldId',
    }
    mappings['hasField'] = hasField_struct

    locatedInCountry_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@from': 'siteId',
        '@to': 'countryName',
        'locatedInCountry': 'countryName',
    }
    mappings['locatedInCountry'] = locatedInCountry_struct

    locatedInState_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@from': 'siteId',
        '@to': 'stateProvince',
        'locatedInState': 'stateProvince',
    }
    mappings['locatedInState'] = locatedInState_struct

    locatedInCounty_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@from': 'siteId',
        '@to': 'countyName',
        'locatedInCounty': 'countyName',
    }
    mappings['locatedInCounty'] = locatedInCounty_struct

    locatedInCity_struct = {
        '@fileName': raw_path + r'/field_sites.csv',
        '@from': 'siteId',
        '@to': 'cityName',
        'locatedInCity': 'cityName',
    }
    mappings['locatedInCity'] = locatedInCity_struct
    
    #Persons

    worksFor_struct = {
        '@fileName': raw_path + r'/persons_with_UID.csv',
        '@from': 'persons_UID',
        '@to': 'organizationName',
        'worksFor': 'organizationName',
    }
    mappings['worksFor'] = worksFor_struct

    worksIn_struct = {
        '@fileName': raw_path + r'/persons_with_UID.csv',
        '@from': 'persons_UID',
        '@to': 'siteId',
        'worksIn': 'siteId',
    }
    mappings['worksIn'] = worksIn_struct

    worksAtDepartment_struct = {
        '@fileName': raw_path + r'/persons_with_UID.csv',
        '@from': 'persons_UID',
        '@to': 'departmentName',
        'worksAtDepartment': 'departmentName',
    }
    mappings['worksAtDepartment'] = worksAtDepartment_struct

    departmentOf_struct = {
        '@fileName': raw_path + r'/persons_with_UID.csv',
        '@from': 'departmentName',
        '@to': 'organizationName',
        'departmentOf': 'departmentName',
    }
    mappings['departmentOf'] = departmentOf_struct

    #Citations

    isPartOfPublication_struct = {
        '@fileName': raw_path + r'/citations.csv',
        '@from': 'identifier',
        '@to': 'bookName',
        'isChapterOf': 'bookName',
    }
    mappings['isChapterOf'] = isPartOfPublication_struct

    studiesSite_struct = {
        '@fileName': raw_path + r'/citations.csv',
        '@from': 'identifier',
        '@to': 'siteId',
        'studiesSite': 'siteId',
    }
    mappings['studiesSite'] = studiesSite_struct

    #Treatments

    hasTreatment_struct = {
        '@fileName': raw_path + r'/treatments.csv',
        '@from': 'experimentName',
        '@to': 'treatmentId',
        'hasTreatment': 'treatmentId',
    }
    mappings['hasTreatment'] = hasTreatment_struct

    hasRotation_struct = {
        '@fileName': raw_path + r'/treatments.csv',
        '@from': 'treatmentId',
        '@to': 'rotationDescriptor',
        'hasRotation': 'rotationDescriptor',
        }
    mappings['hasRotation'] = hasRotation_struct

    hasTillage_struct = {
        '@fileName': raw_path + r'/management_tillage_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'mgtTillage_UID',
        'hasTillage': 'mgtTillage_UID',
    }
    mappings['hasTillage'] = hasTillage_struct
    

    #ExperUnits

    locatedInField_struct = {
        '@fileName': raw_path + r'/experimental_units_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'fieldId',
        'locatedInField': 'fieldId',
    }
    mappings['locatedInField'] = locatedInField_struct

    appliedInField_struct = {
        '@fileName': raw_path + r'/experimental_units_with_UID.csv',
        '@from': 'soilClassification',
        '@to': 'fieldId',
        'appliedInField': 'fieldId'
    }
    mappings['appliedInField'] = appliedInField_struct

    usedInExpUnit_struct = {
        '@fileName': raw_path + r'/experimental_units_with_UID.csv',
        '@from': 'soilClassification',
        '@to': 'expUnit_UID',
        'usedInExpUnit': 'expUnit_UID'
    }
    mappings['usedInExpUnit'] = usedInExpUnit_struct

    #WeatherStation

    recordsWeatherForSite_struct = {
        '@fileName': raw_path + r'/weather_daily_with_UID.csv',
        '@from': 'weatherStationId',
        '@to': 'siteId',
        'recordsWeatherForSite': 'siteId',
    }
    mappings['recordsWeatherForSite'] = recordsWeatherForSite_struct

    recordsWeatherForField_struct = {
        '@fileName': raw_path + r'/weather_daily_with_UID.csv',
        '@from': 'weatherStationId',
        '@to': 'fieldId',
        'recordsWeatherForField': 'fieldId',
    }
    mappings['recordsWeatherForField'] = recordsWeatherForField_struct

    #WeatherDaily
    
    weatherRecordedBy_struct = {
        '@fileName': raw_path + r'/weather_daily_with_UID.csv',
        '@from': 'weatherStationId',
        '@to': 'weatherDaily_UID',
        'weatherRecordedBy': 'weatherDaily_UID',
    }
    mappings['weatherRecordedBy'] = weatherRecordedBy_struct

    weatherRecordedAt_struct = {
        '@fileName': raw_path + r'/weather_daily_with_UID.csv',
        '@from': 'weatherDaily_UID',
        '@to': 'siteId',
        'weatherRecordedAt': 'siteId',
    }
    mappings['weatherRecordedAt'] = weatherRecordedAt_struct

    weatherAtField_struct = {
        '@fileName': raw_path + r'/weather_daily_with_UID.csv',
        '@from': 'weatherDaily_UID',
        '@to': 'fieldId',
        'weatherAtField': 'fieldId',
    }
    mappings['weatherAtField'] = weatherAtField_struct

    #MgtAmendments

    hasAmendment_struct = {
        '@fileName': raw_path + r'/management_amendments_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'mgtAmendments_UID',
        'hasAmendment': 'mgtAmendments_UID',
    }
    mappings['hasAmendment'] = hasAmendment_struct

    hasPesticide_struct = {
        '@fileName': raw_path + r'/management_amendments_with_UID.csv',
        '@from': 'mgtAmendments_UID',
        '@to': 'pesticide_UID',
        'hasPesticide': 'pesticide_UID',
    }
    mappings['hasPesticide'] = hasPesticide_struct

    #MgtPlanting

    plantingAt_struct = {
        '@fileName': raw_path + r'/management_planting_with_UID.csv',
        '@from': 'mgtPlanting_UID',
        '@to': 'expUnit_UID',
        'plantingAt': 'expUnit_UID',
    }
    mappings['plantingAt'] = plantingAt_struct

    #MgtGrowthStages

    tracksGrowth_struct = {
        '@fileName': raw_path + r'/management_growth_stages_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'mgtGrowthStages_UID',
        'tracksGrowth': 'mgtGrowthStages_UID',
    }
    mappings['tracksGrowth'] = tracksGrowth_struct

    #MgtResidue

    hasResidueManagementEvent_struct = {
        '@fileName': raw_path + r'/management_residue_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'mgtResidue_UID',
        'hasResidueManagementEvent': 'mgtResidue_UID',
    }
    mappings['hasResidueManagementEvent'] = hasResidueManagementEvent_struct

    #MgtGrazing

    hasGrazingManagementEvent_struct = {
        '@fileName': raw_path + r'/management_grazing_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'mgtGrazing_UID',
        'hasGrazingManagementEvent': 'mgtGrazing_UID',
    }
    mappings['hasGrazingManagementEvent'] = hasGrazingManagementEvent_struct

    #MeasSoilPhys

    hasPhySample_struct = {
        '@fileName': raw_path + r'/measurements_soil_physical_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measSoilPhys_UID',
        'hasPhySample': 'measSoilPhys_UID',
    }
    mappings['hasPhySample'] = hasPhySample_struct

    appliedOnSoil_struct = {
        '@fileName': raw_path + r'/measurements_soil_physical.csv',
        '@from': 'treatmentId',
        '@to': 'soilClassification',
        'appliedOnSoil': 'soilClassification',
    }
    mappings['appliedOnSoil'] = appliedOnSoil_struct

    # MeasSoilChem
    hasChemSample_struct = {
        '@fileName': raw_path + r'/measurements_soil_chemical_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measSoilChem_UID',
        'hasChemSample': 'measSoilChem_UID',
    }
    mappings['hasChemSample'] = hasChemSample_struct


    chemSampleHasTreatment_struct = {
        '@fileName': raw_path + r'/measurements_soil_chemical_with_UID.csv',
        '@from': 'measSoilChem_UID',
        '@to': 'treatmentId',
        'chemSampleHasTreatment': 'treatmentId',
    }
    mappings['chemSampleHasTreatment'] = chemSampleHasTreatment_struct


    # MeasSoilBiol
    hasBioSample_struct = {
        '@fileName': raw_path + r'/measurements_soil_biological_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measSoilBiol_UID',
        'hasBioSample': 'measSoilBiol_UID',
    }
    mappings['hasBioSample'] = hasBioSample_struct

    #MeasGHGFlux

    hasGasSample_struct = {
        '@fileName': raw_path + r'/measurements_greenhouse_gases_flux_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measGHGFlux_UID',
        'hasGasSample': 'measGHGFlux_UID',
    }
    mappings['hasGasSample'] = hasGasSample_struct

    #MeasResidueMgnt

    isHarvested_struct = {
        '@fileName': raw_path + r'/measurements_residue_management_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measResidueMgnt_UID',
        'isHarvested': 'measResidueMgnt_UID',
    }
    mappings['isHarvested'] = isHarvested_struct

    #MeasHarvestFraction

    hasHarvestFractionData_struct = {
        '@fileName': raw_path + r'/measurements_harvest_fraction_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measHarvestFraction_UID',
        'hasHarvestFractionData': 'measHarvestFraction_UID',
    }
    mappings['hasHarvestFractionData'] = hasHarvestFractionData_struct

    #MeasBiomassCHO

    hasBioMassCarbohydrateData_struct = {
        '@fileName': raw_path + r'/measurements_biomass_cho_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measBiomassCHO_UID',
        'hasBioMassCarbohydrateData': 'measBiomassCHO_UID',
    }
    mappings['hasBioMassCarbohydrateData'] = hasBioMassCarbohydrateData_struct

    #MeasBiomassEnergy

    hasBioMassEnergyData_struct = {
        '@fileName': raw_path + r'/measurements_biomass_energy_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measBiomassEnergy_UID',
        'hasBioMassEnergyData': 'measBiomassEnergy_UID',
    }
    mappings['hasBioMassEnergyData'] = hasBioMassEnergyData_struct

    #MeasBiomassMinAn

    hasBioMassMineralData_struct = {
        '@fileName': raw_path + r'/measurements_biomass_mineral_analysis_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measBiomassMinAn_UID',
        'hasBioMassMineralData': 'measBiomassMinAn_UID',
    }
    mappings['hasBioMassMineralData'] = hasBioMassMineralData_struct

    #MeasGrazingPlants

    hasGrazingData_struct = {
        '@fileName': raw_path + r'/measurements_grazing_plants_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measGrazingPlants_UID',
        'hasGrazingData': 'measGrazingPlants_UID',
    }
    mappings['hasGrazingData'] = hasGrazingData_struct

    #MeasSuppRes

    hasMiscellaneousMeasurement_struct = {
        '@fileName': raw_path + r'/measurements_supporting_research_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'miscellaneousMeasurementUniqueId',
        'hasMiscellaneousMeasurement': 'miscellaneousMeasurementUniqueId',
    }
    mappings['hasMiscellaneousMeasurement'] = hasMiscellaneousMeasurement_struct

    hasGasNutrientData_struct = {
        '@fileName': raw_path + r'/measurements_gas_nutrient_loss_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measGasNutrientLoss_UID',
        'hasGasNutrientData': 'measGasNutrientLoss_UID',
    }
    mappings['hasGasNutrientData'] = hasGasNutrientData_struct

    GasNutrientDataAt_struct = {
        '@fileName': raw_path + r'/measurements_gas_nutrient_loss_with_UID.csv',
        '@from': 'measGasNutrientLoss_UID',
        '@to': 'fieldId',
        'gasNutrientDataAt': 'measGasNutrientLoss_UID',
    }
    mappings['gasNutrientDataAt'] = GasNutrientDataAt_struct

    GasNutrientTreatment_struct = {
        '@fileName': raw_path + r'/measurements_gas_nutrient_loss_with_UID.csv',
        '@from': 'measGasNutrientLoss_UID',
        '@to': 'treatmentId',
        'gasNutrientTreatment': 'measGasNutrientLoss_UID',
    }
    mappings['gasNutrientTreatment'] = GasNutrientTreatment_struct

    hasNutrientEffData_struct = {
        '@fileName': raw_path + r'/measurements_nutrient_efficiency_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measNutrEff_UID',
        'hasNutrientEffData': 'measNutrEff_UID',
    }
    mappings['hasNutrientEffData'] = hasNutrientEffData_struct

    NutrientEffDataAt_struct = {
        '@fileName': raw_path + r'/measurements_nutrient_efficiency_with_UID.csv',
        '@from': 'measNutrEff_UID',
        '@to': 'fieldId',
        'nutrientEffDataAt': 'measNutrEff_UID',
    }
    mappings['nutrientEffDataAt'] = NutrientEffDataAt_struct

    NutrientEffTreatment_struct = {
        '@fileName': raw_path + r'/measurements_nutrient_efficiency_with_UID.csv',
        '@from': 'measNutrEff_UID',
        '@to': 'treatmentId',
        'nutrientEffTreatment': 'measNutrEff_UID',
    }
    mappings['nutrientEffTreatment'] = NutrientEffTreatment_struct

    hasWaterQualityAreaData_struct = {
        '@fileName': raw_path + r'/measurements_water_quality_area_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measWaterQualityArea_UID',
        'hasWaterQualityAreaData': 'measWaterQualityArea_UID',
    }
    mappings['hasWaterQualityAreaData'] = hasWaterQualityAreaData_struct

    WaterQualityAreaDataAt_struct = {
        '@fileName': raw_path + r'/measurements_water_quality_area_with_UID.csv',
        '@from': 'measWaterQualityArea_UID',
        '@to': 'fieldId',
        'waterQualityAreaDataAt': 'measWaterQualityArea_UID',
    }
    mappings['waterQualityAreaDataAt'] = WaterQualityAreaDataAt_struct

    WaterQualityAreaTreatment_struct = {
        '@fileName': raw_path + r'/measurements_water_quality_area_with_UID.csv',
        '@from': 'measWaterQualityArea_UID',
        '@to': 'treatmentId',
        'waterQualityAreaTreatment': 'measWaterQualityArea_UID',
    }
    mappings['waterQualityAreaTreatment'] = WaterQualityAreaTreatment_struct

    hasWaterQualityConcData_struct = {
        '@fileName': raw_path + r'/measurements_water_quality_concentration_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measWaterQualityConc_UID',
        'hasWaterQualityConcData': 'measWaterQualityConc_UID',
    }
    mappings['hasWaterQualityConcData'] = hasWaterQualityConcData_struct

    WaterQualityConcDataAt_struct = {
        '@fileName': raw_path + r'/measurements_water_quality_concentration_with_UID.csv',
        '@from': 'measWaterQualityConc_UID',
        '@to': 'fieldId',
        'waterQualityConcDataAt': 'measWaterQualityConc_UID',
    }
    mappings['waterQualityConcDataAt'] = WaterQualityConcDataAt_struct

    WaterQualityConcTreatment_struct = {
        '@fileName': raw_path + r'/measurements_water_quality_concentration_with_UID.csv',
        '@from': 'measWaterQualityConc_UID',
        '@to': 'treatmentId',
        'waterQualityConcTreatment': 'measWaterQualityConc_UID',
    }
    mappings['waterQualityConcTreatment'] = WaterQualityConcTreatment_struct

    hasWindErosionData_struct = {
        '@fileName': raw_path + r'/measurements_wind_erosion_area_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measWindErosionArea_UID',
        'hasWindErosionData': 'measWindErosionArea_UID',
    }
    mappings['hasWindErosionData'] = hasWindErosionData_struct

    WindErosionDataAt_struct = {
        '@fileName': raw_path + r'/measurements_wind_erosion_area_with_UID.csv',
        '@from': 'measWindErosionArea_UID',
        '@to': 'fieldId',
        'windErosionDataAt': 'measWindErosionArea_UID',
    }
    mappings['windErosionDataAt'] = WindErosionDataAt_struct

    WindErosionTreatment_struct = {
        '@fileName': raw_path + r'/measurements_wind_erosion_area_with_UID.csv',
        '@from': 'measWindErosionArea_UID',
        '@to': 'treatmentId',
        'windErosionTreatment': 'measWindErosionArea_UID',
    }
    mappings['windErosionTreatment'] = WindErosionTreatment_struct

    hasYieldNutrUptakeData_struct = {
        '@fileName': raw_path + r'/measurements_yield_nutrient_uptake_with_UID.csv',
        '@from': 'expUnit_UID',
        '@to': 'measYieldNutUptake_UID',
        'hasYieldNutrUptakeData': 'measYieldNutUptake_UID',
    }
    mappings['hasYieldNutrUptakeData'] = hasYieldNutrUptakeData_struct

    YieldNutrUptakeDataAt_struct = {
        '@fileName': raw_path + r'/measurements_yield_nutrient_uptake_with_UID.csv',
        '@from': 'measYieldNutUptake_UID',
        '@to': 'fieldId',
        'yieldNutrUptakeDataAt': 'measYieldNutUptake_UID',
    }
    mappings['yieldNutrUptakeDataAt'] = YieldNutrUptakeDataAt_struct

    YieldNutrUptakeTreatment_struct = {
        '@fileName': raw_path + r'/measurements_yield_nutrient_uptake_with_UID.csv',
        '@from': 'measYieldNutUptake_UID',
        '@to': 'treatmentId',
        'yieldNutrUptakeTreatment': 'measYieldNutUptake_UID',
    }
    mappings['yieldNutrUptakeTreatment'] = YieldNutrUptakeTreatment_struct


    return mappings


# read the onto and generate cypher
classes_and_props_query = """
    prefix owl: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT DISTINCT ?class (GROUP_CONCAT(DISTINCT ?propTypePair ; SEPARATOR=",") AS ?props)
    WHERE {
        ?class rdf:type owl:Class .
        optional {
            ?prop rdfs:domain ?class ;
            a owl:DatatypeProperty ;
            rdfs:range ?range .
            BIND (concat(str(?prop),';',str(?range)) AS ?propTypePair)
        }
    } GROUP BY ?class
"""

relations_query = """
    prefix owl: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT DISTINCT ?rel ?dom ?ran #(GROUP_CONCAT(DISTINCT ?relTriplet ; SEPARATOR=",") AS ?rels)
    WHERE {
        ?rel a ?propertyClass .
        filter(?propertyClass in (rdf:Property, owl:ObjectProperty, owl:FunctionalProperty, owl:AsymmetricProperty, 
            owl:InverseFunctionalProperty, owl:IrreflexiveProperty, owl:ReflexiveProperty, owl:SymmetricProperty, owl:TransitiveProperty))
        ?rel rdfs:domain ?dom ;
            rdfs:range ?ran .
        #BIND (concat(str(?rel),';',str(?dom),';',str(?range)) AS ?relTriplet)
    }
"""

check_duplicate_nodes_query = """
MATCH (n:{nodeType})
WHERE n.{uniqueProperty} = $record.{sourceProperty}
RETURN n
"""
