# 1260 DFS와 BFS
n, m, v = map(int, input().split())

graph = []

for i in range(m):
    graph.append(list(map(int, input().replace(" ", ""))))


def dfs(graph, n, visited):
    visited[n] = True
    print(n + 1, end=" ")
    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * m

dfs(graph, 0, visited)
