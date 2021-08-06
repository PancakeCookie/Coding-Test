# 1260 DFS와 BFS
n, m, v = map(int, input().split())

graph = []
for i in range(m):
    a, b = map(int, input().split())
    list1 = [a, b]
    list2 = [b, a]
    graph.append(list1)
    graph.append(list2)

print(graph)
