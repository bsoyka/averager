Averager
=====

**Averager** is a simple Python library to calculate averages of values.

>>> import averager
>>> averager.average(1, 2, 3)
2
>>> averager.weighted_average((1, 2), (2, 3))
1.6
>>> averager.median(5, 1, 2)
2
>>> averager.mode(1, 2, 4, 3, 3)
3

|Total Downloads| |Supported Versions| |Testing Status| |Coverage| |GitHub last commit| |GitHub Repo stars|

.. |Total Downloads| image:: https://img.shields.io/pepy/dt/averager
   :target: https://pypi.org/project/averager/
   :alt: Total Downloads

.. |Supported Versions| image:: https://img.shields.io/pypi/pyversions/averager.svg
   :target: https://pypi.org/project/averager/
   :alt: Supported Versions

.. |Testing Status| image:: https://img.shields.io/github/actions/workflow/status/bsoyka/averager/test.yml?branch=main&label=tests
   :target: https://github.com/bsoyka/averager/actions/workflows/test.yml
   :alt: Testing Status

.. |Coverage| image:: https://img.shields.io/codecov/c/github/bsoyka/averager
   :target: https://codecov.io/github/bsoyka/averager
   :alt: Coverage

.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/bsoyka/averager
   :target: https://github.com/bsoyka/averager
   :alt: GitHub last commit

.. |GitHub Repo stars| image:: https://img.shields.io/github/stars/bsoyka/averager
   :target: https://github.com/bsoyka/averager
   :alt: GitHub Repo stars

Installation
------------

Averager is `available on PyPI <https://pypi.org/project/averager/>`_.
Install it with your preferred package manager:

.. code-block:: shell

    $ uv add averager
    $ pip install averager

Averager officially supports Python 3.9+.

API reference
-------------

.. automodule:: averager
    :members:
