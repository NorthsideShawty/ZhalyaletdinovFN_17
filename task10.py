class CVehicle:
    def __init__(self, v_type, model_name, speed, price, year_of_release, x_cord, y_cord):
        self.v_type = v_type
        self.model_name = model_name
        self.speed = speed
        self.price = price
        self.year_of_release = year_of_release
        self.x_cord = x_cord
        self.y_cord = y_cord


class CShip(CVehicle):
    def __init__(self, v_type, model_name, speed, price, year_of_release, x_cord, y_cord, pass_num, port):
        super().__init__(v_type, model_name, speed, price, year_of_release, x_cord, y_cord)
        self.pass_num = pass_num
        self.port = port


def getPort():
    while True:
        port = str(input("\tВведите порт приписки корабля: "))
        if port.isalnum():
            break
        else:
            print("\n\tПорт приписки может содержать только буквы или цифры!!!")
    return port


def getShip_pass_num():
    while True:
        pass_num = int(input("\tВведите кол-во пассажиров (макс. - 6500): "))
        if 0 < pass_num < 6501:
            break
        else:
            print("\n\tНекорректное число пассажиров!!!")
    return pass_num


class CCar(CVehicle):
    def __init__(self, v_type, model_name, speed, price, year_of_release, x_cord, y_cord):
        super().__init__(v_type, model_name, speed, price, year_of_release, x_cord, y_cord)


def getPlane_pass_num():
    while True:
        pass_num = int(input("\tВведите кол-во пассажиров (макс. - 100): "))
        if 0 < pass_num < 101:
            break
        else:
            print("\n\tНекорректное число пассажиров!!!")
    return pass_num


class CPlane(CVehicle):
    def __init__(self, v_type, model_name, speed, price, year_of_release, x_cord, y_cord, height, pass_num):
        super().__init__(v_type, model_name, speed, price, year_of_release, x_cord, y_cord)
        self.height = height
        self.pass_num = pass_num


def getHeight():
    while True:
        height = float(input("\tВысота полета (в метрах) (макс. 11000м): "))
        if 0 <= height <= 11000:
            break
        else:
            print("\n\tВысота введена неправильно!!!")
    return height


def carFunction():
    print("\n\nДобавление транспорта (машина)...")
    v_type = "Машина"
    model_name = getModel_name()
    speed = speed_checker()
    price = price_checker()
    yor = yor_checker()
    x_cord, y_cord = coord_getter()
    car = CCar(v_type, model_name, speed, price, yor, x_cord, y_cord)
    lst.append(car)


def shipFunction():
    print("\n\nДобавление транспорта (корабль)...")
    v_type = "Корабль"
    model_name = getModel_name()
    speed = speed_checker()
    price = price_checker()
    yor = yor_checker()
    x_cord, y_cord = coord_getter()
    port = getPort()
    pass_num = getShip_pass_num()
    ship = CShip(v_type, model_name, speed, price, yor, x_cord, y_cord, pass_num, port)
    lst.append(ship)


def planeFunction():
    print("\n\nДобавление транспорта (самолет)...")
    v_type = "Самолет"
    model_name = getModel_name()
    speed = speed_checker()
    price = price_checker()
    yor = yor_checker()
    x_cord, y_cord = coord_getter()
    height = getHeight()
    pass_num = getPlane_pass_num()
    car = CPlane(v_type, model_name, speed, price, yor, x_cord, y_cord, height, pass_num)
    lst.append(car)


def list_checker(lst1):
    if len(lst1) == 0:
        print("\n\nСписок пуст!!!")
        return
    else:
        lst1 = sorted(lst1, key=lambda k: k.v_type)
        count = 1
        print("\n\n")
        for vehicle in lst1:
            veh_print(vehicle, vehicle.v_type, count)
            count += 1


def veh_print(vehicle, v_type, num):
    if v_type == "Машина":
        print(f"{num}. Тип: {v_type} | Модель: {vehicle.model_name}\n"
              f"\tСкорость: {vehicle.speed} | Цена: {vehicle.price:,.2f} руб.| Год выпуска: {vehicle.year_of_release}\n"
              f"\tДолгота: {vehicle.x_cord} | Широта: {vehicle.y_cord}")
    if v_type == "Самолет":
        print(f"{num}. Тип: {v_type} | Модель: {vehicle.model_name}\n"
              f"\tСкорость: {vehicle.speed} | Цена: {vehicle.price:,.2f} | Год выпуска: {vehicle.year_of_release}\n"
              f"\tДолгота: {vehicle.x_cord} | Широта: {vehicle.y_cord}\n"
              f"\t\tКоличество пассажиров: {vehicle.pass_num} | Высота полета: {vehicle.height:,}м")
    if v_type == "Корабль":
        print(f"{num}. Тип: {v_type} | Модель: {vehicle.model_name}\n"
              f"\tСкорость: {vehicle.speed} | Цена: {vehicle.price:,.2f} | Год выпуска: {vehicle.year_of_release}\n"
              f"\tДолгота: {vehicle.x_cord} | Широта: {vehicle.y_cord}\n"
              f"\t\tКоличество пассажиров: {vehicle.pass_num} чел.| Порт приписки: {vehicle.port}")


def coord_getter():
    while True:
        x_cord = float(input("\tВведите долготу (от -180 до 180): "))
        if -180 <= x_cord <= 180:
            break
    while True:
        y_cord = float(input("\tВведите широту (от -90 до 90): "))
        if -90 <= y_cord <= 90:
            break
    return x_cord, y_cord


def getModel_name():
    while True:
        model_name = str(input("\tВведите имя модели транспорта: "))
        if model_name.isalnum():
            break
        else:
            print("\n\tИмя модели может содержать только буквы или цифры!!!")
    return model_name


def price_checker():
    while True:
        price = float(input("\tЦена транспорта в рублях: "))
        if 0 <= price:
            break
        else:
            print("\n\tНеправильная цена!!!")
    return price


def yor_checker():
    while True:
        yor = int(input("\tГод выпуска (c 1930г. по 2022г.): "))
        if 1930 <= yor <= 2022:
            break
        else:
            print("\n\tГод выпуска введен неправильно!!!")
    return yor


def speed_checker():
    while True:
        speed = int(input("\tСкорость транспорта (от 0 до 200 км/ч): "))
        if 0 < speed <= 200:
            break
        else:
            print("\n\tСкорость транспорта введена неправильно!!!")
    return speed


def main():
    while True:
        print('\nМеню (Введите соответствующий пункт): ')
        print('\t1. Добавить машину')
        print('\t2. Добавить самолет')
        print('\t3. Добавить корабль')
        print('\t4. Просмотреть список')
        print('\n\t0. Завершить программу')
        num = int(input('\nНомер задачи: '))
        if num == 1:
            carFunction()
        elif num == 2:
            planeFunction()
        elif num == 3:
            shipFunction()
        elif num == 4:
            list_checker(lst)
        elif num == 0:
            exit()
        else:
            print('Введите номер пункта меню!!!')
            break


if __name__ == "__main__":
    lst = []
    main()
