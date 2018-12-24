C = 0.6
from collections import defaultdict
max_deep = 0
dic = defaultdict(dict)
def NorMulNor(G, a, b):
    return len(G.in_edges(a))*len(G.in_edges(b))
def S(G, a, b, deep):
    flag = 0
    deep += 1
    if a == b:
        flag = 1
    elif len(G.in_edges(a)) == 0 or len(G.in_edges(b)) == 0:
        flag = 0
    else:
        sigma = 0
        for (u, v) in G.in_edges(a):
            for (u2, v2) in G.in_edges(b):
                if deep <= max_deep:
                    if(not dic[u].get(u2,False)):
                        dic[u][u2] = S(G, u, u2, deep)
                    sigma += dic[u][u2]
        Mul = NorMulNor(G, a, b)#取得兩個圖的射入數量並且相乘
        if Mul != 0:
            flag = C/Mul*sigma
    return flag
def SimRank_algo(G, maxdeep):
    global max_deep
    max_deep = maxdeep
    count={}
    for node in G.nodes():
        for node2 in G.nodes():
            # if node != node2:
            deep = 0
            Sorce = S(G, node, node2, deep)#SimRank裡面的迴圈
            # SimRank_list[node][node2] = "{:.5f}".format(Sorce)
            count[Sorce]=count.get(Sorce, 0)+1#記錄數量（報告用
            if Sorce != 0:
                print(node, node2, "{:.5f}".format(Sorce))
                
    print(count)
    