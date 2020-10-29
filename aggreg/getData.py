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
    pass