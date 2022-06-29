# 1037 약수

n = int(input())
div_list = list(map(int, input().split()))
print(max(div_list)*min(div_list))