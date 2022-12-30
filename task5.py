import array as arr
import random as rand


def array_print(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end="  |  ")
        print()


def row_finder(a, n):
    row = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if a[i][j] > 0:
                count += 1
                break
        if count == 0:
            row = i+1
            break
    return row


def max_replace(a, n):
    for k in range(n):
        row = col = 0
        maximum = -10
        for i in range(n):
            for j in range(n):
                if (i != j) or (i > k):
                    if a[i][j] > maximum:
                        maximum = a[i][j]
                        row, col = i, j
        a[k][k], a[row][col] = a[row][col], a[k][k]
    return a


def main():
    n = 5
    a = arr.array("f")
    a = [[round(rand.triangular(-9, 9, -9), 2) for j in range(n)] for i in range(n)]

    print('Первоначальная матрица: ')
    array_print(a, n)

    row = row_finder(a, n)
    if row == 0:
        print('\n\nСтроки со всеми отрицательными элементами нет!')
    else:
        print(f'\n\nПервая строка со всеми отрицательными элементами: {row}')

    a = max_replace(a, n)
    print('\n\nМатрица после перестановки:')
    array_print(a, n)


if __name__ == "__main__":
    main()
