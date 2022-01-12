# 럭키 스트레이트

n = input()

length = len(n)

sumLeft = 0
sumRight = 0

for i in range(length // 2):
    sumLeft += int(n[i])

for i in range(length//2, length):
    sumRight += int(n[i])

if sumLeft == sumRight:
    print("LUCKY")
else:
    print("READY")
    