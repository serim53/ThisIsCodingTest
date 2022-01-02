# 성적이 낮은 순서로 학생 출력하기

# N 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# key를 이용하여, 점수를 기준으로 정렬
# lambda: 익명함수를 지칭하는 용어. 즉, 기존의 함수(명 등)을 선언하고 사용하던 방식과는 달리 바로 정의하여 사용할 수 있는 함수.
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')