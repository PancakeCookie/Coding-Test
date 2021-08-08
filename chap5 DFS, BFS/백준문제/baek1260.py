# 1260 DFS와 BFS
from collections import deque

n, m, v = map(int, input().split())

graph = []
for i in range(m):
    a, b = map(int, input().split())
    graph.append([a, b])
    graph.append([b, a])
# 입력을 뒤집어서 그래프에 추가해서 모든 노드의 연결관계 입력

graph.sort(key=lambda x: x[1])
graph.sort(key=lambda x: x[0])
# 입력의 뒤 값 먼저 정렬한 후 앞 값 정렬

visited = [False] * (n + 1)


def dfs(start):
    visited[start] = True  # 시작노드를 방문처리
    print(start, end=" ")
    for i in range(len(graph)):
        if graph[i][0] == start and visited[graph[i][1]] != True:
            # visited[graph[i][1]] = True
            dfs(graph[i][1])


dfs(v)

print("")

visited = [False] * (n + 1)  # BFS를 위해 방문 리스트 초기화

queue = deque()


def bfs(start):
    queue.append(start)  # 큐에 시작 노드 넣고
    visited[start] = True  # 방문처리
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in range(len(graph)):
            if graph[i][0] == node and visited[graph[i][1]] != True:
                visited[graph[i][1]] = True
                queue.append(graph[i][1])


bfs(v)

# sep=" "
# 이 옵션을 이용하게 되면 print문의 출력문들 사이에 해당하는 내용을 넣을 수 있습니다.
# 기본 값으로는 공백이 들어가 있으며 이를 사용해 원하는 문자를 입력할 수 있습니다.

# end=" "
# 이 옵션의 경우 print 문을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있습니다.
# 기본 값으로는 개행(\n)이 들어가 있으며 이를 사용해 개행을 없애거나 원하는 문자를 입력할 수 있습니다.

# l = [[] for i in range(n + 1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     l[a].append(b)
#     l[b].append(a)
#     l[a].sort()
#     l[b].sort()

# print(l)
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

# n, m, v = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# for i in range(m):
#     node1 , node2 = map(int,input().split())
#     graph[node1].append(node2)
#     graph[node2].append(node1)
# for i  in range(n+1):
#     graph[i].sort()

# check_dfs = [False] * (n+1)
# check_bfs = [False] * (n+1)

# def DFS(v):
#     check_dfs[v] = True
#     print(v, end = ' ')
#     for value in graph[v] :
#         if check_dfs[value] == False :
#             DFS(value)
# DFS(v)
# print()

# def BFS(v):
#     check_bfs[v] = True
#     q = deque([v])
#     while q:
#         now = q.popleft()
#         print(now, end= " ")
#         for value in graph[now]:
#             if check_bfs[value] == False :
#                 q.append(value)
#                 check_bfs[value] = True
# BFS(v)
