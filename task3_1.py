import numpy as np
import matplotlib.pyplot as plt

while True:
    R = float(input('Введите значение R (>0): '))
    if R > 0:
        break

xn = -5
xk = 5
dx = 1
y_arr = []
x_arr = []
x1 = np.arange(-3, -1, 0.001)

for x in range(xn, xk+1, dx):
    if (x >= -5) and (x <= -3):
        y_arr.append(1)
        plt.plot([-5, -3], [1, 1], c='black')
    elif (x > -3) and (x < -1):
        y_arr.append(-np.sqrt(R ** 2 - (x + 1) ** 2))
        plt.plot(x1, -np.sqrt(R ** 2 - (x1 + 1) ** 2), c='black')
    elif (x >= -1) and (x <= 2):
        y_arr.append(-2)
        plt.plot([-1, 2], [-2, -2], c='black')
    elif (x > 2) and (x <= 5):
        y_arr.append(x - 4)
        plt.plot([2, 5], [-2, 1], c='black')
    x_arr.append(x)

plt.scatter(x_arr, y_arr, marker='o', c='red', s=20)
plt.ylim(-7, 7)
plt.xlim(-7, 7)
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.grid()
plt.show()



