# 거스름돈
inmoney = 1260

givecoin = 0
# / 나누기 연산자, // 몫 연산자, % 나머지 연산자

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    givecoin = givecoin + inmoney // coin
    inmoney = inmoney % coin

print(givecoin)
