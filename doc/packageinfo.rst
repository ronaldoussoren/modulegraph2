modulegraph2.PyPIPackage - Information about installed packages
===============================================================

.. module:: modulegraph2
   :synopsis: Dependency graph for Python code

.. class:: PyPIPackage

   A dataclass representing relevant information about installed Python
   packages (wheels).

   .. data:: identifier

      A unique identifier for use in :class:`ObjectGraph`. Is never a
      valid python module name.

   .. data:: name

      Name of the python distribution.

   .. data:: version

      Version of the python distribution as a string

   .. data:: files

      Set of absolute paths of all files installed for this distribution,
      this includes the wheel metadata

   .. data:: import_names:

      Set of module and package names included in this package.


   .. function:: contains_file(filename)

      Returns True if this distribution contains *filename*, otherwise
      returns False.
