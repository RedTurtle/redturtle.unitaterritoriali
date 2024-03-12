.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/redturtle.unitaterritoriali/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/redturtle.unitaterritoriali/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/redturtle.unitaterritoriali/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/redturtle.unitaterritoriali?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/redturtle.unitaterritoriali/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/redturtle.unitaterritoriali

.. image:: https://img.shields.io/pypi/v/redturtle.unitaterritoriali.svg
    :target: https://pypi.python.org/pypi/redturtle.unitaterritoriali/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/redturtle.unitaterritoriali.svg
    :target: https://pypi.python.org/pypi/redturtle.unitaterritoriali
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/redturtle.unitaterritoriali.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/redturtle.unitaterritoriali.svg
    :target: https://pypi.python.org/pypi/redturtle.unitaterritoriali/
    :alt: License


===========================
redturtle.unitaterritoriali
===========================

This addon takes data from ISTAT:

- https://www.istat.it/it/archivio/6789
- https://www.istat.it/storage/codici-unita-amministrative/Elenco-codici-statistici-e-denominazioni-delle-unita-territoriali.zip

and provide a way to make simple query

Features
--------

- from codice istat to codice catastale/denominazione
- from codice catastale to codice istat/denominazione


Examples
--------

This is an example of how to use this package::

    utility = component.getUtility(IUnitaTerritorialiUtility)
    comune = utility.codice_catastale_to_comune("D458")
    {'codice_istat': '39010', 'denominazione': 'Faenza'}

    comune = utility.codice_istat_to_comune("39010")
    {'codice_catastale': 'D458', 'denominazione': 'Faenza'}

Installation
------------

Install redturtle.unitaterritoriali by adding it to your buildout::

    [buildout]

    ...

    eggs =
        redturtle.unitaterritoriali


and then running ``bin/buildout``


Authors
-------

RedTurtle


License
-------

The project is licensed under the GPLv2.
