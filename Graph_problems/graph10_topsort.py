from Graph_problems import graph11_DirectedaCylicGraph


def dfs(graph,start,visited,order_stack):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph,node,visited,order_stack)

    order_stack.append(start)

def topsort(graph):
    if graph11_DirectedaCylicGraph.isCyclic(graph):
        print("Graph is cyclic")
        return
    visited = []
    order_stack = []

    for node in graph:
        if node not in visited:
            dfs(graph,node,visited,order_stack)

    order_stack.reverse()
    return order_stack



if __name__ == "__main__":

        n = int(input())
        graph = {}
        for i in range(n):
            u,v = list(input().split())
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v not in graph:
                graph[v] = []

        print(graph)
        path = topsort(graph)
        print(path)

# Sample input
# 6
# A B
# A C
# B D
# C D
# C E
# D E