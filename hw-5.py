from math import *

# Задание 1
def task_1():
    def triangle(coords):
        b = list(map(int, [coords[0], coords[1]]))
        c = list(map(int, [coords[0], 0]))
        line1 = round(sqrt(pow(b[0], 2) + pow(b[1], 2)))
        line2 = round(sqrt(pow(c[0], 2) + pow(c[1], 2)))
        print(f'длины векторов {line1} и {line2}')
        angle = ((b[0] * c[0] + b[1] * c[1]) / (line1 * line2))
        print(f'угол относительно оси абцисс {angle}')
        return angle

    points = [input("Введите координаты точки (x y): ").split() for _ in range(3)]
    results = {}
    for point in points:
        results.update({triangle(point): point})
    
    max_angle = max(results.keys())
    print(f'максимальный угол {max_angle} у точки с координатами {results.get(max_angle)}')

# Задание 2
def task_2():
    def palindrom(n):
        new_n = bin(n)[2:]
        if new_n == new_n[::-1]:
            return new_n
        else:
            return ''

    n = int(input("Введите число n: "))
    results = {}
    for i in range(n + 1):
        if palindrom(i) != '':
            results.update({i: palindrom(i)})
    
    print(f'найдено чисел палиндромов {len(results)}, сами числа {results}')

# Основная программа
def main():
    print("Выберите номер задания (1, 2):")
    number = input("Введите номер задания: ")

    if number == '1':
        task_1()
    elif number == '2':
        task_2()
    else:
        print("Некорректный номер задания. Пожалуйста, введите 1 или 2.")
