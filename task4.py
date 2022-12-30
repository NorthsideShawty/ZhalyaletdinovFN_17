import random as rand
import array as arr


def _print(a, n):
    for i in range(n):
        print(a[i], end="  |  ")
    print()


def _fill(a, n):
    a = [round(rand.triangular(-9, 9, 0), 2) for i in range(n)]
    a[rand.randint(0, n-1)] = 0
    return a


def main():
    while True:
        n = int(input('Введите количество элементов массива n: '))
        if n > 2:
            break

    a = arr.array("f")
    last_zero = 0
    summa = 0
    a = _fill(a, n)

    for i in range(0, n):
        if a[i] >= 0:
            summa += 1
        if a[i] == int(0):
            last_zero = i

    print('\n\nОдномерный массив: ')
    _print(a, n)
    print('\nКоличество положительных элементов: %d' % summa)
    summa = 0

    for i in range(last_zero, n):
        summa += a[i]

    print('Сумма элементов после последнего 0: %.2f' % summa)

    for i in range(n):
        for j in range(i, n):
            i_min = i
            if abs(a[i]) >= 1:
                i_min = j
            a[i], a[i_min] = a[i_min], a[i]

    print('\n\nМассив, преобразованный в соотвествии с п.2: ')
    _print(a, n)

    a = [0] + a
    for i in range(2, len(a)):
        if a[i - 1] > a[i]:
            a[0] = a[i]
            j = i - 1
            while a[j] > a[0]:
                a[j + 1] = a[j]
                j = j - 1
            a[j + 1] = a[0]

    a = a[1:]
    print('\n\nСортировка вставками с барьером: ')
    _print(a, n)


if __name__ == "__main__":
    main()
