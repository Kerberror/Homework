import pandas as pd
import matplotlib.pyplot as plt

# Задание 2
def task_2():
    df = pd.read_csv('random/Mall_Customers.csv')
    female_customers = df[df['Genre'] == 'Female']
    w_income = sum(female_customers['Annual Income (k$)']) / len(female_customers)
    print(w_income)

# Задание 3
def task_3():
    df = pd.read_csv('random/Mall_Customers.csv')

    female_customers = df[df['Genre'] == 'Female']
    w_max = female_customers['CustomerID'].where(female_customers['Annual Income (k$)'] == max(female_customers['Annual Income (k$)'])).dropna()
    print(w_max.index)

    male_customers = df[df['Genre'] == 'Male']
    m_max = male_customers['CustomerID'].where(male_customers['Annual Income (k$)'] == max(male_customers['Annual Income (k$)'])).dropna()
    print(m_max.index)

# Задание 4
def task_4():
    df = pd.read_csv('random/Mall_Customers.csv')

    male_customers = df[df['Genre'] == 'Male']
    data = male_customers.groupby('Age')['Annual Income (k$)'].mean()
    plt.plot(data)
    plt.xlabel('Возраст')  # для оси x
    plt.ylabel('Средний доход (к$)')  # для оси y
    plt.title('Средний доход по возрасту мужчин')
    plt.show()

# Задание 5
def task_5():
    fig, ax = plt.subplots(figsize=(10, 6))
    df = pd.read_csv('random/Mall_Customers.csv')

    male_customers = df[df['Genre'] == 'Male']
    female_customers = df[df['Genre'] == 'Female']
    
    data_m = male_customers.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()
    data_w = female_customers.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()

    data_m.plot.bar(color='blue', label='Мужчины')
    data_w.plot.bar(color='pink', label='Женщины')
    
    plt.xlabel('Годовой доход (к$)')
    plt.ylabel('Средний балл расходов (1-100)')
    plt.title('Сравнение расходов мужчин и женщин по доходу')
    plt.legend()
    plt.show()

# Основная программа
def main():
    print("Выберите номер задания (2, 3, 4, 5):")
    number = input("Введите номер задания: ")

    if number == '2':
        task_2()
    elif number == '3':
        task_3()
    elif number == '4':
        task_4()
    elif number == '5':
        task_5()
    else:
        print("Некорректный номер задания. Пожалуйста, введите номер от 2 до 5.")
