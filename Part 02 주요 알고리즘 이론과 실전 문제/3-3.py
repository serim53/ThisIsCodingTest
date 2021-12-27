# 숫자 카드 게임
# 각 행마다 가장 작은 것을 선택하고
# 가장 작은 것 중에 가장 큰 것을 최종적으로 선택

# N, M을 공백으로 구분하여 입력받기 (n은 행, m은 열)
n, m = map(int, input().split())
# 결과
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
