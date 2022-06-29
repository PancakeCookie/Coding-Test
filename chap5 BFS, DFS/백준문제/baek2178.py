# 2178 미로 탐색

n, m = map(int, input().split())

maze = []
for i in range(n):
    mazestr = input()
    maze.append(list(mazestr))

from collections import deque
import queue

def bfs(start, end):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    cnt = 1
    dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]
    while queue:
        node = queue.popleft()
        print(node)
        if node == end:
            print(cnt)
            break
        for dx, dy in dir:
            # 아 조건은 위에서 체크해줘야된다 ~
            if 0 <= node[0]+dx < n and 0 <= node[1]+dy < m:
                # 아 위에 maze는 str이다 ~
                if int(maze[node[0]+dx][node[1]+dy]) == 1 and visited[node[0]+dx][node[1]+dy] == False:
                    queue.append([node[0]+dx, node[1]+dy])
                    visited[node[0]+dx][node[1]+dy] = True
        # for문에 있는 queue에 append 되는 애들은 동일한 cnt를 가지니까 cnt는 for문 밖으로
        cnt += 1

# cnt 방법1 visited를 0으로 한다음에 증가
# cnt 방법2 queue에 cnt넣기 - 탈락
visited = [[False]*m for _ in range(n)]

# 아 여기 인덱스도 맞춰줘야지 ~
bfs([0,0], [n-1, m-1])

