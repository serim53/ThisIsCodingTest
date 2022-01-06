# 효율적인 화폐 구성

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계싼된 결과를 저장하기 위한 DP 테이블 초기화
# 10001은 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않다는 의미이다.
# M의 최대 크기가 10000이므로 불가능한 수로 10001이라는 값을 설정했다.
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 (보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])