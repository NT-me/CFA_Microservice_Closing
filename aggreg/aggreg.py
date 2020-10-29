# Author : David Herzog

import json


""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Aggrégation du data
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



def aggregation( dict_deal, dict_facility, dict_insurance, dict_closer ):
    """ retourne un dict() du contract, aggrégé
        @param      dict_deal:          dico du deal
        @param      dict_facility:      dico de la facilité
        @param      dict_insurance:     dico de l'assurance
        @param      dict_closer:        dico du closer
    """
    dict_contract = dict()
    dict_contract['deal'] = dict_deal
    dict_contract['facility'] = dict_facility
    dict_contract['insurance'] = dict_insurance
    dict_contract['closer'] = dict_closer
    return dict_contract

