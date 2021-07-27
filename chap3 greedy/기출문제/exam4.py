n = int(input())
mycoin = list(map(int, input().split()))

mycoin.sort(reverse=True)
xcoin = 1

print(xcoin in mycoin)
