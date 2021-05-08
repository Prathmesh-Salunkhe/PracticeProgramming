class Graph:
    def __init__(self,edges):
        self.vertices = []
        self.vertices = self.add_vertices(edges)
        self.no_vertices = len(self.vertices)
        self.adj_mat = self.add_edges(edges)

    def add_vertices(self,edges):
        for u,v in edges:
            if u not in self.vertices:
                self.vertices.append(u)
            if v not in self.vertices:
                self.vertices.append(v)
        return self.vertices

    def add_edges(self,edges):
        self.adj_mat = [[0] * self.no_vertices for i in range(self.no_vertices)]
        for u,v in edges:
            index_u = ord(u) - ord('A')
            index_v = ord(v) - ord('A')
            self.adj_mat[index_u][index_v] = 1
            self.adj_mat[index_v][index_u] = 1
        return self.adj_mat


g = Graph([('A','B'),('B','C')])
print(g.vertices)
print(g.adj_mat)

class Graph_weighted:
    def __init__(self,edges):
        self.vertices = []
        self.vertices = self.add_vertices(edges)
        self.no_vertices = len(self.vertices)
        self.adj_mat = self.add_edges(edges)

    def add_vertices(self,edges):
        for u,v,w in edges:
            if u not in self.vertices:
                self.vertices.append(u)
            if v not in self.vertices:
                self.vertices.append(v)
        return self.vertices

    def add_edges(self,edges):
        self.adj_mat = [[0] * self.no_vertices for i in range(self.no_vertices)]
        for u,v,w in edges:
            index_u = ord(u) - ord('A')
            index_v = ord(v) - ord('A')
            self.adj_mat[index_u][index_v] = int(w)
            self.adj_mat[index_v][index_u] = int(w)
        return self.adj_mat

g_w = Graph_weighted([('A','B','2'),('B','C','3')])
print(g_w.vertices)
print(g_w.adj_mat)

class Graph_directed:
    def __init__(self,edges):
        self.vertices = []
        self.vertices = self.add_vertices(edges)
        self.no_vertices = len(self.vertices)
        self.adj_mat = self.add_edges(edges)

    def add_vertices(self,edges):
        for u,v in edges:
            if u not in self.vertices:
                self.vertices.append(u)
            if v not in self.vertices:
                self.vertices.append(v)
        return self.vertices

    def add_edges(self,edges):
        self.adj_mat = [[0] * self.no_vertices for i in range(self.no_vertices)]
        for u,v in edges:
            index_u = ord(u) - ord('A')
            index_v = ord(v) - ord('A')
            self.adj_mat[index_u][index_v] = 1
        return self.adj_mat


g = Graph_directed([('A','B'),('B','C')])
print(g.vertices)
print(g.adj_mat)

class Graph_directed_weighted:
    def __init__(self,edges):
        self.vertices = []
        self.vertices = self.add_vertices(edges)
        self.no_vertices = len(self.vertices)
        self.adj_mat = self.add_edges(edges)

    def add_vertices(self,edges):
        for u,v,w in edges:
            if u not in self.vertices:
                self.vertices.append(u)
            if v not in self.vertices:
                self.vertices.append(v)
        return self.vertices

    def add_edges(self,edges):
        self.adj_mat = [[0] * self.no_vertices for i in range(self.no_vertices)]
        for u,v,w in edges:
            index_u = ord(u) - ord('A')
            index_v = ord(v) - ord('A')
            self.adj_mat[index_u][index_v] = int(w)
        return self.adj_mat

g_w = Graph_directed_weighted([('A','B','2'),('B','C','3')])
print(g_w.vertices)
print(g_w.adj_mat)

