# 모험가 길드 => 공포도가 x인 모험가는 반드시 명 이상으로 구성한 모험가 그룹에 참여해야함. 최대 몇개의 모험가 그룹? //28

n = 6
num = [1, 1, 2, 2, 3, 5]

print(num)

num.sort(reverse=True)
list2 = []

for i in range(0, n):
    cnt = 0
    while i < n and num[i] <= (n - i):
        i += num[i]
        cnt += 1
    list2.append(cnt)

print(max(list2))
