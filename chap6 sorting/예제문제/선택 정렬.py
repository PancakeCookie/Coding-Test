# 선택 정렬 = 가장 작은 데이터를 선택해 맨 앞 데이터와 바꾸는 것을 반복
# 시간 복잡도 O(n^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 아직 가장 작은 수는 아님
    for j in range(i + 1, len(array)):  # 가장 작은 수의 인덱스를 찾는 과정
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 찾았으니 바꿈

print(array)
