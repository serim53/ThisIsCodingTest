
# 거스름돈 금액
n = 1260
# 동전의 개수
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # // 연산자 : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
    count += n // coin
    # 원래 금액에서 현재 코인의 단위로 나눈 후 남은 금액을 n에 다시 저장함
    n %= coin

print(count)

