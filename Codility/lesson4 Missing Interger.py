def solution(A):
    A.sort()
    min = 1
    for i in A:
        if i == min:
            min += 1
    return min