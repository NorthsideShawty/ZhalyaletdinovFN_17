import numpy as np
import matplotlib.pyplot as plt

while True:
    R = float(input('Введите аргумент R (>0): '))
    if R > 0:
        break

res_f = '-------------------------\n|  Мишень НЕ поражена!  |\n-------------------------'
res_t = '-------------------------\n|       Попадание!      |\n-------------------------'
count = 0
xshot = []
yshot = []
xmiss = []
ymiss = []

for x in range(1, 11):
    print('\n-------------------------\n|\t\tВыстрел #%d\t\t|\n-------------------------' % x)
    x0 = float(input(' Введите значение x: '))
    y0 = float(input(' Введите значение y: '))

    if (x0 <= 0) and (x0 >= -R) and (y0 >= 0):
        y1 = np.sqrt(R ** 2 - (x0 + R) ** 2)
        if y0 <= y1:
            count += 1
            xshot.append(x0)
            yshot.append(y0)
            print(res_t)
        else:
            xmiss.append(x0)
            ymiss.append(y0)
            print(res_f)
    elif (x0 >= 0) and (x0 <= R) and (y0 <= 0):
        y1 = -1*np.sqrt(R ** 2 - (x0 - R) ** 2)
        if y0 >= y1:
            xshot.append(x0)
            yshot.append(y0)
            print(res_t)
            count += 1
        else:
            xmiss.append(x0)
            ymiss.append(y0)
            print(res_f)
    else:
        xmiss.append(x0)
        ymiss.append(y0)
        print(res_f)

    print('\n:::::::::::::::::::::::::\n:::::::::::::::::::::::::')

print('\nКол-во попаданий: %d/10' % count)

x1 = np.arange(-R, 0, 0.001)
plt.plot(x1, np.sqrt(R ** 2 - (x1 + R) ** 2), [-R, -R], [0, R], c='black')
x1 = np.arange(0, R, 0.001)
plt.plot(x1, -1*np.sqrt(R ** 2 - (x1 - R) ** 2), [R, R], [0, -R], c='black')
plt.plot([-R, R], [0, 0], c='black')
plt.scatter(xmiss, ymiss, marker='o', c='r', s=20)
plt.scatter(xshot, yshot, marker='o', c='g', s=20)
plt.ylim(-11, 11)
plt.xlim(-11, 11)
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.grid()
plt.show()
