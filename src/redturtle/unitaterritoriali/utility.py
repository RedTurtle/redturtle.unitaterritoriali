from importlib import resources
from redturtle.unitaterritoriali.interfaces import IUnitaTerritorialiUtility
from zope.interface import implementer

import csv
import logging


logger = logging.getLogger(__name__)


file_codici = "codici_statistici_01_01_2026.csv"
with resources.open_text(__package__, file_codici, encoding="utf-8") as fd:
    DATA = list(csv.DictReader(fd, delimiter=";"))

# province
PROV = sorted(
    [
        {"value": k, "title": v}
        for (k, v) in {
            row["Sigla automobilistica"]: row[
                "Denominazione dell'Unità territoriale sovracomunale \n(valida a fini statistici)"
            ]
            for row in DATA
        }.items()
    ],
    key=lambda x: x["title"],
)

# comuni
COMUNI = sorted(
    [
        {"value": k, "title": v}
        for (k, v) in {
            row["Codice Comune formato numerico"]: row["Denominazione in italiano"]
            for row in DATA
        }.items()
    ],
    key=lambda x: x["title"],
)

ISTAT = {
    comune["Codice Comune formato numerico"]: {
        "codice_catastale": comune["Codice Catastale del Comune"],
        "denominazione": comune["Denominazione in italiano"],
    }
    for comune in DATA
}

CATASTALE = {
    comune["Codice Catastale del Comune"]: {
        "codice_istat": comune["Codice Comune formato numerico"],
        "denominazione": comune["Denominazione in italiano"],
    }
    for comune in DATA
}


# BBB
def load_data_from_csv():
    return DATA


@implementer(IUnitaTerritorialiUtility)
class UnitaTerritoriali(object):
    def __init__(self):
        self.codice_istat_to_data = ISTAT
        self.codice_catastale_to_data = CATASTALE

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
