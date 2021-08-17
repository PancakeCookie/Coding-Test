# 1427 소트인사이드
n = input()

forsort = []
for i in range(len(n)):
    forsort.append(n[i])

forsort.sort(reverse=True)

for i in forsort:
    print(i, end="")
