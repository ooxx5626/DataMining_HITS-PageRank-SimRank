import networkx as nx
from Hit import hit_algo
from PageRank import pageRank_algo
from SimRank import SimRank_algo
def readFile(fileName): #讀檔
    with open(fileName) as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content] 
    return content
    
def get_node_edge(content):#切成networkx可以用的格式
    g = {}
    for node in content:
        line = node.split(',')
        if(line[0] not in g):
            g[line[0]]=[]
        g[line[0]].append(line[1])
    return g
if __name__ == "__main__":
    e = {"1":{"3","5"}, 
    "2":{"3", "5"},
    "3":"4",
    "4":"1"
    }
    content = readFile("hw3dataset/graph_1.txt")
    e = get_node_edge(content)
    # print(e)
    G = nx.DiGraph(e)
    hit_algo(G)
    # pageRank_algo(G)
    # SimRank_algo(G,3)