Modulegraph2 command-line interface
===================================

Synopsis
--------

**python** **-mmodulegraph2** [*option*] **name** ...

Description
-----------

Build a modulegraph for one or more scripts, modules or distributions and
output the graph as a HTML or Graphviz file.

Options
-------

.. program:: **python** **-mmodulegraph2**

.. option:: -h, --help

   Display the command-line interface and exit.

.. option:: -m, --module

   The positional arguments are module names (default behaviour).

.. option:: -s, --script

   The positional arguments are scripts.

.. option:: -d, --distribution

   The positional arguments are distributions.

.. option:: -f FORMAT, --format FORMAT

   Output the graph in the specified format. Two formats supported:

   **html**
     Output a HTML report on the dependency graph

   **dot**
     Output a Graphviz file with the depedency graph

.. option::  -x NAME, --exclude NAME

   Add *NAME* to the list of excluded modules.

.. option::   -p PATH, --path PATH

   Add PATH to the module search path.

.. option:: -o FILE, --output FILE

   Write output to path (defaults to stdout)

.. option:: name...

   The names of modules, scripts or distributions at the root of
   the depedency graph.
