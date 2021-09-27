# 2133 타일채우기
n = int(input())

tileable = [0]*(n+1)
tileable[1] = 0
tileable[2] = 3
tileable[3] = 0
tileable[4] = 11
specialtile = [0]*(n+1)
specialtile[4] = 2

for i in range(6,n+1):
    if(i%2 == 0):
        specialtile[i] = specialtile[i-2]*2*3 + specialtile[i-4]*4 + 2



for i in range(6,n+1):
    if(i%2 == 0):
        tileable[i] = (tileable[i-2]*3) + specialtile[i] 
    else:
        tileable[i] = 0;

print(tileable[n])