Introduction
------------

Modulegraph2 is a library for creating and introspecting
the dependency graph between Python modules. The graph is
created using static analisys from source and byte code.

The dependency graph contains information about packages,
modules, extensions and their dependencies. The dependencies
are annotated with relevant information about the import
statement.

Modules that from a distribution installed using pip also have
a link to information about that distribution.

Historic
........

Modulegraph2 is a complete rewrite of `modulegraph <https://pypi.org/project/modulegraph/>`_,
using lessons learned in that project but with a complete new
Python 3 code base and full test coverage.

|pypi-version| |test-badge| |lint-badge| |docs-badge|

.. |pypi-version| image:: https://img.shields.io/pypi/v/modulegraph2.svg
   :target: https://pypi.org/project/modulegraph2

.. |test-badge| image:: https://github.com/ronaldoussoren/modulegraph2/actions/workflows/test.yml/badge.svg
   :target: https://github.com/ronaldoussoren/modulegraph2/actions/workflows/test.yml

.. |lint-badge| image:: https://github.com/ronaldoussoren/modulegraph2/actions/workflows/lint.yml/badge.svg
   :target: https://github.com/ronaldoussoren/modulegraph2/actions/workflows/lint.yml

.. |docs-badge| image:: https://img.shields.io/readthedocs/modulegraph2/latest.svg
   :target: https://modulegraph2.readthedocs.io
