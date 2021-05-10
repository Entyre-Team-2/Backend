import pandas as pd 
import numpy as np 
import math as math
from math import isnan
import json,requests #For getting the data from the drugbank api 

def get_risk(pos_inter):
    col_1_medicines = list()
    col_2_medicines = list()
    col_3_risk_scores = list()
    
    for combination in pos_inter:
        med_1_full = combination[0]
        med_2_full = combination[1]
        
        # adding the medicine names to the column lists 
        #col_1_medicines.append(med_1)
        #col_2_medicines.append(med_2)
        
        # Only using the first four letters of the medicine name 
        med_1 = med_1_full[0:4]
        med_2 = med_2_full[0:4]
        
        # API Access
        API_KEY = "310bffd2cf2be1608045231355596b19" # paste your API key here
        HEADERS = {
            'authorization': API_KEY
        }

        # Getting product_concept_ids
        url = "https://api.drugbank.com/v1/us/product_concepts"

        # For first medicine
        drug_1 = med_1
        param = {'q': drug_1}

        response = requests.get(url, params=param, headers=HEADERS)
        data_1 = response.json()
        data_1_list = list(data_1)
        
        if len(data_1_list) == 0:
            continue
        drug_1_pcid = data_1_list[0]['drugbank_pcid']

        # For Second medicine
        drug_2 = med_2
        param = {'q': drug_2}

        response = requests.get(url, params=param, headers=HEADERS)
        data_2 = response.json()
        data_2_list = list(data_2)
        if len(data_2_list) == 0:
            continue
        drug_2_pcid = data_2_list[0]['drugbank_pcid']
        
        # adding the medicine names to the column lists 
        col_1_medicines.append(med_1_full)
        col_2_medicines.append(med_2_full)

        # Drug-Drug Interaction lookup
        inter_pcid = drug_1_pcid + ',' + drug_2_pcid

        url = "https://api.drugbank.com/v1/us/ddi"
        param = {"product_concept_id": inter_pcid}
        response3 = requests.get(url, params=param, headers=HEADERS)
        result_ddi_data = response3.json()
        ddi_dict = dict(result_ddi_data)
        
        if ddi_dict['total_results'] == 0:
            risk = 0
        elif ddi_dict['interactions'][0]['severity'] == "minor":
            risk = 1
        elif ddi_dict['interactions'][0]['severity'] == "moderate":
            risk = 2
        else: 
            risk = 3
            
        col_3_risk_scores.append(risk)
        
    data_dict = {'Medicine 1': col_1_medicines,'Medicine 2': col_2_medicines, 'Degree of Risk': col_3_risk_scores}
    risk_df = pd.DataFrame.from_dict(data_dict)
    
    return risk_df

def aggregate_risk(df):
    def conditions(s):
        if s['Degree of Risk'] == 0:
            return 0
        elif s['Degree of Risk'] == 1:
            return 25 
        elif s['Degree of Risk'] == 2:
            return 50 
        else:
            return 75

    df['Numeric Risk'] = df.apply(conditions,axis = 1)
    df = df.sort_values(by = 'Numeric Risk',ascending=False)
    overall_risk = df['Numeric Risk'].mean()
    
    return df,overall_risk