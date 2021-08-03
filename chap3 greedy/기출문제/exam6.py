# 무지의 먹방 라이브
food_times = list(map(int, input().split()))
k = int(input())

eattime = 1

while True:
    for i in range(len(food_times)):
        if food_times[i] > 0:
            food_times[i] = food_times[i] - 1
            eattime = eattime + 1

            if eattime == k:
                print(i + 1)
            break

        else:
            i = i + 1
