# 1이 될 때까지

# n, k 입력받기
n, k = map(int, input().split())
# 연산 횟수 result
result = 0

while True:
    # n이 1이 되면 연산횟수 출력 후 그만하기
    if n == 1:
        print(result)
        break
    else:
        # n이 k로 완전히 나누어 떨어지면 나누기
        if n % k == 0:
            n = n / k
            result = result + 1
        # n이 k로 완전히 누누어 떨어지지 않으면 n에 -1
        else:
            n = n - 1
            result = result + 1
