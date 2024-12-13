import math

# Задание 1
def task_1():
    r = int(input("Введите радиус: "))
    print("Длина окружности:", round(2 * math.pi * r, 2))
    print("Площадь круга:", round(math.pi * math.pow(r, 2), 2))

# Задание 2
def task_2():
    x = 10
    y = 55
    print("Исходные значения:", x, y)
    x, y = y, x
    print("Поменянные значения:", x, y)

# Задание 3
def task_3():
    L = int(input("Введите длину: "))
    g = 9.81
    print("Период колебаний:", round(2 * math.pi * math.sqrt(float(L) / g), 2))

# Основная программа
def main():
    print("Выберите номер задания (1, 2, 3):")
    number = input("Введите номер задания: ")

    if number == '1':
        task_1()
    elif number == '2':
        task_2()
    elif number == '3':
        task_3()
    else:
        print("Некорректный номер задания. Пожалуйста, введите 1, 2 или 3.")
