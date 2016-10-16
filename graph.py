#### ADJACENCY LISTS (actually sets)

class ALDirectedGraph(object):
    def __init__(self):
        self.Adj = {}
    def itervertices():
        """Iterate all vertices in the graph in arbitrary order."""
        return self.Adj.iterkeys()
    def add_vertex(self, u):
        """Add a vertex to the graph.
        
        A vertex can be any hashable object, e.g., an integer or a tuple.

        Time: O(1).
        """
        if u in self.Adj: raise 'vertex %r already in graph' % u
        self.Adj[u] = set()
    def remove_vertex(u):
        """Remove specified vertex from the graph.

        This operation removes all outgoing edges from the vertex,
        but does not remove incoming edges to the vertex.
        (In this data structure, there is no fast way to find them.)
        You should remove such edges before removing the vertex.

        Time: O(1).
        """
        del self.Adj[u]
    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v.

        Adds the vertices to the graph if they are not already in it.

        Time: O(1).
        """
        if u not in self.Adj:
            self.add_vertex(u)
        self.Adj[u].add(v)
        if v not in self.Adj:
            self.add_vertex(v)
    def remove_edge(self, u, v):
        """Remove the edge from u to v.

        Time: O(1).
        """
        self.Adj[u].remove(v)
    def neighbors(self, u):
        """Return the set of neighbors of (vertices adjacent to) u.
        
        Time: O(1).
        """
        return self.Adj[u]

class UndirectedGraphMixin(object):
    def remove_vertex(self, u):
        """Remove specified vertex and all incident edges from the graph.
        
        Time: O(1).
        """
        for v in self.neighbors(u):
            self.remove_edge(v, u)
        super(UndirectedGraphMixin, self).remove_vertex(u)
    def add_edge(self, u, v):
        """Add an undirected edge between two vertices.

        Adds the vertices to the graph if they are not already in it.

        Time: O(1).
        """
        super(UndirectedGraphMixin, self).add_edge(u, v)
        super(UndirectedGraphMixin, self).add_edge(v, u)
    def remove_edge(self, u, v):
        """Remove the undirected edge between two vertices.
        
        Time: O(1).
        """
        super(UndirectedGraphMixin, self).remove_edge(u, v)
        super(UndirectedGraphMixin, self).remove_edge(v, u)

class ALUndirectedGraph(UndirectedGraphMixin, ALDirectedGraph):
    pass

#### OBJECT-ORIENTED ADJACENCY LISTS (actually sets)

class OOALVertex(object):
    def __init__(self):
        self.neighbors = set()

class OOALDirectedGraph(object):
    Vertex = OOALVertex
    def __init__(self):
        self.vertices = set()
    def itervertices():
        """Iterate all vertices in the graph in arbitrary order."""
        return iter(self.vertices)
    def add_vertex(self, u):
        """Add a vertex to the graph.
        
        The vertex should be an OOALVertex object.

        Time: O(1).
        """
        if u in self.vertices: raise 'vertex %r already in graph' % u
        self.vertices.add(u)
    def remove_vertex(u):
        """Remove specified vertex from the graph.

        This operation removes all outgoing edges from the vertex,
        but does not remove incoming edges to the vertex.
        (In this data structure, there is no fast way to find them.)
        You should remove such edges before removing the vertex.

        Time: O(1).
        """
        self.vertices.remove(u)
    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v.

        Adds the vertices to the graph if they are not already in it.

        Time: O(1).
        """
        if u not in self.vertices:
            self.add_vertex(u)
        u.neighbors.add(v)
        if v not in self.vertices:
            self.add_vertex(v)
    def remove_edge(self, u, v):
        """Remove the edge from u to v.

        Time: O(1).
        """
        u.neighbors.remove(v)
    def neighbors(self, u):
        """Return the set of neighbors of (vertices adjacent to) u.
        
        Time: O(1).
        """
        return u.neighbors

class OOALUndirectedGraph(UndirectedGraphMixin, OOALDirectedGraph):
    pass

#### OBJECT-ORIENTED INCIDENCE LISTS (with edge objects)

class OOILVertex(object):
    def __init__(self):
        self.edges = set()

class OOILEdge(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def other_end(self, a_or_b):
        if self.a is a_or_b:
            return self.b
        else:
            return self.a
    def as_tuple(self):
        return (self.a, self.b)
    def __hash__(self):
        return hash(self.as_tuple())
    def __cmp__(self, other):
        if isinstance(other, OOILEdge):
            return cmp(self.as_tuple(), other.as_tuple())
        else:
            return -1

class OOILDirectedGraph(object):
    Vertex = OOILVertex
    Edge = OOILEdge
    def __init__(self):
        self.vertices = set()
    def itervertices():
        """Iterate all vertices in the graph in arbitrary order."""
        return iter(self.vertices)
    def add_vertex(self, u):
        """Add a vertex to the graph.
        
        The vertex should be an OOILVertex object.

        Time: O(1).
        """
        if u in self.vertices: raise 'vertex %r already in graph' % u
        self.vertices.add(u)
    def remove_vertex(u):
        """Remove specified vertex from the graph.

        This operation removes all outgoing edges from the vertex,
        but does not remove incoming edges to the vertex.
        (In this data structure, there is no fast way to find them.)
        You should remove such edges before removing the vertex.

        Time: O(1).
        """
        self.vertices.remove(u)
    def add_edge(self, u, v = None):
        """Add the specified edge, or the edge from vertex u to vertex v.

        This function can be given a single OOILEdge object, or two
        OOILVertex objects (in which case it forms the edge object).
        Also adds the vertices to the graph if they are not already in it.

        Time: O(1).
        """
        if v is None:
            edge = u
            u, v = edge.a, edge.b
        else:
            edge = self.Edge(u, v)
        if u not in self.vertices:
            self.add_vertex(u)
        u.edges.add(edge)
        if v not in self.vertices:
            self.add_vertex(v)
    def remove_edge(self, u, v = None):
        """Remove a specified edge, or the edge from vertex u to vertex v.

        Time: O(1).
        """
        if v is None:
            edge = u
        else:
            edge = self.Edge(u, v)
        u.edges.remove(edge)
    def neighbors(self, u):
        """Iterate neighbors of (vertices adjacent to) u."""
        return (edge.other_end(u) for edge in u.edges)
    def incident_edges(self, u):
        """Return the set of outgoing edges from u.
        
        Time: O(1)
        """
        return u.edges

## Undirected version needs a slightly different Edge object:

class OOILUndirectedEdge(OOILEdge):
    def as_tuple(self):
        if self.a <= self.b:
            return (self.a, self.b)
        else:
            return (self.b, self.a)

class OOILUndirectedGraph(UndirectedGraphMixin, OOILDirectedGraph):
    Edge = OOILUndirectedEdge
    def incident_edges(self, u):
        """Return the set of edges incident to u.
        
        Time: O(1)
        """
        return u.edges
