# 문자열 재정렬
n = input()

englist = [0] * len(n)
numlist = [0] * len(n)
for i in range(0, len(n)):
    if ord(n[i]) >= 65:
        englist[i] = n[i]
    else:
        numlist[i] = int(n[i])

for i in englist:
    if i == 0:
        englist.remove(0)

englist.sort()
print("".join(englist) + str(sum(numlist)))

# 아스키 코드 0 -> 48, 9 -> 57, A -> 65 Z -> 90, a -> 97, z -> 122
# .isalpha() -> 알파벳이면 true, .isdigit -> 숫자면 true . isalnnum -> 특수문자 있으면 false
# "구분자".join(합칠 리스트) -> 문자열로 이루어진 리스트를 하나의 문자열로
