def min_cost(cost,visited):
    min = 100000000
    for key in cost:
        if cost[key] < min and key not in visited:
            min = cost[key]
            min_node = key

    return min_node


def dijkstra(graph,start):
    cost = {}
    parent = {}
    visited = []
    for node in graph:
        cost[node] = 1000000

    cost[start] = 0
    parent[start] = None


    for i in range(len(graph)):
        min_node = min_cost(cost,visited)
        visited.append(min_node)
        for v,w in graph[min_node]:
            if v not in visited:
                new_cost = cost[min_node] + w
                if new_cost < cost[v]:
                    cost[v] = new_cost
                    parent[v] = min_node



    path = []

    for node in graph:
        node_path = []
        child = node
        while child is not None:
            node_path.append(child)
            child = parent[child]
        node_path.reverse()
        path.append(node_path)


    return cost,parent,path


if __name__ == "__main__":

        n = int(input())
        graph = {}
        for i in range(n):
            u,v,w = list(input().split())
            if u in graph:
                graph[u].append((v,int(w)))
            else:
                graph[u] = [(v,int(w))]

            if v in graph:
                graph[v].append((u,int(w)))
            else:
                graph[v] = [(u,int(w))]

        start = 'A'

        print(graph)
        cost,parent,node_path = dijkstra(graph,start)
        print(cost)
        print(parent)
        print(node_path)


#Sample input
# 6
# A B 2
# A C 1
# B D 3
# C D 3
# C E 1
# E D 1