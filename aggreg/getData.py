# Author : David Herzog

import json
from . import fetchData as fd
from . import aggreg as ag
from DB import wrapperDB as wdb


""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     Transmission du data aggrégé
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



def getContractById( id ):
    """ retourne le contrat spécifique en format json
        @param :    id      String avec le deal-code (clé fonctionnelle)
    """

    wdb.createCloseConstract( id )    # remplissage de la BD closer

    dict_deal = fd.fetchDealById( id )              # dico deal
    dict_facility = fd.fetchFacilityById( id )      # dico faciliy
    dict_insurance = fd.fetchInsuranceById( id )    # dico insurance
    dict_closer = wdb.searchContractByKey( id )     # dico closer

    # aggreg
    dict_contract = ag.aggregation( dict_deal, dict_facility, dict_insurance, dict_closer )

    # dict -> json
    contract_json = json.dumps(dict_contract)
    return contract_json



def getAllContracts():
    """ retourne la liste de tous les contrats en format json
    """
    dict_contracts = dict()

    list_dict_deals = fd.fetchAllDeals()
    list_dict_facilities = fd.fetchAllFacilities()
    list_dict_insurances = fd.fetchAllInsurances()
    dict_dict_closer = wdb.allContracts()


    for dict_deal in list_dict_deals:
        code = dict_deal['code']
        wdb.createCloseConstract( code )    # remplissage de la BD closer
        dict_facility = ( dict_facility for dict_facility in list_dict_facilities if dict_facility['deal_code']==code )
        dict_insurance = ( dict_insurance for dict_insurance in list_dict_insurances if dict_insurance['insurance_code']==code )
        dict_closer = dict_dict_closer[code]

        # end_for
        dict_contract = ag.aggregation( dict_deal, dict_facility, dict_insurance, dict_closer )
        dict_contracts[code] = dict_contract

    return dict_contracts

    