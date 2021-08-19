# 부품 찾기
import sys

input = sys.stdin.readline

n = int(input())
store = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

store.sort()


def binary_search(array, target, start, end):
    if start > end:
        return print("no")
    mid = (start + end) // 2
    if array[mid] > target:
        binary_search(array, target, start, mid - 1)
    elif array[mid] == target:
        return print("yes")
    else:
        binary_search(array, target, mid + 1, end)


for i in range(len(request)):
    binary_search(store, request[i], 0, n - 1)  # 시작과 끝은 배열 값이 아니라 위치 값
