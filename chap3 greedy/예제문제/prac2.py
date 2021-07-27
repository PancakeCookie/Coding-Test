# 큰 수의 법칙
a = [2, 4, 5, 4, 6]

a.sort()

n, m, k = 5, 9, 2

j, sum = 0, 0

for i in range(m):
    if j < k:
        sum += a[4]
        j += 1
    else:
        sum += a[3]
        j = 0

print(sum)
