logs = ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]
student = dict()
problem = dict()
for i in range(len(logs)):
    logs[i] = logs[i].split(" ")

logs.sort()
for i in range(len(logs)-1):
    problem[str(logs[i][1])] = logs[i][2]
    student[str(logs[i][0])] =  problem
    if(logs[i][0] != logs[i+1][0]):
        problem = dict()
    if i == len(logs)-2: # 마지막일때
        if(logs[i][0] == logs[len(logs)-1][0]):
            problem[str(logs[len(logs)-1][1])] = logs[len(logs)-1][2]
            student[str(logs[len(logs)-1][0])] =  problem
        else:
            problem = dict()
            problem[str(logs[len(logs)-1][1])] = logs[len(logs)-1][2]
            student[str(logs[len(logs)-1][0])] =  problem
sol5student= []
for i in list(student.keys()):
    if(len(student.get(i))>=5):
        sol5student.append(i)

cheat = set()
for i in sol5student:
    for j in sol5student:
        if(i !=j):
            student.get(i) == student.get(j)
            cheat.add(i)
cheat = list(cheat)
cheat.sort()
if(len(cheat) == 0):
    cheat.append("None")

print(cheat)