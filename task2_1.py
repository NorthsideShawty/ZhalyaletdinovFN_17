import math

while True:
    R = float(input('Введите значение R (>=2): '))
    if R >= 2:
        break

while True:
    x = float(input('Введите значение x [-5; 5]: '))
    if (x >= -5) and (x <= 5):
        break

if (x >= -5) and (x <= -3):
    y = 1
elif (x > -3) and (x < -1):
    y = -math.sqrt(R ** 2 - (x + 1) ** 2)
elif (x >= -1) and (x <= 2):
    y = -2
elif (x > 2) and (x <= 5):
    y = x - 4

print(y)
