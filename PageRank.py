D = 0.15
def PR_algo(PR, G, node):
    s = 0
    for (u, v) in G.in_edges(node):
        outEdges_count = len(G.out_edges(u))
        s += PR[u]/outEdges_count
    return s
def init(G, n):
    PR = {}
    for node in G.nodes():
        PR[node] = 1/n
    return PR
def pageRank_algo(G):
    # print(G.nodes())
    n = len(G.nodes())
    PR = init(G, n)#數據初始化
    # print(PR)
    new_PR = {}
    count = {}
    for node in G.nodes():
        new_PR[node] = D/n + (1-D)*PR_algo(PR, G, node)#PR公式
        count[new_PR[node]] = count.get(new_PR[node],0)+1#記錄數量（報告用
    print(new_PR)
    print(sorted(count.items(), key=lambda x:x[1]))