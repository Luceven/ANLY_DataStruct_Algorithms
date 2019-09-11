import random
import itertools
import math
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
    
    def neighbor(self, node):
        neighbors = {}
        for i in range(len(self.E)):
            if self.E[i][0] == node:
                neighbors[self.E[i][1]] = self.E[i][2]
            elif self.E[i][1] == node:
                neighbors[self.E[i][0]] = self.E[i][2]
        return neighbors

def Prims(Graph):
    dist = {key:math.inf for key in Graph.V.keys()} 
    prev = {key:None for key in Graph.V.keys()}
    mst_node = []
    mst_edge = []
    H = {0:dist[0]}
    weight = 0
    while len(H)!= 0:
        vv = list(min(H.items(), key=lambda x: x[1]))
        v = vv[0]
        if vv[1] != math.inf:
            weight += vv[1]
        del H[v]
        mst_node.append(v)
        mst_edge.append([v,prev[v]])
        neighbors = g.neighbor(v)
        for w in neighbors.keys():
            if w not in mst_node:
                if dist[w] > neighbors[w]:
                    dist[w] = neighbors[w]
                    prev[w] = v
                    H[w] = dist[w]
    print("Edges in MST:",mst_edge)
    print("Average weight of MST:", weight/(len(mst_node)-1))

    
# test
# input graph with 100 nodes in 10 dimension 
g = Graph(100,10)
Prims(g)
