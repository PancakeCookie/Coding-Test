# 13549 숨바꼭질3

# from collections import deque


# n, k = map(int, input().split())
# max = 100001
# def bfs(start, end):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         node = queue.popleft()
#         if node == end:
#             break
#         tozero = node
#         for i in range(1000):
#             if tozero < max and visited[i] == False and tozero not in queue:
#                 queue.append(tozero)
#                 visited[tozero] = True
#                 cntlist[tozero] = cntlist[node]
#                 tozero = tozero * 2
#         print(queue)
#         move = [node-1, node+1]
#         for i in move:
#             if 0 <= i < max and visited[i] == False:
#                 queue.append(i)
#                 cntlist[i] = cntlist[node] + 1
#                 visited[i] = True
#     print(cntlist[end])

# cntlist = [0] * max
# visited = [False] * max

# bfs(n, k)



# --------------------------------------------------------------------------------------------------------------------------------------

from collections import deque

n, k = map(int, input().split())

def bfs(start, end):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        if node == end:
            break
        teleport = [node*2]
        moves = [node-1, node+1]
        for move in teleport:
            if 0 <= move < max and visited[move] == False: 
                cntlist[move] = cntlist[node]
                visited[move] = True
                queue.append(move)
        for move in moves:
            if 0 <= move < max and visited[move] == False: 
                cntlist[move] = cntlist[node] + 1
                visited[move] = True
                queue.append(move)

                
    print(cntlist[end])
    
max = 100001

# -1로 초기화하면 한번에 가능
cntlist = [0] * max
visited = [False] * max

# 당연히 씨발 큐에 리스크가 없는 텔레포트가 먼저 가야되지않나 이런 생각을 해봅니다

bfs(n, k)



