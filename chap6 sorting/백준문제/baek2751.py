# 2751 수 정렬하기 2
n = int(input())
numlist = []
for i in range(n):
    numlist.append(int(input()))

numlist.sort()

for i in range(n):
    print(numlist[i])
