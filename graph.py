"""
Directed Graph

This graph class is a container that holds a set
of vertices and a list of directed edges.
Edges are modelled as tuples (u,v) of vertices.
"""

class Graph:
  def __init__(self, Vertices = set(), Edges = list()):
    
    # g = Graph({1,2,3}, [(1,2), (2,3)])

    self.alist = {}

    for v in Vertices:
      self.add_vertex(v)
    for e in Edges:
      self.add_edge(e)

  def get_vertices(self):
    
    # Returns the set of vertices in the graph.

    return set(self.alist.keys())

  def get_edges(self):

    # Returns a list of all edges in the graph.

    edges = []
    for v,l in self.alist.items():
      edges += l
    return edges

  def add_vertex(self, v):

    """
    Add a vertex v to the graph.
    If v exists in the graph, do nothing.
    """

    if v not in self.alist:
      self.alist[v] = []

  def add_edge(self, e):

    """
    Add edge e to the graph.
    Raise an exception if the endpoints of
    e are not in the graph.
    """

    if not self.is_vertex(e[0]) or not self.is_vertex(e[1]):
      raise ValueError("An endpoint is not in graph")
    self.alist[e[0]].append(e[1])

  def is_vertex(self, v):
   
    # Check if vertex v is in the graph.

    return v in self.alist

  def is_edge(self, e):

    # Check if edge e is in the graph.

    if e[0] not in self.alist:
      return False

    return e[1] in self.alist[e[0]]

  def neighbours(self, v):

    # Return a list of neighbours of v.

    if not self.is_vertex(v):
      raise ValueError("Vertex not in graph")

    return self.alist[v]





def is_walk(g, walk):

  """
  Given a graph 'g' and a list 'walk', return true
  if 'walk' is a walk in g.
  """

  if not walk: # should have at least one vertex
    return False

  if len(walk) == 1:
    return g.is_vertex(walk[0])

  for i in range(len(walk)-1):

    if not g.is_edge((walk[i], walk[i+1])):
      return False

  return True


def is_path(g, path):

  """
  Given a graph 'g' and a list 'path',
  return true if 'path' is a path in g.
  """

  if len(set(path)) < len(path):
    return False

  return is_walk(g, path)

if __name__ == "__main__":
  import doctest
  doctest.testmod()
