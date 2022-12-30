import math as m
import matplotlib.pyplot as plt

while True:
    xn = float(input('Введите Xнач (>0.5): '))
    if xn > 0.5:
        break

while True:
    dx = float(input('Введите шаг (dx>0): '))
    if dx > 0:
        break

while True:
    xk = float(input('Введите Xкон (больше Xнач+dx): '))
    if xk >= xn+dx:
        break

Eps = float(input('Введите точность (Eps): '))

print('\nФункция: ln(x)\nТочность (Eps): %.5f\nШаг (dx): %.3f\nИнтервал: [%.f, %.f]' % (Eps, dx, xn, xk))

count = 0
fx_arr = []
xn_arr = []

while round(xn, 1) <= xk:
    fx = (xn - 1) / xn
    fx0 = 0
    n = 1
    while abs(fx0 - fx) > Eps:
        fx0 = fx
        fx += m.pow(xn - 1, n + 1) / ((n + 1) * m.pow(xn + 1, n + 1))
        n += 1
    xn_arr.append(xn)
    fx_arr.append(fx)

    xn += dx

plt.title('f(x) = ln(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(xn_arr, fx_arr, c='black')
plt.ylim(-xk-2, xk+2)
plt.xlim(-xk-2, xk+2)
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
