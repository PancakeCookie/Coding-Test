# 1931 회의실 배정
n = int(input())

time = [0] * n
usingtime = [0] * n

for i in range(0, n):
    time[i] = list(map(int, input().split()))


print()
