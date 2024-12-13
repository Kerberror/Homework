# Задание 1
def task_1():
    n = int(input("Введите число n (до 100): "))
    if n <= 100:
        print([i**3 for i in range(1, n + 1)])
    else:
        print("n должно быть меньше или равно 100.")

# Задание 2
def task_2():
    for i in range(1, 10):
        strochka = [i * j for j in range(1, 10)]
        for j in range(len(strochka)):
            if len(str(strochka[j])) == 1 and j != 8:
                print(f'{strochka[j]}  ', end='')
            elif len(str(strochka[j])) != 1 and j != 8:
                print(f'{strochka[j]} ', end='')
            else:
                print(f'{strochka[j]}', end='\n')

# Задание 2* (умножение в обратном порядке)
def task_2_star():
    for i in range(9, 0, -1):
        strochka = [i * j for j in range(1, 10)]
        for j in range(len(strochka)):
            if len(str(strochka[j])) == 1 and j != 8:
                print(f'{strochka[j]}  ', end='')
            elif len(str(strochka[j])) != 1 and j != 8:
                print(f'{strochka[j]} ', end='')
            else:
                print(f'{strochka[j]}', end='\n')

# Основная программа
def main():
    print("Выберите номер задания (1, 2, 2*):")
    number = input("Введите номер задания: ")

    if number == '1':
        task_1()
    elif number == '2':
        task_2()
    elif number == '2*':
        task_2_star()
    else:
        print("Некорректный номер задания. Пожалуйста, введите 1, 2 или 2*.")
