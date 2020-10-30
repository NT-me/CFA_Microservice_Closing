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

        Return :
            -1 : si le deal n'existe pas
            sinon : {
                        'status_facility' : 1 ou -1
                        'status_insurance' : 1 ou -1
                        'status_closer' : 1 ou -1

            }
    """

    dict_deal = fd.fetchDealById( id )              # dico deal
    # erreur si deal n'existe pas
    if dict_deal == -1:
        return -1

    dict_facility = fd.fetchFacilityById( id )      # dico faciliy
    dict_insurance = fd.fetchInsuranceById( id )    # dico insurance
    dict_closer = wdb.searchContractByKey( id )     # dico closer

    wdb.createCloseConstract( id )    # remplissage de la BD closer (si le deal existe)

    # aggreg
    dict_contract = ag.aggregation( dict_deal, dict_facility, dict_insurance, dict_closer )

    # dict -> json
    contract_json = json.dumps(dict_contract)

    dict_res_contract = dict()
    dict_res_contract['status_facility'] = ( -1 if dict_facility==-1 else 1 )
    dict_res_contract['status_insurance'] = ( -1 if dict_insurance==-1 else 1 )
    dict_res_contract['status_closer'] = ( -1 if dict_closer==-1 else 1 )
    dict_res_contract['contract_json'] = contract_json
    return dict_res_contract



def getAllContracts():
    """ retourne la liste de tous les contrats en format json
    """
    dict_contracts = dict()

    # fetch all data
    list_dict_deals = fd.fetchAllDeals()
    list_dict_facilities = fd.fetchAllFacilities()
    list_dict_insurances = fd.fetchAllInsurances()
    dict_dict_closer = wdb.allContracts()

    # then filter the ones with the corresponding 'code'
    for dict_deal in list_dict_deals:
        code = dict_deal['code']
        wdb.createCloseConstract( code )    # remplissage de la BD closer
        dict_facility = [ dict_facility for dict_facility in list_dict_facilities if dict_facility['deal_code']==code ][0]
        dict_insurance =  [ dict_insurance for dict_insurance in list_dict_insurances if dict_insurance['insurance_code']==code][0]
        dict_closer = dict_dict_closer[code]

        # and finally, put them all together in a contract and add it to 'dict_contracts'
        dict_contract = ag.aggregation( dict_deal, dict_facility, dict_insurance, dict_closer )
        dict_contracts[code] = dict_contract

    return dict_contracts