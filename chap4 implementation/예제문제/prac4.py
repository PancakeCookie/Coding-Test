# 게임 개발
n, m = list(map(int, input().split()))

col, low, dir = list(map(int, input().split()))


mapinfo = [[0] * m for _ in range(n)]

for i in range(0, n):  # 포문 if문! 리스트[[1,2] , 5]
    for j in range(0, m):
        mapinfo[i][j] = list(map(int, input().split()))

print(mapinfo)
