# 2938 설탕배달
sugar = int(input())

bag = 0
while True:
    if sugar == 0:
        print(bag)
        break
    elif (sugar % 5) == 0:
        bag = bag + 1
        sugar = sugar - 5

    elif (sugar % 3) == 0:
        bag = bag + 1
        sugar = sugar - 3

    elif sugar > 3:
        bag = bag + 1
        sugar = sugar - 3

    elif sugar == 0:
        print(bag)

    else:
        print(-1)
        break
