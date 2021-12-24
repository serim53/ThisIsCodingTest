# 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
# 결과
result = 0
# 더하는 숫자를 세기 위한 변수
count = 0
# 제일 큰 수 True 두번째 큰 수 False
IsMax = True

data.sort()  # 입력받은 수들 정렬하기
big = data[-1]  # 첫번째로 큰 수
secondbig = data[-2]  # 두번째로 큰 수

# k만큼씩 더하면서 총 m번을 더해야 함
# 더하는 수는 첫번째로 큰 수 big, 두번째로 큰 수 secondbig만 있으면 됨
# 첫 번째 큰 수와 두 번재 큰 수를 번갈아가면서 k번씩 더하되, m번의 횟수가 채워지면 그만하도록


while m > 0:
    if m > k:
        if IsMax:
            result += big * k
            m -= k
            IsMax = False
        elif not IsMax:
            result += secondbig
            m -= 1
            IsMax = True
    else:
        if IsMax:
            result += big * m
            m = 0
        elif not IsMax:
            result += secondbig
            result += big * (m-1)
            m = 0

print(result)

