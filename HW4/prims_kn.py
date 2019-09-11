import random
import itertools
import math
import datetime
from timeit import default_timer as timer
from math import exp
# Class for generate edges
class Edge:
    def __init__(self, node1, node2):
        # when dimension = 1, generate weight by selecting random number from (0,1)
        if len(node1) == 1:
            self.node1 = node1
            self.node2 = node2
            self.weight = round(random.uniform(0,1),4)
        # when dimension != 1, generate weight by calculating Euclidean distance
        else:
            self.node1 = node1
            self.node2 = node2
            self.weight = round((sum([(node1[i]-node2[i])**2 for i in range(len(node1))]))**0.5,4)
    # output nodes and weight
    def output(self):
        return[self.node1, self.node2, self.weight]

class Graph:
    def __init__(self, n, dim):
        # define graph's vertices, each has a label
        self.V = {key:[round(random.uniform(0, 1), 4) for j in range(dim)] for key in range(n)}
        # define edges, each is a list with node label and weight
        self.E = [[x[0],x[1],Edge(self.V[x[0]],self.V[x[1]]).output()[2]] 
                  for x in itertools.combinations(range(n), 2)]
        # throw away large edges
        if n > 1000:
            self.E = [item for item in self.E if item[2]<0.3*exp(-n*0.00004)]
    # adjacency dictionary for looking up edges, each with neighbors and distance(weight)
    def matrix(self):
        A = {key:[] for key in self.V.keys()}
        for edge in self.E:
            A[edge[0]].append([edge[1],edge[2]])
            A[edge[1]].append([edge[0],edge[2]])
        return A


def Prims(Graph):
    A = g.matrix()
    # distance dict
    dist = {key:math.inf for key in Graph.V.keys()} 
    # prev dict
    prev = {key:None for key in Graph.V.keys()}
    # store the nodes in MST
    mst_node = []
    # store the edges in MST
    mst_edge = []
    # "Priority Queue" in Prim's Algorithm
    H = {0:dist[0]}
    # store the weight of edges in MST
    mst_weight = []
    while len(H)!= 0:
        # process next node with smallest distance
        vv = list(min(H.items(), key=lambda x: x[1]))
        v = vv[0]
        if vv[1] != math.inf:
            mst_weight.append(vv[1])
        # end up with this node
        del H[v]
        mst_node.append(v)
        mst_edge.append([v,prev[v]])
        neighbors = A[v]
        # process with the neighbors of v, find the nearest one
        for w in neighbors:
            if w[0] not in mst_node:
                if dist[w[0]] > w[1]:
                    dist[w[0]] = w[1]
                    prev[w[0]] = v
                    H[w[0]] = dist[w[0]]
    return(mst_weight)

start = timer()
g = Graph(4096,4)
sum(Prims(g))
end = timer()
with open("results.txt", "a") as file:
    file.write(str(end - start) + " ")
