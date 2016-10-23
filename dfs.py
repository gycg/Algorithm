from graph import *

class DFSResults:
    def __init__(self):
        self.parent = dict()
        self.time = dict()
        self.vertices = list()
        self.t = -1

def dfs(g):
    results = DFSResults()

    for vertex in g.itervertices():
        if vertex not in results.parent:
            dfs_visit(g, vertex, results)

    return results

def dfs_visit(g, v, results, parent = None):
    results.vertices.append(v)
    results.parent[v] = parent
    
    for n in g.neighbors(v):
        if n not in results.parent:
            results.parent[n] = v
            dfs_visit(g, n, results, v)

    results.t += 1
    results.time[v] = results.t

    #results.t += 1
    #results.time[v] = results.t
    
def topological_sort(g):
    r = dfs(g)
    top = [None for i in r.vertices]
    for vertex in r.time:
        top[r.time[vertex]] = vertex
    return top 
            
if __name__ == '__main__':
    g = ALDirectedGraph()
    g.add_edge('u', 'x')
    g.add_edge('u', 'v')
    g.add_edge('v', 'y')
    
    g.add_edge('w', 'y')
    g.add_edge('w', 'z')
    
    g.add_edge('x', 'v')
    g.add_edge('y', 'x')
    g.add_edge('z', 'z')

    r = dfs(g)
    print 'vertices: ', r.vertices
    print 'time: ', r.time
    print 'topological sort: ', topological_sort(g)
