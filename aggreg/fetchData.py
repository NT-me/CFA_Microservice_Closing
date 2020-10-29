# Author : David Herzog

import requests
import json


""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Récupération du data à aggréger chez les autres services
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# TODO
""" 
    Deal:
    - contenu json

    Facility:
    - url get
    - contenu json

    Assurance:
    - url get
    - contenu json
"""

""" retourne le Deal sous forme de dict()
    
    nom
    montant
    zone
    devise
    borrower
    lender
    status
"""
def fetchDealById(id):
    path = "api/v1/deals/" + str(id)
    res_json = requests.get(path)
    res_dict = json.loads(res_json)
    return res_dict

""" retourne tous les Deals sous forme de dict()
    
    code
    nom
    montant
    zone
    devise
    borrower
    lender
    status
"""
def fetchAllDeals():
    path = "api/v1/deals"
    res_json = requests.get(path)
    res_dict = json.loads(res_json)
    return res_dict

""" retourne l'Assurance sous forme de dict()

    nom
    pourcentage
"""
def fetchInsuranceById(id):
    path = "api/???/" + str(id)
    res_json = requests.get(path)
    res_dict = json.loads(res_json)
    return res_dict

""" retourne toutes les Assurances sous forme de dict()

    code
    nom
    pourcentage
"""
def fetchAllInsurances():
    path = "api/???"
    res_json = requests.get(path)
    res_dict = json.loads(res_json)
    return res_dict


""" retourne la Facilité sous forme de dict()

    nom
    facility_code
    amount
    devise
    entities :  [
                    [name, calendar, percentage],
                    [name, calendar, percentage],
                    ...
                ]
"""
def fetchFacilityById(id):
    path = "api/v1/facilities/" + str(id)
    res_json = requests.get(path)
    res_dict = json.loads(res_json)
    return res_dict

""" retourne la Facilité sous forme de dict()

    deal_code
    nom
    facility_code
    amount
    devise
    entities :  [
                    [name, calendar, percentage],
                    [name, calendar, percentage],
                    ...
                ]
"""
def fetchAllFacilities():
    path = "api/v1/facilities"
    res_json = requests.get(path)
    res_dict = json.loads(res_json)
    return res_dict

