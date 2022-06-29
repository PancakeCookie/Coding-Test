# 18405 경쟁적 전염
from collections import deque

n, k = map(int, input().split())

testtube = []
for i in range(n):
    testtube.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

virus = deque()
for i in range(n):
    for j in range(n):
        if testtube[i][j] != 0:
            virus.append([i, j])


print(virus.popleft()[0])


# 전체탐색을 두려워하지말자
# return break continue
