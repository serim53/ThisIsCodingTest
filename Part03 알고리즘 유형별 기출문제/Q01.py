# 모험가 길드

# 모험가의 수 N 입력받기
n = int(input())
data = list(map(int, input().split()))

data.sort()

# 총 그룹 수
group = 0
# 현재 그룹에 포함된 모험가의 수
member = 0

for i in data:
    member += 1 # 현재 그룹에 해당 모험가 포함시키기
    # 만약 그룹에 포함된 모험가의 수가 공포도보다 높다면
    if member >= i:
        # 그룹을 증가시키고
        group += 1
        # 모험가 수를 0으로 초기화
        member = 0

print(group)
