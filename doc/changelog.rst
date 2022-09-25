Release history
===============

2.2.1
-----

* Fix incompatibility with recent setuptools versions

* Fix incompatibility with Python 3.11

2.2
---

* Enhance the support for setuptools vendored packages
  to also work with pkg_resources (which uses the same
  mechanism).

* Fix graphbuilding problem when using "setuptools",
  "pkg_resources" or "six".

* Fix test failures with recent python versions, failures
  were due to imperfect test hygiene.

* Add a *code* attribute to :class:`modulegraph2.Script`
  and :class:`modulegraph2.Module`, containing the compiled
  bytecode for the module (or *None*)

2.1
-----

* #11: ``ModuleGraph.add_script`` did not work reliably

* Add support for the way setuptools locates vendored
  packages (``setuptools.extern.VendorImporter``)

2.0
---

* No functional changes

* Migrated to GitHub

2.0a2
-----

Fixed a number of issues:

* Test suite now passes on Windows

* Test suite now passes on Linux

* Test suite now passes with Python 3.6

* Implemented automated tested on Windows and Linux
  using AppVeyor. MacOS is manually tested for
  now as that's my main development platform.

2.0a1
-----

Initial pre-release. This version should be
functionally complete, but hasn't been used
by other code yet.
