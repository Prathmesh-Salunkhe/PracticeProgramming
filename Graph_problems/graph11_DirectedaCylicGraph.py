def dfs(graph,start,visited):
    for node in graph[start]:
        if node in visited:
            return True
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n,visited)

    return False



def isCyclic(graph):
    visited = []
    for node in graph:
        visited.append(node)
        cyc = dfs(graph,node,visited)
        if cyc is True:
            return True
        visited.remove(node)

    return False



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
        cyclic = isCyclic(graph)
        print(cyclic)

# Sample input
# 6
# A B
# A C
# B D
# C D
# D E
# E C