number = input()

number = list(number)
resultA = 0
resultB = 0

for i in range(0, int(len(number) / 2)):
    resultA = resultA + int(number[i])

for i in range(int(len(number) / 2), len(number)):
    resultB = resultB + int(number[i])

if resultA == resultB:
    print("LUCKY")
else:
    print("READY")
