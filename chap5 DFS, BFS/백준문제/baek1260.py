# 1260 DFS와 BFS
n, m, v = map(int, input().split())

graph = [[]]
matrix = [[0, 0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    graph.append(list(map(int, input().replace(" ", ""))))

j = 0
for i in range(1, n + 2):

    matrix[i][0] = graph[i][1]


print(matrix)


def dfs(graph, n, visitied):
    visitied[n] = True
    print(n, " ")


# def dfs(graph, n, visited):
#     visited[n] = True
#     print(n, end=" ")
#     for i in graph[n]:
#         if not visited[i]:
#             dfs(graph, i, visited)


visited = [False] * (n + 1)

# dfs(graph, v, visited)
