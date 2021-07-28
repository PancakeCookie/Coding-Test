# 18312 시각
n, m = list(map(int, input().split()))

cnt = 0

# for i in range(0, n + 1):
#     for j in range(0, 60):
#         for k in range(0, 60):
#             if str(m) in str(i) + str(j) + str(k):
#                 cnt = cnt + 1
# 이렇게하면 01시 05분 07초 일때 0 포함된 것을 못 찾음

for i in range(0, n + 1):
    if i < 10:
        i = "0" + str(i)
    for j in range(0, 60):
        if j < 10:
            j = "0" + str(j)
        for k in range(0, 60):
            if k < 10:
                k = "0" + str(k)
            if str(m) in str(i) + str(j) + str(k):
                cnt = cnt + 1
print(cnt)
# 이 외에도 zfill, rjust함수를 사용하는 방법이 있다
