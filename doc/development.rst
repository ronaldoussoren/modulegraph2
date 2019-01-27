Development
===========

Tox
---

All testing is automated using tox.

Coding style
------------

This package uses PEP8 to guide the coding style, and in particular
uses the "black" code formatter to format all code.


Type checking
-------------

The public interfaces contain type annotations for mypy
and all production code must be without warnings from mypy. The testsuite
is not verified using mypy.


Testing
-------

The production code (package "modulegraph2") should have full
test coverage. Take care to verify that new code is actually tested
and not just accidently covered.

CI
--

Information about the CI setup (macOS, Windows, Linux; Py3.6, 3.7 and 3.8)
