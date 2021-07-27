# 문자열 재정렬
n = input()

englist = [0] * len(n)
numsum = [0] * len(n)
for i in range(0, len(n)):
    if ord(n[i]) >= 65:
        englist[i] = n[i]
    else:
        numsum[i] = n[i]

print(englist, numsum)

# 아스키 코드 0 -> 48, 9 -> 57, A -> 65 Z -> 90, a -> 97, z -> 122
