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

There is `documentation at readthedocs <https://modulegraph2.readthedocs.io/>`_

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

CI Status
.........

.. image:: https://github.com/ronaldoussoren/modulegraph2/workflows/Lint/badge.svg
.. image:: https://github.com/ronaldoussoren/modulegraph2/workflows/Test/badge.svg

Historic
........

Modulegraph2 is a complete rewrite of `modulegraph <https://pypi.org/project/modulegraph/>`_,
using lessons learned in that project but with a complete new
Python 3 code base and full test coverage.
