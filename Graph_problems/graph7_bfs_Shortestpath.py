def bfs(graph,start,end):
    visited = []
    bfs_trav = []
    level = {}
    parents = {}
    q = []

    q.append(start)
    visited.append(start)
    bfs_trav.append(start)
    level[start] = 0
    parents[start] = None

    while len(q) > 0:
        parent = q.pop(0)
        visited.append(parent)

        for child in graph[parent]:
            if child not in visited:
                q.append(child)
                visited.append(child)
                parents[child] = parent
                bfs_trav.append(child)
                level[child] = level[parent] + 1

    path = []
    child = end

    while child is not None:
        path.append(child)
        child = parents[child]

    path.reverse()
    return path










if __name__ == "__main__":

        n = int(input())
        graph = {}
        for i in range(n):
            u,v  = list(input().split())
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]

            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]

        start = 'A'
        end = 'E'
        path = bfs(graph,start,end)
        print(path)


#Sample input
# 6
# A B
# B D
# A C
# C D
# C E
# E D