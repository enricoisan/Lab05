# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


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

    @staticmethod
    def getIscrittiCorso(corso):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT s.matricola, s.cognome, s.nome, s.CDS
                    FROM iscrizione i
                    JOIN studente s ON i.matricola = s.matricola
                    WHERE i.codins = %s"""

        cursor.execute(query, (corso,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudente(matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * FROM studente s 
                    WHERE s.matricola = %s"""

        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiStudente(matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT c.codins, c.crediti, c.nome, c.pd
                    FROM iscrizione i
                    JOIN corso c ON c.codins = i.codins
                    WHERE i.matricola = %s"""

        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res
