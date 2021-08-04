# 10989 수 정렬하기 3
n = int(input())
numlist = []
for i in range(n):
    numlist.append(int(input()))

count = [0] * (10000 + 1)
for i in range(len(numlist)):
    count[numlist[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
