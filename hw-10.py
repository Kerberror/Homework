import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Задание 1
def task_1():
    series1 = pd.Series([4.313, 4.338, 4.358, 4.378, 4.4, 4.425, 4.447, 4.468])
    print(series1)
    series2 = pd.Series(np.arange(0, 20, 2))
    print(series2)
    series3 = pd.Series({'Семейство': 1, 'Шмуклеров': 3, 'производило': 5, 'гвозди': 7})
    print(series3)

# Задание 2
def task_2():
    series1 = pd.Series(np.arange(0, 8, 2))
    series2 = pd.Series(np.arange(2, 10, 1))
    print(series1, series2)
    union_set = set.union(set(series1), set(series2))
    union_series = pd.Series(list(union_set))
    print(union_series)

# Задание 3
def task_3():
    gender_series = pd.Series({
        0: 'female', 1: 'male', 2: 'male', 3: 'female', 4: 'female', 
        5: 'male', 6: 'male', 7: 'male', 8: 'male', 9: 'female', 
        10: 'female', 11: 'female', 12: 'female', 13: 'female', 
        14: 'male', 15: 'male', 16: 'male', 17: 'male', 
        18: 'male', 19: 'female', 20: 'female', 
        21: 'female', 22: 'male', 23: 'male', 
        24: 'male', 25: 'male', 26: 'female', 
        27: 'female', 28: 'male', 
        29: 'female', 30: 'male', 
        31: 'female', 32: 'female',
        33: 'male', 
        34: 'female'
    })

    x = gender_series.value_counts().index
    y = gender_series.value_counts().values
    plt.bar(x, y, color=['pink', 'blue'])
    plt.xlabel('количество учеников') # для оси x
    plt.ylabel('пол учеников') # для оси y
    plt.title('соотношение студентов')
    plt.show()

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
        print("Некорректный номер задания. Пожалуйста, введите номер от 1 до 3.")

if __name__ == "__main__":
    main()
