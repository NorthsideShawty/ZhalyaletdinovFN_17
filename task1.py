import math

while True:
    m = float(input("Введите число больше 0: "))
    if m > 0:
        break

z1 = math.sqrt((3*m+2)**2 - 24*m)/(3*math.sqrt(m)-(2/math.sqrt(m)))
z2 = -math.sqrt(m)

res = 'совпали'
if round(z1, 3) != round(z2, 3):
    res = 'НЕ совпали'

print("Результат z1 (%.3f) и Результат z2 (%.3f) %s" % (z1, z2, res))
