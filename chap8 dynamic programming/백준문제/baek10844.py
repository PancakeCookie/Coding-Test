# 10844 쉬운 계단 수
n = int(input())
stepnum = [0] * (n + 1)
cnt = 0
# if x == 0:
#     cnt += 1;
# elif 1 <= x and x <= 8:
#     cnt += 2;
# else:
#     cnt +=1;


for i in range(1, n + 1):
    for j in range(0, 10):
        if 1 <= j and j <= 8:
            cnt += 2

    if i == 1:
        stepnum[i] = 9
    else:
        stepnum[i] += cnt

print(stepnum[n])
# 9 * 2**(n-1) - 안되는거
