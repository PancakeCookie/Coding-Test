# 1697 숨바꼭질
from collections import deque

n, k = int(input().split())

def bfs(graph, start, visited):
    queue = deque([start])


visited = [0]*(k+1)

