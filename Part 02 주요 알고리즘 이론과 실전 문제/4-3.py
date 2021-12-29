# 왕실의 나이트
# 8x8 좌표상에서 이동할 수 있는 경로의 수 반환

# 현재 나이트의 위치 입력받기
input_data = input()
row = input(input_data[1])
# ord() 함수는 문자를 아스키코드로 변환해주는 함수
# 해당 연산을 거치면 a는 1, b는 2로 저장됨
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)