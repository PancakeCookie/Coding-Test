# 미로탈출
from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

queue = deque
visited = [[False] * (n) for _ in range(n)]
cnt = 0

print(visited)


def bfs(x, y):
    queue.append(x, y)
    visited[x][y] = True
    while queue:
        node = queue.popleft()
        cnt = cnt + 1


# return continue break
