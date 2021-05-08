#concepts : connected nodes in graph, adjencylist , non-connected nodes,dfs


def dfs(node,graph,visited,temp=[]):
    temp.append(node)
    visited[node] = True

    for n in graph[node]:
        if visited[n] == False:
            t = dfs(n,graph,visited,temp)

    return temp


def maxfund(n,pairs,fund):
    graph = {}
    for i in range(1,n+1):
        graph[i] = []
    for u,v in pairs:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    connected = []
    visited = {}
    for node in graph:
        visited[node] = False
    print(visited)
    for node in graph:
        if visited[node] == False:
            temp = []
            node_grp = dfs(node,graph,visited,temp)
            #print(node_grp)
            connected.append(node_grp)

    print(connected)
    max_fund = []
    for grp in connected:
        summ = 0
        for p in grp:
            summ = summ + fund[p-1]
        max_fund.append(summ)

    print(max_fund)

    return max(max_fund)


if __name__ == '__main__':
    n = int(input())
    fund = list(map(int,input().split()))
    p = int(input())
    pairs = []
    for i in range(p):
        pair = tuple(map(int,input().split()))
        pairs.append(pair)

    result = maxfund(n,pairs,fund)
    print(result)