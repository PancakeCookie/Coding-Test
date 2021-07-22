# 11047 동전 0


n, k = list(map(int, input().split()))
coinlist = [0] * n
for i in range(0, n):
    coinlist[i] = int(input())

coinlist.sort(reverse=True)
coincnt = 0
i = 0
k // coinlist[i]
while True:
    if k >= coinlist[i]:
        coincnt = coincnt + k // coinlist[i]
        k = k % coinlist[i]
    elif k < coinlist[i]:
        i = i + 1
        if i == n:
            print(coincnt)
            break
