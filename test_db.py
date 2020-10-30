import unittest
import sys
from DB import wrapperDB as wdb
import sqlite3 as sql
import os

class ApiTest(unittest.TestCase):

    def test_updateStateClose(self):
        c = sql.connect("DB/dataBase.db")
        c.execute("INSERT INTO \"closingContract\" (key, timestamp, close, user)  VALUES (\"L789\", 1603966615, false, 13)")
        c.commit()
        wdb.updateStateClose("L789", "USERNAME")
        c.execute("SELECT close FROM \"closingContract\" WHERE key LIKE \"L789\"")
        ret = c.fetchall()

        self.assertEqual(ret[0]["code"], 1)




if __name__ == '__main__':
    wdb.initDB()

    try:
        c = sql.connect("DB/dataBase.db")
        c.execute("INSERT INTO \"closingContract\" (key, timestamp, close, user)  VALUES (\"L12345\", 1603966615, false, 13)")
        c.commit()
    except :
        pass

    unittest.main()
