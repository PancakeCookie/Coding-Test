# 음료수 얼려먹기
n, m = map(int, input().split())

ice = []
for i in range(n):
    ice.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    else:
        return False  # ice[x][y] == 1 인 애들


count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count = count + 1

print(count)
