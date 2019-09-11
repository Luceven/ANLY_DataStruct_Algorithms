import random
import itertools
import math
import datetime
from math import exp
class Edge:
    
    def __init__(self, node1, node2):
        if len(node1) == 1:
            self.node1 = node1
            self.node2 = node2
            self.weight = random.uniform(0,1)
        else:
            self.node1 = node1
            self.node2 = node2
            self.weight = round(sum([(node1[i]-node2[i])**2 for i in range(len(node1))])**0.5,4)
        
    def output(self):
        return[self.node1, self.node2, self.weight]

class Graph:
   
    def __init__(self, n, dim):
        self.V = {key:[round(random.uniform(0, 1), 4) for j in range(dim)] for key in range(n)}
        self.E = [[x[0],x[1],Edge(self.V[x[0]],self.V[x[1]]).output()[2]] 
                  for x in itertools.combinations(range(n), 2)]
        if n > 1000:
            self.E = [item for item in self.E if item[2]<0.5*exp(-n/70400)]
    
    def matrix(self):
        A = {key:[] for key in self.V.keys()}
        for edge in self.E:
            A[edge[0]].append(edge[1:3])
            A[edge[1]].append(edge[1:3])
        return A

def Prims(Graph):
    A = g.matrix()
    dist = {key:math.inf for key in Graph.V.keys()} 
    prev = {key:None for key in Graph.V.keys()}
    mst_node = []
    mst_edge = []
    H = {0:dist[0]}
    mst_weight = []
    weight = 0
    while len(H)!= 0:
        vv = list(min(H.items(), key=lambda x: x[1]))
        v = vv[0]
        if vv[1] != math.inf:
            weight += vv[1]
            mst_weight.append(vv[1])
        del H[v]
        mst_node.append(v)
        mst_edge.append([v,prev[v]])
        neighbors = A[v]
        for w in neighbors:
            if w[0] not in mst_node:
                if dist[w[0]] > w[1]:
                    dist[w[0]] = w[1]
                    prev[w[0]] = v
                    H[w[0]] = dist[w[0]]
    return(mst_weight)



g = Graph(128,2)
print(sum(Prims(g)))



