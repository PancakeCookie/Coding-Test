from itertools import combinations, permutations

n = int(input())
mycoin = list(map(int, input().split()))

mycoin.sort()
possiblecoin = []

for i in range(1, n + 1):
    combi = list(combinations(mycoin, i))

print(combi)
