# 문자열 뒤집기
inputdata = list(input())

ziplist = []
for i in range(0, len(inputdata)):
    if inputdata[i] != inputdata[i + 1]:
        ziplist[i] = 1

print(ziplist)
