# 1260 DFS와 BFS

n, m, v = map(int, input().split())
connect = []
for i in range(m):
    start, end = map(int, input().split())
    connect.append([start, end])
    connect.append([end, start])

connect.sort(key= lambda x : (x[0],x[1]))

graph = [[] for _ in range(n+1)]
for i in connect:
    graph[i[0]].append(i[1])  
# print(graph)

visited = [False] * (m+1)

def dfs(graph, node):
    visited[node] = True
    print(node, end=" ")
    for i in graph[node]:
        # 방문 안했으면
        if visited[i] == False:
            dfs(graph, i)


visited = [False] * (m+1)
from collections import deque

def bfs(graph, node):
    # 큐 만들고 시작 노드 넣어줌
    queue = deque([node])
    visited[node] = True
    # 큐가 빌 때 까지
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

# dfs(graph, v)
bfs(graph, v)
    