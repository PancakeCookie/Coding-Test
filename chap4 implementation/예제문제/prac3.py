# 왕실의 나이트

current = list(input())

current[0] = int(ord(current[0]))  # 아스키코드로 변환 소문자 a = 97
current[1] = int(current[1])

movecnt = 0

if (97 <= current[0] + 1 and current[0] + 1 <= 103) and (
    1 <= current[1] + 2 and current[1] + 2 <= 8
):
    movecnt = movecnt + 1

if (97 <= current[0] + 1 and current[0] + 1 <= 103) and (
    1 <= current[1] - 2 and current[1] - 2 <= 8
):
    movecnt = movecnt + 1

if (97 <= current[0] - 1 and current[0] - 1 <= 103) and (
    1 <= current[1] + 2 and current[1] + 2 <= 8
):
    movecnt = movecnt + 1
if (97 <= current[0] - 1 and current[0] - 1 <= 103) and (
    1 <= current[1] - 2 and current[1] - 2 <= 8
):
    movecnt = movecnt + 1
if (97 <= current[0] + 2 and current[0] + 2 <= 103) and (
    1 <= current[1] + 1 and current[1] + 1 <= 8
):
    movecnt = movecnt + 1
if (97 <= current[0] + 2 and current[0] + 2 <= 103) and (
    1 <= current[1] - 1 and current[1] - 1 <= 8
):

    movecnt = movecnt + 1
if (97 <= current[0] - 2 and current[0] - 2 <= 103) and (
    1 <= current[1] + 1 and current[1] + 1 <= 8
):
    movecnt = movecnt + 1
if (97 <= current[0] - 2 and current[0] - 2 <= 103) and (
    1 <= current[1] - 1 and current[1] - 1 <= 8
):
    movecnt = movecnt + 1

print(movecnt)
