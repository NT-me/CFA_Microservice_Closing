import sqlite3 as sql
import json
import datetime as dt


FLAG_CHANGE_SUCCESS = 1
FLAG_CHANGE_FAIL = 0

def initDB():
    conn = sql.connect('DB/dataBase.db')

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
    conn = sql.connect('DB/dataBase.db')

    cursor = conn.cursor()
    req0 = "SELECT close, timestamp, user  FROM \"closingContract\" WHERE key LIKE \"{0}\" ".format(idContract)
    cursor.execute(req0)
    ret = cursor.fetchall()

    res = dict()

    if len(ret) > 0:
        # Cas où il trouve
        res["timestamp"] = ret[0][1]
        res["user"] = ret[0][2]
        if(ret[0][0] == 0):
            # Cas où le contrat n'est PAS fermé

            # Signe un contrat
            req1 = "UPDATE \"closingContract\" SET close = 1 WHERE key LIKE \"{0}\"".format(idContract)
            cursor.execute(req1)
            conn.commit()

            # Met a jour le timestamp
            req2 = "UPDATE \"closingContract\" SET timestamp = {1} WHERE key LIKE \"{0}\"".format(idContract, int(dt.datetime.now().timestamp()))
            cursor.execute(req2)
            conn.commit()

            # Met a jour le signataire
            req3 = "UPDATE \"closingContract\" SET user = \"{1}\" WHERE key LIKE \"{0}\"".format(idContract, username)
            cursor.execute(req3)
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


def allContracts():
    """
    Permet de rechercher dans la base de donnée tous les contrats signés ou a
    signé avec leurs clefs fonctionnelles.

    Return :
        res -> dict : Dictionnaire de dictionnaire avec tous les contrats et leur info
    """
    conn = sql.connect('DB/dataBase.db')

    cursor = conn.cursor()
    req0 = "SELECT key, close, timestamp, user  FROM \"closingContract\""
    cursor.execute(req0)
    ret = cursor.fetchall()
    res = dict()

    for contract in ret:
        res[contract[0]] = dict()
        res[contract[0]]["status"] = contract[1]
        res[contract[0]]["timestamp"] = contract[2]
        res[contract[0]]["user"] = contract[3]

    return res


def searchContractByKey(idContract):
    """
    Permet de rechercher dans la base de donnée un contrat signé ou a signé avec
    sa clef fonctionnelle.

    Params :
        idContract -> str : Clef fonctionnelle

    Return :
        res -> dict : Permet de retourner toutes les informations nécessaires
        -1 -> int : Erreur
    """
    conn = sql.connect('DB/dataBase.db')
    
    cursor = conn.cursor()
    req0 = "SELECT close, timestamp, user  FROM \"closingContract\" WHERE key LIKE \"{0}\" ".format(idContract)
    cursor.execute(req0)
    ret = cursor.fetchall()
    res = dict()

    if len(ret) > 0:
        res["status"] = ret[0][0]
        res["timestamp"] = ret[0][1]
        res["user"] = ret[0][2]

    else:
        return -1

    return res


def createCloseConstract(idContract):
    """
    Cette fonction permet de vérifier si un contrat à signer OU signé est déjà présent
    dans notre base de données.
    S'il ne l'est pas l'ajoute avec des valeurs par défaut

    Params :
        idContract -> str : Clef fonctionnelle du contrat

    Return :
        True : Le contrat existe déjà
        False : Le contrat a été ajouté avec des valeurs par défaut
    """

    conn = sql.connect('DB/dataBase.db')
    cursor = conn.cursor()
    req0 = "SELECT id  FROM \"closingContract\" WHERE key LIKE \"{0}\" ".format(idContract)
    cursor.execute(req0)
    ret = cursor.fetchall()

    if len(ret) > 0:
        # Si le contrat est déjà présent dans notre base de donnée
        return True
    else:
        # Si le contrat n'existe pas encore dans notre base de donnée
        # On le créer avec les valeurs par défaut
        ts = int(dt.datetime.now().timestamp())
        req1 = "INSERT INTO \"closingContract\" (key, timestamp, close)  VALUES (\"{0}\", {1}, 0)".format(idContract, ts)
        print(req1)
        cursor.execute(req1)
        conn.commit()
        return False
