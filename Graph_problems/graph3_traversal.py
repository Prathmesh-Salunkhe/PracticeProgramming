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

    def traversal(self):
        visited = [False]*self.no_vertices

        def dfs(node):
            node = ord(node) - ord('A')
            if visited[node]:
                return
            visited[node] = True
            print(chr(node + ord('A')))

            nbrs = self.adj_mat[node]

            for i in range(len(nbrs)):
                if nbrs[i] == 1:
                    dfs(chr(i + ord('A')))
            return

        dfs('A')


g = Graph([('A','B'),('A','E'),('B','C'),('B','D')])
print(g.vertices)
print(g.adj_mat)

g.traversal()