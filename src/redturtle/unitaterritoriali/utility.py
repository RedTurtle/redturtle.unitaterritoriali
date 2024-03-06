from redturtle.unitaterritoriali.interfaces import IUnitaTerritorialiUtility
from zope.interface import implementer
from plone.memoize import forever
import csv
import os
import logging


logger = logging.getLogger(__name__)


file_codici = "codici_statistici_22_01_2024.csv"


@forever.memoize
def load_data_from_csv():
    """
    Load data from csv in current folder
    """
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    filename = "{}/{}".format(current_file_directory, file_codici)
    fd = open(filename, "r", newline="", encoding="latin-1")
    csv_reader = csv.DictReader(fd, delimiter=";")
    return list(csv_reader)


@implementer(IUnitaTerritorialiUtility)
class UnitaTerritoriali(object):

    def __init__(self):
        self.data = self._get_data()

    def _get_data(self):
        """This utility load data when instance starting"""
        comuni = load_data_from_csv()
        self.codice_istat_to_data = {}
        self.codice_catastale_to_data = {}
        for comune in comuni:
            codice_istat = comune["Codice Comune formato numerico"]
            codice_catastale = comune["Codice Catastale del comune"]
            denominazione = comune["Denominazione in italiano"]
            self.codice_istat_to_data[codice_istat] = {
                "codice_catastale": codice_catastale,
                "denominazione": denominazione,
            }
            self.codice_catastale_to_data[codice_catastale] = {
                "codice_istat": codice_istat,
                "denominazione": denominazione,
            }

    def codice_istat_to_comune(self, codice_istat):
        # it's an int, but here we have only strings
        codice_istat = str(codice_istat)
        if codice_istat in self.codice_istat_to_data:
            return self.codice_istat_to_data[codice_istat]
        else:
            logger.warning("Il codice istat {} non esiste".format(codice_istat))
            return None

    def codice_catastale_to_comune(self, codice_catastale):
        if codice_catastale in self.codice_catastale_to_data:
            return self.codice_catastale_to_data[codice_catastale]
        else:
            logger.warning("Il codice catastale {} non esiste".format(codice_catastale))
            return None
