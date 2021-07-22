# 11399 ATM
n = int(input())
moneytime = list(map(int, input().split()))

moneytime.sort()

lastsum = 0
sum = [0] * n
fullsum = 0

for i in range(0, n):
    sum[i] = lastsum + moneytime[i]
    lastsum = lastsum + moneytime[i]

for i in range(0, n):
    fullsum = fullsum + sum[i]

print(fullsum)
