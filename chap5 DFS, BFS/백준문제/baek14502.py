# 14502 연구소
from itertools import combinations
import copy

n, m = map(int, input().split())
lab = []

for i in range(n):
    lab.append(list(map(int, input().split())))

lab_copy = copy.deepcopy(lab)

blank = []
virus = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            blank.append([i, j])
        if lab[i][j] == 2:
            virus.append([i, j])

result = list(combinations(blank, 3))


def insfection(x, y):
    if x - 1 >= 0 and lab_copy[x - 1][y] == 0:  # 상이니까 y좌표는 체크 안해도됨
        lab_copy[x - 1][y] = 2
        insfection(x - 1, y)
    if x + 1 < n and lab_copy[x + 1][y] == 0:
        lab_copy[x + 1][y] = 2
        insfection(x + 1, y)
    if y - 1 >= 0 and lab_copy[x][y - 1] == 0:
        lab_copy[x][y - 1] = 2
        insfection(x, y - 1)
    if y + 1 < m and lab_copy[x][y + 1] == 0:
        lab_copy[x][y + 1] = 2
        insfection(x, y + 1)


for i in range(len(result)):
    a, b, c = map(list, result[i])
    lab[a[0]][a[1]] = 1
    lab[b[0]][b[1]] = 1
    lab[c[0]][c[1]] = 1

for i in range(len(virus)):
    insfection(i[0], i[1])

print(lab_copy)
