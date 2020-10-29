import sqlite3 as sql
import json
import datetime as dt

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
    cursor = conn.cursor()
    req0 = "SELECT key, close, timestamp, user  FROM \"closingContract\""
    cursor.execute(req0)
    ret = cursor.fetchall()
    res = dict()

    for contract in ret:
        res[ret[0][0]] = dict()
        res[ret[0][0]]["status"] = ret[0][1]
        res[ret[0][0]]["timestamp"] = ret[0][2]
        res[ret[0][0]]["user"] = ret[0][3]

    return res


def searchContractByKey(idContract):
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
    cursor = conn.cursor()
    req0 = "SELECT id  FROM \"closingContract\" WHERE key LIKE \"{0}\" ".format(idContract)
    cursor.execute(req0)
    ret = cursor.fetchall()

    if len(ret) > 0:
        return True
    else:
        ts = int(dt.datetime.now().timestamp())
        req1 = "INSERT INTO \"closingContract\" (key, timestamp, close)  VALUES (\"{0}\", {1}, 0)".format(idContract, ts)
        print(req1)
        cursor.execute(req1)
        conn.commit()
        return False
