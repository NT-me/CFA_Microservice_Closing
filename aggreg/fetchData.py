# Author : David Herzog

import requests
import json


""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Récupération du data à aggréger chez les autres services
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

END_POINT = ""
PATH_DEALS = END_POINT + "/v1/deals"
PATH_FACILITIES = END_POINT + "/v1/facilities"
PATH_INSURANCES = END_POINT + "/insurance"

def fetchDataById( path, id ):
    response = requests.get( path + "/" + str(id) )
    return ( -1 if response.status_code != 200 else response.json() )

def fetchDealById( id ):
    """ retourne le Deal sous forme de dict()
        nom, montant, zone, devise, borrower, lender, status
    """
    response = fetchDataById( PATH_DEALS, id )
    return ( -1 if response==-1 else response )


def fetchAllDeals():
    """ retourne tous les Deals sous forme de liste de dict()
        code, nom, montant, zone, devise, borrower, lender, status
    """
    res_json = requests.get( PATH_DEALS )
    res_dict = json.loads( res_json )
    return res_dict


def fetchInsuranceById( id ):
    """ retourne l'Assurance sous forme de dict()
        nom, pourcentage
    """
    response = fetchDataById( PATH_INSURANCES, id )
    return ( -1 if response==-1 else response )

def fetchAllInsurances():
    """ retourne toutes les Assurances sous forme de liste de dict()
        code, nom, pourcentage
    """
    res_json = requests.get( PATH_INSURANCES )
    res_dict = json.loads( res_json )
    return res_dict


def fetchFacilityById( id ):
    """ retourne la Facilité sous forme de dict()
        nom, facility_code, amount, devise, entities :  [
                                                            [name, calendar, percentage],
                                                            [name, calendar, percentage],
                                                            ...
                                                        ]
    """
    response = fetchDataById( PATH_FACILITIES, id )
    return ( -1 if response==-1 else response )

def fetchAllFacilities():
    """ retourne toutes les Facilités sous forme de liste de dict()
        deal_code, nom, facility_code, amount, devise, entities :   [
                                                                        [name, calendar, percentage],
                                                                        [name, calendar, percentage],
                                                                        ...
                                                                    ]
    """
    res_json = requests.get( PATH_FACILITIES )
    res_dict = json.loads( res_json )
    return res_dict