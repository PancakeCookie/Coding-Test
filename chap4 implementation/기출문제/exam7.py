# 럭키 스트레이트
n = input()

leftsum = 0
rightsum = 0
for i in range(0, int(len(n) / 2)):
    leftsum = leftsum + int(n[i])

for i in range(int(len(n) / 2), len(n)):
    rightsum = rightsum + int(n[i])

if leftsum == rightsum:
    print("LUCKY")
else:
    print("READY")
