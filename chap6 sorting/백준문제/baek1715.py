# 1715 카드 정렬하기
import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
que = PriorityQueue()
for i in range(n):
    que.put(int(input()))

cnt = 0

while True:
    if n == 1:
        break
    a = que.get()
    b = que.get()
    cnt = cnt + a + b
    if not que.empty():
        que.put(a + b)
    else:
        break

if n == 1:
    sys.stdout.write(str(0))
else:
    sys.stdout.write(str(cnt))

# def solution(L, x):
#     for i in range(len(L)):
#         if L[i] > x:
#             break
#         i += 1
#     L.insert(i, x)


# decklist.sort()
# cnt = 0
# while True:
#     if len(decklist) >= 3:
#         # decklist.append(decklist[0] + decklist[1])
#         solution(decklist, decklist[0] + decklist[1])
#         cnt = cnt + decklist[0] + decklist[1]
#         del decklist[0]
#         del decklist[0]

#     else:
#         cnt = cnt + decklist[0] + decklist[1]
#         sys.stdout.write(str(cnt))
#         break
