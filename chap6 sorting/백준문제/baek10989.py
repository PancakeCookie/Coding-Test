# 10989 수 정렬하기 3
import sys

input = sys.stdin.readline

n = int(input())
count = [0] * (10000 + 1)

for i in range(n):
    count[int(input())] += 1

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            sys.stdout.write(str(i) + "\n")

# sys를 씁시다
