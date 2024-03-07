# -*- coding: utf-8 -*-
import unittest
from zope.component import getUtility
from redturtle.unitaterritoriali.interfaces import IUnitaTerritorialiUtility
from redturtle.unitaterritoriali.testing import (
    REDTURTLE_UNITATERRITORIALI_FUNCTIONAL_TESTING,
)


class ModelloPraticaIntegrationTest(unittest.TestCase):
    layer = REDTURTLE_UNITATERRITORIALI_FUNCTIONAL_TESTING

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
