import networkx as nx
from Hit import hit_algo
from PageRank import pageRank_algo
from SimRank import SimRank_algo
def readFile(fileName): #讀檔
    with open(fileName) as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content] 
    return content
    
def get_node_edge(content, isBiDirected):#切成networkx可以用的格式
    g = {}
    for node in content:
        key = ''
        value = ''
        if ',' in node:
            line = node.split(',')
            key = line[0]
            value = line[1]
        else:
            line = node.split()
            key = line[1]
            value = line[2]
        if key not in g:
            g[key]=[]
        if not value in g[key]:
            g[key].append(value)
            if isBiDirected:
                if value not in g.keys():
                    g[value]=[]
                g[value].append(key)
                
    return g
if __name__ == "__main__":
    e = {"1":{"3","5"}, 
    "2":{"3", "5"},
    "3":"4",
    "4":"1"
    }
    content = readFile("hw3dataset/data.ntrans_1.ascii.tlen_5.nitems_1.npats_2")
    e = get_node_edge(content, False)
    print(e)
    G = nx.DiGraph(e)
    # hit_algo(G)
    pageRank_algo(G)
    # SimRank_algo(G,3)