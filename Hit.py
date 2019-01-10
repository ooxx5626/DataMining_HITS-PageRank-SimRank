# import networkx as nx
def get_node_edge(content):
    g = {}
    for node in content:
        line = node.split(',')
        if(line[0] not in g):
            g[line[0]]=[]
        g[line[0]].append(line[1])
    return g
def init(G):
    a_page = {}
    h_page = {}
    for v in G.nodes():
        a_page[v] = 1
        h_page[v] = 1
    return a_page, h_page

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
def HubsAuthorities(a_page, h_page, G):
    new_a_page = {}
    new_h_page = {}
    for v in a_page:
        for (u, v) in G.in_edges(v):
            new_a_page[u] = new_a_page.get(u, 0.0) + h_page[v]
        for (u, v) in G.out_edges(v):
            new_h_page[u] = new_h_page.get(u, 0.0) + a_page[v]
    return new_a_page, new_h_page
def Absolute (x):
    flag = {}
    # min_x = min(x.values())
    s = 0
    for i in list(x.values()):
        s += i**2
    return s**0.5
    # return sum(x.values())
def t_Nor(x, y, G):
    new_a_page = {}
    new_h_page = {}
    # print("Absolute (x)", Absolute (x))
    for i, v in x.items():
        new_a_page[i] = x[i]/Absolute (x)
    for i, v in y.items():
        new_h_page[i] = y[i]/Absolute (y)
    for v in G.nodes():
        new_a_page.setdefault(v, 0)
        new_h_page.setdefault(v, 0)
    # print("new_a_page", new_a_page)
    return new_a_page, new_h_page
def dec(x, y):
    z ={}
    for k, v in y.items():
        z[k] = abs(x.get(k) - v)
    return z
def plus_values(x, y):
    for k, v in y.items():
        x[k] += v
    s = sum(x.values()) + sum(y.values())
    return s
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges
def hit_algo(G):
    # e = get_node_edge(content)

    # a = find_path(e, 'A', 'D')
    # graph = Graph(e)
    # print(graph)
    # path = graph.find_all_paths("C", "B")
    # print(path)

    # G = nx.DiGraph(e)
    # print(G.nodes())
    # print(G.edges())
    # print(G.out_edges('2'))
    # print(G.in_edges('2'))
    # print(G.in_edges(nbunch ='2'))

    a_page, h_page = init(G)#初始化
    t=1
    while True:
        new_a_page, new_h_page = HubsAuthorities(a_page, h_page, G)#計算新的hub和Authorities
        print("new_a_page", new_a_page)
        print("new_h_page", new_h_page)
        new_a_page, new_h_page = t_Nor(new_a_page, new_h_page, G)#正規化Hub和Authorities
        ad = dec(new_a_page,a_page)#相減
        hd = dec(new_h_page,h_page)
        Nor_ta = Absolute(ad)#取絕對值
        Nor_th = Absolute(hd)
        # print("a_page", a_page)
        # print("h_page", h_page)

        # print("ad", ad)
        # print("hd", hd)
        # print("Nor_ta", Nor_ta)
        # print("Nor_th", Nor_th)

        error = Nor_ta + Nor_th
        a_page, h_page = new_a_page, new_h_page
        t+=1
        if error<=1.5:
            break
    print("Error :", error)
    # print('success')
    print('Count :', t)
    print('authority page :', a_page)
    print('hub :', h_page)
    # return a_page, h_page