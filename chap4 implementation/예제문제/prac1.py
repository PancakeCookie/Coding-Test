# 상하좌우
n = int(input())
move = input().split()

explorer = [1, 1]

for i in move:
    if i == "R":
        if explorer[1] != n:
            explorer[1] = explorer[1] + 1
    elif i == "L":
        if explorer[1] != 1:
            explorer[1] = explorer[1] - 1
    elif i == "U":
        if explorer[0] != 1:
            explorer[0] = explorer[0] - 1
    else:  # i == "D"
        if explorer[0] != n:
            explorer[0] = explorer[0] + 1

print(explorer)
