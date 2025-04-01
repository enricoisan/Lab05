# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso

class DAO():
    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * FROM corso c"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res


