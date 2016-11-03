from collections import deque

def bfs(graph, source):
    color = {}
    d = {}
    p = {}
    for node in graph:
        color[node] = 0
        d[node] = float('Inf')
        p[node] = None
    color[source] = 1
    d[source] = 0
    p[source] = None

    actives = deque()
    actives.append(source)
    while len(actives):
        u = actives.popleft()
        for v in graph[u]:
            if color[v] == 0:
                color[v] = 1
                d[v] = d[u] + 1
                p[v] = u
                actives.append(v)
        color[u] = 2
    return d, p

def print_path(graph, source, v, p):
    if v == source:
        print source
    elif p[v] == None:
        print "No Path"
    else:
        print_path(graph, source, p[v], p)
        print v

def test():
    graph = {
        'v' : {'r'},
        'r' : {'v', 's'},
        's' : {'r', 'w'},
        'w' : {'s', 'x', 't'},
        'x' : {'w', 't', 'u', 'y'},
        't' : {'w', 'x', 'u'},
        'u' : {'t', 'x', 'y'},
        'y' : {'x', 'u'}
    }
    d, p = bfs(graph, 'v')
    print d, p
    print_path(graph, 'v', 'u', p)

if __name__ == '__main__': test()
