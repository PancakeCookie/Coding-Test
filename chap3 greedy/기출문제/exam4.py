from itertools import combinations, permutations

n = int(input())
mycoin = list(map(int, input().split()))

mycoin.sort()
possiblecoin = []


combi = list(combinations(mycoin, 2))

print(combi)

# 정답 꼭 체크
