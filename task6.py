class Zodiac:
    def __init__(self, surn, nm, dt):
        self.surname = surn
        self.name = nm
        self.date = dt
        self.zodiac = oracle(self.date)

    def display_info(self):
        print(f'\n\nФИО: {self.surname} {self.name}')
        if self.date[1] < 10 and self.date[0] < 10:
            print(f'Дата рождения: 0{self.date[0]}.0{self.date[1]}.{self.date[2]}')
        elif self.date[1] < 10 and self.date[0] > 9:
            print(f'Дата рождения: {self.date[0]}.0{self.date[1]}.{self.date[2]}')
        elif self.date[1] > 9 and self.date[0] < 10:
            print(f'Дата рождения: 0{self.date[0]}.{self.date[1]}.{self.date[2]}')
        else:
            print(f'Дата рождения: {self.date[0]}.{self.date[1]}.{self.date[2]}')
        print(f'Знак зодиака: {self.zodiac}')


def oracle(date):
    if (date[0] > 22 and date[1] == 12) or (date[0] < 21 and date[1] == 1):
        return 'Козерог'
    elif (date[0] > 20 and date[1] == 1) or (date[0] < 20 and date[1] == 2):
        return 'Водолей'
    elif (date[0] > 19 and date[1] == 2) or (date[0] < 21 and date[1] == 3):
        return 'Рыбы'
    elif (date[0] > 20 and date[1] == 3) or (date[0] < 21 and date[1] == 4):
        return 'Овен'
    elif (date[0] > 20 and date[1] == 4) or (date[0] < 22 and date[1] == 5):
        return 'Телец'
    elif (date[0] > 21 and date[1] == 5) or (date[0] < 22 and date[1] == 6):
        return 'Близнецы'
    elif (date[0] > 21 and date[1] == 6) or (date[0] < 22 and date[1] == 7):
        return 'Рак'
    elif (date[0] > 22 and date[1] == 7) or (date[0] < 22 and date[1] == 8):
        return 'Лев'
    elif (date[0] > 21 and date[1] == 8) or (date[0] < 24 and date[1] == 9):
        return 'Дева'
    elif (date[0] > 23 and date[1] == 9) or (date[0] < 24 and date[1] == 10):
        return 'Весы'
    elif (date[0] > 23 and date[1] == 10) or (date[0] < 23 and date[1] == 11):
        return 'Скорпион'
    elif (date[0] > 22 and date[1] == 11) or (date[0] < 23 and date[1] == 12):
        return 'Стрелец'


def date_checker(date):
    if 0 < date[1] < 13:
        if date[1] % 2 == 1 and not(0 < date[0] < 32):
            return False
        if date[1] % 2 == 0 and (not(0 < date[0] < 31) and date[1] != 2 or date[1] == 2 and not(0 < date[0] < 30)):
            return False
    else:
        return False
    return True


def main():
    zod_arr = []
    surn = nm = ''
    date = []
    for i in range(1, 9):
        print(f'\n\nДобавление нового объекта Zodiac...\t[{i}/8]')
        while True:
            surn = input('\nВведите фамилию: ')
            nm = input('Введите имя: ')
            if surn.isalpha() and nm.isalpha():
                break
            else:
                print('\nНеправильный формат имени и/или фамилии!!!\n')
        while True:
            dd = int(input('Введите день рождения: '))
            mm = int(input('Введите месяц рождения (01-12): '))
            yyyy = int(input('Введите год рождения: '))
            date = [dd, mm, yyyy]
            if date_checker(date):
                break
            else:
                print('\nНеправильный формат даты!!!\n')
        zod_arr.append(Zodiac(surn, nm, date))

    while True:
        month = int(input('\nВведите месяц рождения (01-12), по которому надо найти людей: '))
        if 0 < month < 13:
            break
        else:
            print('Неправильный формат!!!')

    count = 0
    zod_arr = sorted(zod_arr, key=lambda k: k.zodiac)
    for item in zod_arr:
        if item.date[1] == month:
            Zodiac.display_info(item)
            count += 1

    if count == 0:
        print(f'\nЛюдей, родившихся в {month}-й месяц рождения не нашлось!!!')

    fname = input('\n\nВведите имя нового файла для сохранения объектов: ')
    file = open(f'{fname}.txt', 'w', encoding='utf-8')
    for item in zod_arr:
        file.write(f'{item.surname};{item.name};'
                   f'{item.date[0]}.{item.date[1]}.{item.date[2]};'
                   f'{item.zodiac}\n')

    return


if __name__ == "__main__":
    main()
