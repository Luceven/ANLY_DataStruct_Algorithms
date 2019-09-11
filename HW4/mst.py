#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:51:46 2019

@author: katezeng
"""

import random

# to generate the uniformly random weights of the tree
def weightGenerator(num_edg):
    mylist = [0]*num_edg
    for i in range(num_edg):
        mylist[i] = random.uniform(0,1)
    return mylist

class Vertex:
    def __init__(self, key):
        self._neighbors = []
        self._key = key

    def add_neighbor(self, neighbor_vertex, weight):
        self._neighbors.append((neighbor_vertex, weight))

    def get_connections(self):
        return self._neighbors

    def get_key(self):
        return self._key

    def get_weight(self, to_vertex):
        for neighbor in self._neighbors:
            if to_vertex == neighbor[0].get_key():
                return neighbor[1]

class UnionFind:
    def __init__(self, n):
        self._n = n
        self._parent = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]
        
    def find(self, x):
        if(x != self._parent[x]):
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self, x, y):
        (x_root, y_root) = (self.find(x), self.find(y))
        if x_root == y_root:
            return
        
        if self._rank[x_root] < self._rank[y_root]:
            self._parent[x_root] = y_root
        elif self._rank[y_root] < self._rank[x_root]:
            self._parent[y_root] = x_root
        else:
            self._parent[y_root] = x_root
            self._rank[x_root] += 1
            
    def __str__(self):
        return str(self._parent)


class Graph:
    def __init__(self):
        self._vertices = {}
        
    def add_vertex(self, vertex):
        v = Vertex(vertex)
        self._vertices[vertex] = v

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self._vertices:
            self.add_vertex(from_vertex)

        if to_vertex not in self._vertices:
            self.add_vertex(to_vertex)

        self._vertices[from_vertex].add_neighbor(self._vertices[to_vertex], weight)
        
    def get_vertices(self):
        vertices = self._vertices.keys()
        vertices.sort()
        return vertices

    def get_edges(self):
        edges = []
        for vertex in self._vertices:
            neighbors = self._vertices[vertex].get_connections()
            for neighbor in neighbors:
                edges.append((vertex, neighbor[0].get_key(), self._vertices[vertex].get_weight(neighbor[0].get_key())))

        return edges

    def get_vertex(self, vertex_key):
        for v in self._vertices:
            if v == vertex_key:
                return self._vertices[v]
        return None
            
    def kruskals(self):
        res = []
        num_v = len(self._vertices)
        uf = UnionFind(num_v)
        
        edges = sorted(self.get_edges(), key = lambda x: x[2])
        
        for e in edges:
            vertex1 = e[0]
            vertex2 = e[1]
            
            if uf.find(vertex1) != uf.find(vertex2):
                uf.union(vertex1, vertex2)
                res.append(e)
                
            if len(res) == num_v - 1:
                break
            
        return res
    
    ## prim, without testing at this point
    def prim(self):
        # initialize the MST
        res = set()
        # create a set that keeps track of vertices already included in MST
        X = set()
    
        # select an arbitrary vertex to begin with
        # assign key value as 0 for the first vertex so that it is picked first
        X.add(0)
        while len(X) != self._vertices:
            crossing = set()
            # for each element x in X, add the edge (x, k) to crossing if
            # k is not in X
            for x in X:
                for k in range(len(self._vertices)):
                    if k not in X and self.get_edges() != 0:
                        crossing.add(self.get_edges())
            # find the edge with the smallest weight in crossing
            edge = sorted(crossing, key = lambda x: x[2])
            print(edge)
            
            # add this edge to MST
            res.add(edge)
            print(res)
            # add the new vertex to X
            X.add(edge[1])
            print(X)
        return res
    
    
    
if __name__ == "__main__":

    """
    # Graph constructed as a directed graph removing redundant edges
    graph = {
        "0" : [("1", 1), ("2", 2), ("3", 3)],
        "1" : [("2", 1)],
        "2" : [],
        "3" : [("2", 6)]
    }
    """

    g = Graph()

    for v in range(4):
        g.add_vertex(v)

    g.add_edge(0, 1, random.uniform(0,1))
    g.add_edge(0, 2, random.uniform(0,1))
    g.add_edge(0, 3, random.uniform(0,1))
    g.add_edge(1, 2, random.uniform(0,1))
    g.add_edge(3, 2, random.uniform(0,1))

    # choose to use kruskals or prim
    #m_spanning_tree_edges = g.kruskals()
    m_spanning_tree_edges = g.prim()
    
    # find weight
    total_weight = 0
    for e in m_spanning_tree_edges:
        total_weight += e[2]

    print("The edges in the minimum spanning tree are: {}"
        .format(m_spanning_tree_edges), "and the total weight is: {}".format(total_weight))