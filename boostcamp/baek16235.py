# 나무 재테크
n, m, k = map(int, input().split())

ground = [[0] * n for _ in range(n)] # 2차원 리스트컴프리헨션
vital = [[5] * n for _ in range(n)]
a = [[0] * n for _ in range(n)]
tree = [[0] * 3 for _ in range(m)]

for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(m):
    tree[i] = list(map(int, input().split()))
    tree[i][0] = tree[i][0] - 1
    tree[i][1] = tree[i][1] - 1

dx, dy = (0,0,0,1,1,-1,-1,-1), (-1,0,1,-1,1,-1,0,1)

year = 0 
while year <= k:
    year += 1
    
    # 나이가 어린 나무부터 양분을 먹으니 나이순으로 정렬해줌
    tree.sort(key= lambda x:x[2])
    
    # 봄
    for index,[n,m,k] in enumerate(tree):
        if vital[n][m] >= k:
            vital[n][m] = vital[n][m] - k
            tree[index][2] = k+1
        else: # 여름
            vital[n][m] = vital[n][m] + tree[index][2] // 2
            tree[index][2] = 0 
    # 가을

    for N,M,K in tree:
        if (K % 5) == 0:
            for i in range(8):
                if(0<=N+dx[i]<n) and (0<=M+dy[i]<n):
                    tree.append([n+dx[i], m+dy[i],1])
                    
    # 겨울 
    for i in range(n):
        for j in range(n):
            vital[i][j] = vital[i][j] + a[i][j]
    
tree_cnt = 0
for n,m,k in tree:
    if k != 0 :
        tree_cnt += 1
print(tree_cnt)

# for n,m,k in tree:
#     print(n,m,k)
# print(n,m,k)
# print(a)
# print(tree)

# ctrl + D 다중선택
# import copy             # copy 모듈을 가져옴, 2차원 리스트 복사할 떄
# deadtree = copy.deepcopy(tree) 