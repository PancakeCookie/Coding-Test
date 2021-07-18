# 곱하기 혹은 더하기
inputdata = input()

result = 0

for i in range(0, len(inputdata)):
    if result * int(inputdata[i]) > result + int(inputdata[i]):
        result = result * int(inputdata[i])
    else:
        result = result + int(inputdata[i])

print(result)
