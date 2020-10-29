import sqlite3 as sql
import json

conn = sql.connect('DB/dataBase.db')

FLAG_CHANGE_SUCCESS = 1
FLAG_CHANGE_FAIL = 0

def initDB():
    with open('DB/create_instruct.json') as json_file:
        cr_in = json.load(json_file)
    for i in cr_in:
        cursor = conn.cursor()
        script = cr_in[i]
        cursor.execute(script)
        conn.commit()
    return True


def updateStateClose(idContract, username):
    """
    Params :
    idContract -> str : Représente le contrat
    username -> str : Représente l'utilisateur
    """
    cursor = conn.cursor()
    req0 = "SELECT close, timestamp, user  FROM \"closingContract\" WHERE key LIKE \"{0}\" ".format(idContract)
    cursor.execute(req0)
    ret = cursor.fetchall()

    res = dict()
    res["timestamp"] = ret[0][1]
    res["user"] = ret[0][2]

    if len(ret) > 0:
        # Cas où il trouve
        if(ret[0][0] == 0):
            # Cas où le contrat n'est PAS fermé
            req1 = "UPDATE \"closingContract\" SET close = 1 WHERE key LIKE \"{0}\"".format(idContract)
            cursor.execute(req1)
            conn.commit()
            res["change_success"] = FLAG_CHANGE_SUCCESS
            return res
        elif (ret[0][0] == 1):
            # Cas où le contrat est fermé
            res["change_success"] = FLAG_CHANGE_FAIL
            return res
        else:
            # Wat
            return -1
    else:
        # Cas où il ne trouve pas
        return -1

    print(ret)



def allContracts():
    pass


def searchContractByKey(key):
    pass
