# 미로탈출
from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

def bfs(x, y):
    queue = deque

count = 1

for i in range(n):
    for m in range(m):
