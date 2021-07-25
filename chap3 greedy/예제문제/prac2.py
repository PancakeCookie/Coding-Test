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

 n,m,k = map(int, input().split()) num = list(map(int, input().split())) num.sort() max_list=[] max_list.append(num[n-1]) max_list.append(num[n-2]) #print(max_list) #큰수, 그 다음으로 큰 수가 들어가있음 sum = 0 max_cnt=0 for i in range(0,m): if max_cnt<k: sum = sum+max_list[0] max_cnt = max_cnt+1 else: sum = sum+max_list[1] max_cnt=0 print(sum)