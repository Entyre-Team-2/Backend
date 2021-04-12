from requests.auth import HTTPBasicAuth
import requests

med_names = []
drugbank_ids = []

for i in range(2):
    med_name = input("What medicine are you taking?")
    med_names.append(med_name)
    single_med_url = "https://api.drugbank.com/v1/drug_names?q=" + med_name
    req_1 = requests.get(single_med_url, headers={'Authorization': '310bffd2cf2be1608045231355596b19'}, json={'key': 'value'})
    json_response = req_1.json()
    drugbank_id = json_response["products"][0]["ingredients"][0]["drugbank_id"]
    drugbank_ids.append(drugbank_id)
    print("The details of the medicine are:  ")
    print(json_response)
    adverse_answer = input(
        "Would you like to know the adverse affects? (y/n) ")
    if (adverse_answer == "y" or adverse_answer == "Y"):
        adverse_affects_url = "https://api.drugbank.com/v1/drugs/" + \
            drugbank_id + "/adverse_effects"
        req_2 = requests.get(
            adverse_affects_url, headers={'Authorization': '310bffd2cf2be1608045231355596b19'}, json={'key': 'value'})
        print(req_2.json())


ddi_answer = input("Would you like to know how these 2 drugs interact?")
if(ddi_answer == "y" or ddi_answer == "Y"):
    ddi_url = "https://api.drugbank.com/v1/ddi?drugbank_id=" + \
        drugbank_ids[0] + "," + drugbank_ids[1] + "&include_references=true"
    req_3 = requests.get(ddi_url, headers={
                         'Authorization': '310bffd2cf2be1608045231355596b19'}, json={'key': 'value'})
    print(req_3.json())
