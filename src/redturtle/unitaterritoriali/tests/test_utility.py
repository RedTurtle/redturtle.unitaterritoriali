# -*- coding: utf-8 -*-
from redturtle.unitaterritoriali.interfaces import IUnitaTerritorialiUtility
from redturtle.unitaterritoriali.testing import FUNCTIONAL_TESTING
from redturtle.unitaterritoriali.utility import load_data_from_csv
from zope.component import getUtility

import unittest


class ModelloPraticaIntegrationTest(unittest.TestCase):
    layer = FUNCTIONAL_TESTING

    def test_utility(self):
        utility = getUtility(IUnitaTerritorialiUtility)
        self.assertTrue(utility)

        codice_catalstale = "D458"
        codice_istat = "39010"
        res = utility.codice_catastale_to_comune(codice_catalstale)
        self.assertIn("denominazione", res)
        self.assertIn("codice_istat", res)

        res = utility.codice_istat_to_comune(codice_istat)
        self.assertIn("denominazione", res)
        self.assertIn("codice_catastale", res)

    def test_sardegna_2026(self):
        comuni = load_data_from_csv()

        prov_key = "Denominazione dell'Unità territoriale sovracomunale \n(valida a fini statistici)"
        self.assertEqual(
            len([c for c in comuni if c[prov_key] == "Cagliari"]),
            70,
        )

        self.assertEqual(
            len(
                [c for c in comuni if c[prov_key] == "Medio Campidano"]
            ),  # ex Sud Sardegna
            28,
        )
