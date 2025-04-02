from database import corso_DAO
from database.corso_DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getIscrittiCorso(self, corso):
        return DAO.getIscrittiCorso(corso)

    def getStudente(self, matricola):
        return DAO.getStudente(matricola)

    def getCorsiStudente(self, matricola):
        return DAO.getCorsiStudente(matricola)