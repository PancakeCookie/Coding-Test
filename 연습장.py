student = {}
ssac = {}
number = 3
n = []
for i in range(0, 3):
    for j in range(0,3):
        m = list(input().split())
        n.append(m)
    student[n[1][0]] = n[1][1]
    student[n[2][0]] = n[2][1]  
    ssac[n[0][1]] = student
    n=[]

print(ssac)