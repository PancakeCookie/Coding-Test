# 1697 숨바꼭질
from collections import deque

n, k = map(int, input().split())

def bfs(start, end):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        # 현재를 꺼냈잖아 씨발아 
        if node == end:
            break
        ssibal = [node-1, node+1, node*2]
        for i in ssibal:
            if 0 <= i < 100000 + 1 and cntlist[i] == 0 : 
            # i 범위설정 
            # range안에 있고 다음갈 곳이 방문을 안했으면
                queue.append(i)
                cntlist[i] = cntlist[node] + 1 ## cntlist[node] 
    print(cntlist[end])
        
# <= 100 대신 < 100 + 1
# inf = float('inf')
cntlist = [0]*(100000+1)  
# cntlist = [0] * 2 ## [0, 1]
          
# bfs니까 min 아님 dfs로 해야 min임
bfs(n, k)

