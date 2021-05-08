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
            self.adj_mat[u][v] = 1
            self.adj_mat[v][u] = 1
        return self.adj_mat

    def traversal(self):
        visited = [False]*self.no_vertices

        def dfs(node):

            if visited[node]:
                return
            visited[node] = True
            print(node)

            nbrs = self.adj_mat[node]

            for i in range(len(nbrs)):
                if nbrs[i] == 1:
                    dfs(i)
            return

        dfs(0)

    def connected_nodes(self):
        visited = [False]*self.no_vertices
        count = 0
        node_grp = [-1]*self.no_vertices


        def traverse_makevisited(i):
            if visited[i] == True:
                return
            visited[i] = True
            for n in range(len(self.adj_mat[i])):
                #print(n)
                if self.adj_mat[i][n] == 1:
                    if visited[n] == False:
                        node_grp[n] = count         #assigning all the node conntected to the starting node the same grp no
                        traverse_makevisited(n)

        for i in range(self.no_vertices): #self.no_vertices
            #print(i)
            if visited[i] == False:
                count +=1
                node_grp[i] = count         #giving the starting node a no
                traverse_makevisited(i)

        return node_grp


g = Graph([(0,1),(0,3),(1,2),(1,4),(5,6),(6,7)])
print(g.vertices)
print(g.adj_mat)

#g.traversal()
print(g.connected_nodes())