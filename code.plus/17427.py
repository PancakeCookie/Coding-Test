# 17427 약수의 합 2

# 내가 만든 채 -> 존나 오래걸림
# allnum = list(range(2,10001))
# divnum = 2
# allnum2 = allnum[:]
# for num in allnum:
#     if num % divnum == 0:
#         for i in range(1, int(10001/divnum)):
#             if divnum*(i+1) in allnum2:
#                 allnum2.remove(divnum*(i+1))
#     divnum = divnum +1
# print(len(allnum2))

# 멀쩡한 채
# import math

# maxnum = 1000000
# allprime = [False, True] + [True for i in range(2,maxnum+1)] # 0, 1 // 2~1000000
# for i in range(2, int(math.sqrt(maxnum))+1): # 제곱근까지만 판별해도 됨
#     if allprime[i] == True: # i가 소수인 경우
#         j = 2
#         while i*j <= maxnum:
#             allprime[i*j] = False
#             j = j + 1 

# for i in range(1, maxnum+1):
#     if allprime[i]:
#         print(i)

# realprime = []
# for idx, bool in enumerate(allprime):
#     if bool == True:
#         realprime.append(idx)
# print(realprime)
