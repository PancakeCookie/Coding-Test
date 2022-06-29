n = int(input())
while len(str(n)):
    
    one = "1"
    answer = 0
    while True:
        if int(one) % n == 0: # 쩝... 순서 조심
            answer = len(list(one))
            print(answer)
            break
        else: 
            one = one + "1"
    try:
        n = int(input())
    except:
        break

# def haha(x):
#       num = 0
#   i = 1
#   while True :
#     num = num * 10 + 1
#     num %= x
#     if num == 0 :
#       print(i)
#       break
#     i+=1

# while True :
#   try :
#     n = int(input())
#     haha(n)
#   except :
#     break