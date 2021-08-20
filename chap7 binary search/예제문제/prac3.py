# 떡볶이 떡 만들기
n, m = map(int, input().split())
dduk = list(map(int, input().split()))

cutline = 1

dduk_cutted = [0] * n

while True:
    for i in range(n):
        if dduk[i] - cutline >= 0:
            dduk_cutted[i] = dduk[i] - cutline
        else:
            dduk_cutted[i] = 0

    if sum(dduk_cutted) >= m:
        cutline = cutline + 1
        dduk_cutted = [0] * n
    else:
        cutline = cutline + 1
        print(cutline)
        break
