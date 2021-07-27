# 거스름돈
inmoney = 1260

givecoin = 0
# / 나누기 연산자, // 몫 연산자, % 나머지 연산자

if inmoney >= 500:
    givecoin = givecoin + inmoney // 500
    inmoney = inmoney % 500
if inmoney >= 100:
    givecoin = givecoin + inmoney // 100
    inmoney = inmoney % 100
if inmoney >= 50:
    givecoin = givecoin + inmoney // 50
    inmoney = inmoney % 50
if inmoney >= 10:
    givecoin = givecoin + inmoney // 10
    inmoney = inmoney % 10

print(givecoin)

# 동전 종류를 리스트로
