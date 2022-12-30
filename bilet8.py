class Student:
    def __init__(self, surname, cypher, marks):
        self.surname = surname
        self.cypher = cypher
        self.marks = marks

    def display_info(self):
        pass


def new_student():
    marks = []
    print(f'\n\nДобавление студента...')
    while True:
        surname = input('\nВведите фамилию студента: ')
        if surname.isalpha():
            if surname[:1].isupper() and surname[1:len(surname)].islower():
                break
            else:
                print('\nОшибка!!! Фамилия пишется с большой буквы, а после буквы идут прописью!!!\n')
        else:
            print('\nОшибка!!! Фамилия должна содержать только буквы!!!\n')

    while True:
        cypher = input('\nВведите шифр студента: ')
        if cypher.isalnum():
            break
        else:
            print('\nОшибка!!! В шифре не должно быть спец. символов!!!\n')

    while True:
        math = int(input('Оценка за математику (2-5): '))
        if math in [2, 3, 4, 5]:
            marks.append(math)
            break
        else:
            print('Введите оценку от 2 до 5')
    while True:
        eng = int(input('Оценка за английский язык (2-5): '))
        if eng in [2, 3, 4, 5]:
            marks.append(eng)
            break
        else:
            print('Введите оценку от 2 до 5')
    while True:
        phys = int(input('Оценка за физику (2-5): '))
        if phys in [2, 3, 4, 5]:
            marks.append(phys)
            break
        else:
            print('Введите оценку от 2 до 5')

    stud = Student(surname, cypher, marks)
    file = open('Student.txt', 'a', encoding='utf-8')
    file.write(f'{stud.surname};{stud.cypher};'
               f'{stud.marks[0]};{stud.marks[1]};{stud.marks[2]}\n')
    file.close()

    student_sorter('Student.txt')


def student_sorter(fname):
    stud_arr = []
    with open(fname, 'r', encoding='utf-8') as file:
        students = file.read().split('\n')
    for student in students:
        person = student.split(';')
        stud_arr.append(person)
    stud_arr = stud_arr[:-1]
    pers_arr = []
    for person in stud_arr:
        pers_arr.append(Student(person[0], person[1], [person[2], person[3], person[4]]))
    with open(fname, 'w', encoding='utf-8') as file:
        pers_arr = sorted(pers_arr, key=lambda k: k.cypher)
        for item in pers_arr:
            file.write(f'{item.surname};{item.cypher};'
                       f'{item.marks[0]};{item.marks[1]};{item.marks[2]}\n')


def diplay_all():
    stud_arr = []
    with open('Student.txt', 'r', encoding='utf-8') as file:
        students = file.read().split('\n')
    for student in students:
        person = student.split(';')
        stud_arr.append(person)
    stud_arr = stud_arr[:-1]
    pers_arr = []
    for person in stud_arr:
        pers_arr.append(Student(person[0], person[1], [person[2], person[3], person[4]]))
    for person in pers_arr:
        print(f'\n\nСтудент: {person.surname}\n'
              f'Шифр: {person.cypher}\n'
              f'Оценка по математике: {person.marks[0]}\n'
              f'Оценка по английскому языку: {person.marks[1]}\n'
              f'Оценка по физике: {person.marks[2]}')


def diplay_wo_two():
    stud_arr = []
    with open('Student_wo_bad_marks.txt', 'r', encoding='utf-8') as file:
        students = file.read().split('\n')
    for student in students:
        person = student.split(';')
        stud_arr.append(person)
    stud_arr = stud_arr[:-1]
    pers_arr = []
    for person in stud_arr:
        pers_arr.append(Student(person[0], person[1], [person[2], person[3], person[4]]))
    for person in pers_arr:
        print(f'\n\nСтудент: {person.surname}\n'
              f'Шифр: {person.cypher}\n'
              f'Оценка по математике: {person.marks[0]}\n'
              f'Оценка по английскому языку: {person.marks[1]}\n'
              f'Оценка по физике: {person.marks[2]}')


def delete_bad_ones():
    stud_arr = []
    with open('Student.txt', 'r', encoding='utf-8') as file:
        students = file.read().split('\n')
    for student in students:
        person = student.split(';')
        stud_arr.append(person)
    stud_arr = stud_arr[:-1]
    pers_arr = []
    for person in stud_arr:
        pers_arr.append(Student(person[0], person[1], [person[2], person[3], person[4]]))
    stud_arr = []
    for person in pers_arr:
        if int(person.marks[0]) != 2 and int(person.marks[1]) != 2 and int(person.marks[2]) != 2:
            stud_arr.append(person)
    with open('Student_wo_bad_marks.txt', 'w', encoding='utf-8') as file:
        stud_arr = sorted(stud_arr, key=lambda k: k.cypher)
        for item in stud_arr:
            file.write(f'{item.surname};{item.cypher};'
                       f'{item.marks[0]};{item.marks[1]};{item.marks[2]}\n')


def main():
    while True:
        print('\nМеню (Введите соответствующий пункт): ')
        print('\t1. Добавить студента')
        print('\t2. Просмотреть всех студентов')
        print('\t3. Просмотреть студентов без оценки "2"')
        print('\t4. Удалить двоечников')
        print('\n\t0. Завершить программу')
        num = int(input('\nНомер задачи: '))
        if num == 1:
            new_student()
        elif num == 2:
            diplay_all()
        elif num == 3:
            diplay_wo_two()
        elif num == 4:
            delete_bad_ones()
        elif num == 0:
            exit()
        else:
            print('Введите номер пункта меню!!!')
            break


if __name__ == "__main__":
    main()
