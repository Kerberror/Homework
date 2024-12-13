from random import randint, sample

# Задание 5
def task_5():
    m, n = randint(2, 10), randint(2, 10)
    arr = []
    for i in range(m):
        brr = []
        for j in range(n):
            brr.append(randint(-10, 10))
        arr.append(brr)
    
    print(arr)
    
    summi = {}
    for row in arr:
        summi.update({sum(row): row})
    
    print(f'максимальная сумма {max(summi.keys())} у строчки {summi.get(max(summi.keys()))}')
    print(f'минимальная сумма {min(summi.keys())} у строчки {summi.get(min(summi.keys()))}')

# Задание 6
def task_6():
    m, n = randint(2, 10), randint(2, 10)
    arr = []
    for i in range(n):
        brr = sample(range(-30, 30), m)
        arr.append(brr)
    
    print(arr)
    
    for row in arr:
        if row[row.index(min(row))] % 2 == 0:
            row[row.index(min(row))] = 0
        else:
            row[row.index(min(row))] = 1
    
    print(arr)

# Основная программа
def main():
    print("Выберите номер задания (5, 6):")
    number = input("Введите номер задания: ")

    if number == '5':
        task_5()
    elif number == '6':
        task_6()
    else:
        print("Некорректный номер задания. Пожалуйста, введите 5 или 6.")
