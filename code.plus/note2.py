n, m = map(int, input().split())

from itertools import permutations

num_list = range(1,n+1)
perm_list = permutations(num_list, m)
for perm in perm_list:
    # 이거 대신 .join도 가능했음
    for i in perm:
        print(i, end=" ") 
    print("")