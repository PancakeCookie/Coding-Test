# 시각
n = int(input())

threecnt = 0

for i in range(0, n + 1):
    if i == (3 or 13 or 23):
        threecnt = threecnt + 3600
    else:
        threecnt = threecnt + 45 * 15 + 15 * 60

print(threecnt)
# 이렇게 말고 문자형으로도 가능
