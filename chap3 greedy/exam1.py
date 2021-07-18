# 모험가 길드
n = 6
inputdata = [1, 1, 1, 1, 2, 4]

guild = 0
input.sort()

for i in range(0, n):
    n = n - input[i]
    if n >= 0:
        guild = guild + 1
        if n == 0:
            print(guild)
            break
    else:
        print(guild)
        break
