x = int(input())

array = [0] * 1000001

for i in range(1, x + 1):
    if i == 1:
        array[i] = 0
    else:
        array[i] = array[i - 1] + 1
        if i % 3 == 0:
            array[i] = min(array[i], array[i // 3] + 1)
        if i % 2 == 0:
            array[i] = min(array[i], array[i // 2] + 1)
    if i == x:
        print(array[i])
