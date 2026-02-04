# -*- coding: utf-8 -*-
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import redturtle.unitaterritoriali


class RedturtleUnitaterritorialiLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=redturtle.unitaterritoriali)

    def setUpPloneSite(self, portal):
        return


REDTURTLE_UNITATERRITORIALI_FIXTURE = RedturtleUnitaterritorialiLayer()


REDTURTLE_UNITATERRITORIALI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REDTURTLE_UNITATERRITORIALI_FIXTURE,),
    name="RedturtleUnitaterritorialiLayer:IntegrationTesting",
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REDTURTLE_UNITATERRITORIALI_FIXTURE,),
    name="RedturtleUnitaterritorialiLayer:FunctionalTesting",
)
