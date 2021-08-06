# 위에서 아래로
n = int(input())
numlist = []

for i in range(n):
    numlist.append(int(input()))

numlist.sort(reverse=True)

print(numlist)
