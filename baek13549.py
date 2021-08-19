# 13549 숨바꼭질3
n, k = map(int, input().split())

cnt = 0

while True:
    if n * 2 <= k:
        n = n * 2
        cnt = cnt + 1
    else:
        n = n - 1
        cnt = cnt + 1
