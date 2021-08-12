# 두 배열의 원소 교체
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(a)
print(b)

a.sort()
b.sort(reverse=True)

print(a)
print(b)

cnt = 0

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]

print(sum(a))
