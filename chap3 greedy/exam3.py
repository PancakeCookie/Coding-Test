# 문자열 뒤집기
inputdata = list(input())

zerocount = 0
onecount = 0
reversecount = 0


def count():
    zerocount = 0
    onecount = 0
    for i in range(0, len(inputdata)):
        if int(inputdata[i]) == 0:
            zerocount = zerocount + 1
        else:
            onecount = onecount + 1
    return zerocount


while True:
    if count() != (0 or len(inputdata)):
        if zerocount >= onecount:  # 0이 1보다 많거나 같음 -> 1을 0으로
            for i in range(0, len(inputdata)):
                if int(inputdata[i]) == 1:
                    inputdata[i] = "0"
            reversecount = reversecount + 1
        else:  # 1이 0보다 많음 -> 0을 1로
            for i in range(0, len(inputdata)):
                if int(inputdata[i]) == 0:
                    inputdata[i] = "1"
            reversecount = reversecount + 1
    else:
        print(reversecount)
        break
