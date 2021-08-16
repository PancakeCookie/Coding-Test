# 14502 연구소
from itertools import combinations
import copy

n, m = map(int, input().split())
lab = []

for i in range(n):
    lab.append(list(map(int, input().split())))

lab_copy = copy.deepcopy(lab)  # 다차원 리스트의 복사를 위해 import copy, deepcopy 사용

blank = []  # 0의 위치 저장
virus = []  # 2의 위치 저장

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            blank.append([i, j])
        if lab[i][j] == 2:
            virus.append([i, j])

result = list(combinations(blank, 3))  # 3차원 배열


def insfection(x, y):
    if x - 1 >= 0 and lab_copy[x - 1][y] == 0:  # 상이니까 y좌표는 체크 안해도됨
        lab_copy[x - 1][y] = 2
        insfection(x - 1, y)
    if x + 1 < n and lab_copy[x + 1][y] == 0:
        lab_copy[x + 1][y] = 2
        insfection(x + 1, y)
    if y - 1 >= 0 and lab_copy[x][y - 1] == 0:  # 하니까 x좌표는 체크 안해도됨
        lab_copy[x][y - 1] = 2
        insfection(x, y - 1)
    if y + 1 < m and lab_copy[x][y + 1] == 0:
        lab_copy[x][y + 1] = 2
        insfection(x, y + 1)


count = 0
countlist = []
for i in range(len(result)):
    a, b, c = map(list, result[i])  # 벽 세우기
    lab_copy[a[0]][a[1]] = 1
    lab_copy[b[0]][b[1]] = 1
    lab_copy[c[0]][c[1]] = 1
    for i in range(len(virus)):  # 감염 시키고
        insfection(virus[i][0], virus[i][1])
    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] == 0:  # 0 갯수 세고
                count = count + 1
    countlist.append(count)  # 카운트에 넣은 다음
    lab_copy = copy.deepcopy(lab)  # 초기화
    count = 0

print(max(countlist))
