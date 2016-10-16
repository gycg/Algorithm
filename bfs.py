from graph import *
from collections import deque
 
class BFSResults:
    def __init__(self):
        self.level = dict()
        self.parent = dict()

def bfs(g, s):
    r = BFSResults()
    
    actives = deque()   
    actives.append(s)
    r.parent[s] = None
    r.level[s] = 0
    
    while len(actives):
        v = actives.popleft()    
        for n in g.neighbors(v):
            if n not in r.parent:
                r.parent[n] = v
                r.level[n] = r.level[v] + 1
                actives.append(n)
    
    return r

def print_path(g, s, v):
    if v == s:
        print "path:", s,
    elif r.parent[v] == None:
        print "No path"
    else:
        print_path(g, s, r.parent[v])
        print "-> "+v,
   
if __name__ == '__main__':
    g = ALDirectedGraph()
    
    g.add_edge('r', 's')
    g.add_edge('r', 'v')
    g.add_edge('s', 'r')
    g.add_edge('s', 'w')
    g.add_edge('t', 'w')
    g.add_edge('t', 'x')
    g.add_edge('t', 'u')
    g.add_edge('u', 't')
    g.add_edge('u', 'x')
    g.add_edge('u', 'y')
    g.add_edge('v', 'r')
    g.add_edge('w', 's')
    g.add_edge('w', 't')
    g.add_edge('w', 'x')
    g.add_edge('x', 'w')
    g.add_edge('x', 't')
    g.add_edge('x', 'u')
    g.add_edge('x', 'y')
    g.add_edge('y', 'x')
    g.add_edge('y', 'u')
    
    r = bfs(g, 'v')
    print 'level:', r.level
    print 'parent: ', r.parent
    print_path(g, 'v', 'u')
