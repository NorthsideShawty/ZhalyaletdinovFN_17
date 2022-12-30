import math

while True:
    R = float(input('Введите аргумент R (>0): '))
    if R > 0:
        break

x0 = float(input('\nВведите значение x: '))
y0 = float(input('Введите значение y: '))

res_f = '\nТочка с заданными координатами НЕ попала в область'
res_t = '\nТочка с заданными координатами попала в область'

if (x0 <= 0) and (x0 >= -R) and (y0 >= 0):
    y1 = math.sqrt(R ** 2 - (x0 + R) ** 2)
    if y0 < y1:
        print(res_t)
elif (x0 >= 0) and (x0 <= R) and (y0 <= 0):
    y1 = -math.sqrt(R ** 2 - (x0 - R) ** 2)
    if y0 > y1:
        print(res_t)
else:
    print(res_f)
