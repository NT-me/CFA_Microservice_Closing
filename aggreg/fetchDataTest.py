# Author : David Herzog

import requests
import json


### ======================= version test ===========================

res_deal_id =  {                                \
                    "code": "J123456",          \
                    "name": "toto",             \
                    "amount": 1000.0,           \
                    "zone": "AMER",             \
                    "devise": "EURO",           \
                    "borrower": "CFA INSTA",    \
                    "lender": "BNP",            \
                    "status": "STRUCTURING"     \
                }

res_facility_id = {                                                      \
                    "deal_code": "J123456",                              \
                    "facilities": [                                      \
                                    {                                    \
                                    "id": 42,                            \
                                    "name": "myName",                    \
                                    "facilityCode": "F123456",           \
                                    "dealCode": "J123456",               \
                                    "amount": 1234,                      \
                                    "devise": "Euro"                     \
                                    }                                    \
                                ]                                        \
                    }

res_insurance_id =    [                                 \
                        {                               \
                            "id_facilite": "999",       \
                            "name": "test6",            \
                            "percentage": 0.7           \
                        },                              \
                        {                               \
                            "id_facilite": "999",       \
                            "name": "test put",         \
                            "percentage": 0.12          \
                        },                              \
                        {                               \
                            "id_facilite": "999",       \
                            "name": "test put2",        \
                            "percentage": 0.99          \
                        }                               \
                    ]


res_deal_all = [                                    \
                    {                               \
                        "code": "J123456",          \
                        "name": "toto",             \
                        "amount": 1000.0,           \
                        "zone": "AMER",             \
                        "devise": "EURO",           \
                        "borrower": "CFA INSTA",    \
                        "lender": "BNP",            \
                        "status": "STRUCTURING"     \
                    },                              \
                    {                               \
                        "code": "J123456",          \
                        "name": "toto",             \
                        "amount": 1000.0,           \
                        "zone": "AMER",             \
                        "devise": "EURO",           \
                        "borrower": "CFA INSTA",    \
                        "lender": "BNP",            \
                        "status": "STRUCTURING"     \
                    }                               \
                ]

res_facility_all =  [
                        {                                                        \
                            "deal_code": "J123456",                              \
                            "facilities": [                                      \
                                            {                                    \
                                            "id": 42,                            \
                                            "name": "myName",                    \
                                            "facilityCode": "F123456",           \
                                            "dealCode": "J123456",               \
                                            "amount": 1234,                      \
                                            "devise": "Euro"                     \
                                            }                                    \
                                        ]                                        \
                            },                                                   \
                            {                                                    \
                            "deal_code": "J123457",                              \
                            "facilities": [                                      \
                                            {                                    \
                                            "id": 43,                            \
                                            "name": "myName2",                   \
                                            "facilityCode": "F123457",           \
                                            "dealCode": "J123457",               \
                                            "amount": 12345,                     \
                                            "devise": "Dollar"                   \
                                            }                                    \
                                        ]                                        \
                            }                                                    \
                    ]

res_insurance_all = [                                       \
                        [                                   \
                            {                               \
                                "id_facilite": 42,          \
                                "name": "test6",            \
                                "percentage": 0.7           \
                            },                              \
                            {                               \
                                "id_facilite": "999",       \
                                "name": "test put",         \
                                "percentage": 0.12          \
                            },                              \
                            {                               \
                                "id_facilite": "999",       \
                                "name": "test put2",        \
                                "percentage": 0.99          \
                            }                               \
                        ],                                  \
                        [                                   \
                            {                               \
                                "id_facilite": "222",       \
                                "name": "test6",            \
                                "percentage": 0.7           \
                            },                              \
                            {                               \
                                "id_facilite": "222",       \
                                "name": "test put",         \
                                "percentage": 0.12          \
                            },                              \
                            {                               \
                                "id_facilite": "222",       \
                                "name": "test put2",        \
                                "percentage": 0.99          \
                            }                               \
                        ]                                   \
                    ]                           

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
    return res_deal_id


def fetchAllDeals():
    """ retourne tous les Deals sous forme de liste de dict()
        code, nom, montant, zone, devise, borrower, lender, status
    """
    return res_deal_all


def fetchInsuranceById( id ):
    """ retourne l'Assurance sous forme de dict()
        nom, pourcentage
    """
    return res_insurance_id

def fetchAllInsurances():
    """ retourne toutes les Assurances sous forme de liste de dict()
        code, nom, pourcentage
    """
    return res_insurance_all


def fetchFacilityById( id ):
    """ retourne la Facilité sous forme de dict()
        nom, facility_code, amount, devise, entities :  [
                                                            [name, calendar, percentage],
                                                            [name, calendar, percentage],
                                                            ...
                                                        ]
    """
    return res_facility_id

def fetchAllFacilities():
    """ retourne toutes les Facilités sous forme de liste de dict()
        deal_code, nom, facility_code, amount, devise, entities :   [
                                                                        [name, calendar, percentage],
                                                                        [name, calendar, percentage],
                                                                        ...
                                                                    ]
    """
    return res_facility_all