# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import redturtle.unitaterritoriali


class RedturtleUnitaterritorialiLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=redturtle.unitaterritoriali)

    def setUpPloneSite(self, portal):
        return


REDTURTLE_UNITATERRITORIALI_FIXTURE = RedturtleUnitaterritorialiLayer()


REDTURTLE_UNITATERRITORIALI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REDTURTLE_UNITATERRITORIALI_FIXTURE,),
    name="RedturtleUnitaterritorialiLayer:IntegrationTesting",
)


REDTURTLE_UNITATERRITORIALI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REDTURTLE_UNITATERRITORIALI_FIXTURE,),
    name="RedturtleUnitaterritorialiLayer:FunctionalTesting",
)


REDTURTLE_UNITATERRITORIALI_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REDTURTLE_UNITATERRITORIALI_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="RedturtleUnitaterritorialiLayer:AcceptanceTesting",
)
