# 18310 안테나
n = int(input())
house = list(map(int, input().split()))

house.sort()

# reach = [0] * n
# for i in house:
#     for j in range(0, n):
#         reach[j] = reach[j] + abs(i - house[j])
# print(reach)
# print(house[reach.index(min(reach))])
# 시간 초과

# 그냥 중간값을 찾으면 된다
print(house[round(n / 2) - 1])
