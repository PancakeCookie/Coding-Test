# 이진 탐색 예제


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # // 연산자는 나누기 연산 후 소수점을 버리고 정수 부분 수만 구함
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:  # array[mid] < target 인 경우
        return binary_search(array, target, mid + 1, end)


# 이진 탐색 문제는 입력 데이터가 많거나 탐색 범위가 큼
# import sys
# input = sys.stdin.readline
# rstrip() = 공백문자 제거
# int(sys.stdin.readline()) 이런식으로 하면 공백문자가 알아서 사라짐

# strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
# lstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.
# rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.
