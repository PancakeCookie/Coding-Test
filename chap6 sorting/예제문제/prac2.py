# 성적이 낮은 순서로 학생 출력하기
from sys import stdin


n = int(input())

stdinfo = []
for i in range(n):
    stdinfo.append(list(input().split()))

# def setting(data):
#     return data[1]

# stdinfo.sort(key=setting)

stdinfo.sort(key=lambda x: x[1])  # 인수 x를 x[1]로

print(stdinfo)
# 성적 범위가 1~100 이니 계수 정렬을 이용한다
# 만약 데이터가 크면 계수정렬로
