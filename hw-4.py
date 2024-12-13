import re

# Задание 1
def task_1():
    text = input("Введите текст: ")
    modified_text = text.replace('н', '!')
    max_n_length = len(max(re.findall(r'н+', text), key=len, default=''))
    print(f'новая строчка: {modified_text}, кол-во символов: {max_n_length}')

# Задание 2
def task_2():
    text = input("Введите текст: ")
    found_patterns = re.findall(r'\((.+?)\)', text)
    print(found_patterns)

# Задание 2* (использование метода find)
def task_2_star():
    text = input("Введите текст: ")
    start_index = text.find('(') + 1
    end_index = text.find(')')
    if start_index > 0 and end_index > start_index:
        print(text[start_index:end_index])
    else:
        print("Скобки не найдены или пустые.")

# Задание 3
def task_3():
    text = input("Введите текст: ").lower()
    found_words = re.findall(r'\bа\w+я\b', text)
    print(found_words)

# Основная программа
def main():
    print("Выберите номер задания (1, 2, 2*, 3):")
    number = input("Введите номер задания: ")

    if number == '1':
        task_1()
    elif number == '2':
        task_2()
    elif number == '2*':
        task_2_star()
    elif number == '3':
        task_3()
    else:
        print("Некорректный номер задания. Пожалуйста, введите 1, 2, 2* или 3.")
