modulegraph2.ObjectGraph - A basic directed graph with roots
============================================================

.. module:: modulegraph2
   :synopsis: Dependency graph for Python code

.. class:: ObjectGraph

   A simple directed graph, without duplicate edges between nodes.

   Nodes in the graph can be arbitrary objects with a string attribute named "identifier".

   Edges between nodes can have data associated with them.

   The graph has explicit root nodes, primarily used by the graph iteration method.

   .. function:: add_node(node)

      Adds node to the graph.

      :arg node: The node to add to the graph
      :raises KeyError: The node identifier is not unique in the graph

   .. function:: add_root(node)

      Registers *node* as a root of the graph.

      :arg node: Node or node identifier to register as root
      :raises KeyError: When the node is not part of the graph

   .. function:: add_edge(source, destination, edge_attributes=None, merge_attributes=None)

      Adds a new edge from *source* to *destination* to the graph.

      :arg source: Node or node identifier
      :arg destination: Node or node identifier
      :arg edge_attributes: Arbitrary data for the edge
      :arg merge_attributes: Function that is called when there is already an edge between *source* and *destination*.
      :raises KeyError: When *source* or *destination* cannot be found
      :raises ValueError: When there is already an edge between *source* and *destionation* and *merge_attributes* was not specified

   .. function:: __contains__(node)

      Returns true if *node* is part of the graph.

      :arg node: Node or node identifier to look for.

   .. function:: roots()

      Yields all nodes that are registered as graph root.

   .. function:: nodes()

      Yields all nodes for the graph.

   .. function:: edge_data(source, destination)

      Returns the edge data for the edge from *source* to *destination*.

      :raises KeyError: When *source* or *destionation* is not part of the graph
      :raises KeyError: When there is no edge from *source* to *destionation*

   .. function:: incoming(destination)

      Yields all tuples (edge_data, source) for all edges that have *destionation* as their destination.

      :arg destination: Node or node identifier

   .. function:: outgoing(source)

      Yields all tuples (edge_data, destination) for all edges that have *source* as their source.

      :arg source: Node or node identifier

   .. function:: iter_graph(\*, node=None)

      Yield all nodes that can be reached from *node*. When *node* is not specified this will yield
      all nodes that can be reached from any of the root nodes.

      :arg node: The node to start iterating from
