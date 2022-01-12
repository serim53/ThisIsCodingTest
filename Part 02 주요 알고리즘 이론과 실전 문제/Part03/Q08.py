# 문자열 재정렬

s = input()
sString = []
sInt = 0

for i in range(len(s)):
    if 48 <= ord(s[i]) <= 57:
        sInt += int(s[i])
    else:
        sString.append(s[i])

sString.sort()

if sInt != 0:
    sString.append(str(sInt))

print(''.join(sString))
