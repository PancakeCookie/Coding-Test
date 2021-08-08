n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
for i in range(n + 1):
    graph[i].sort()

print(graph)
check_dfs = [False] * (n + 1)
check_bfs = [False] * (n + 1)


def DFS(v):
    check_dfs[v] = True
    print(v, end=" ")
    for value in graph[v]:
        if check_dfs[value] == False:
            DFS(value)


DFS(v)
print()


def BFS(v):
    check_bfs[v] = True
    q = deque([v])
    while q:
        now = q.popleft()
        print(now, end=" ")
        for value in graph[now]:
            if check_bfs[value] == False:
                q.append(value)
                check_bfs[value] = True


BFS(v)
