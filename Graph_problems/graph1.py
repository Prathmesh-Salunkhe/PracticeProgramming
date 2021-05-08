class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for u, v in self.edges:
            if u in self.graph_dict:
                self.graph_dict[u].append(v)
            else:
                self.graph_dict[u] = [v]

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return None

        shortest_path = []

        for node in self.graph_dict[start]:
            sp = self.get_shortest_path(node, end, path)
            if sp:
                if len(shortest_path) == 0 or len(sp) < len(shortest_path):
                    shortest_path = sp

        return shortest_path


routes = [("Mumbai", "Paris"), ("Paris", "New York"), ("Mumbai", "Dubai"), ("Dubai", "New York"), ("Paris", "Dubai")]
g = Graph(routes)

#print(g.graph_dict)
#print(g.get_paths("Mumbai", "New York"))

print(g.get_shortest_path("Mumbai", "New York"))
