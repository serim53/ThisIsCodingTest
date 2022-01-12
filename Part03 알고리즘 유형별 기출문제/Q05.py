# 볼링공 고르기

n, m =int(input())

weight = list(map(int, input().split()))

array = [0] * 11

for i in weight:
    array[i] += 1

result = 0

for i in range(1, m + 1):
    n -= array[i]   # 무게가 i인 볼링공의 개수 제외
    result += array[i]  # B가 선택하는 경우의 수와 곱하기

print(result)
