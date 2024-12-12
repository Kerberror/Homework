import re

# Задание 1
def task_1():
    text = input("Введите текст для проверки: ")
    if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text):
        print('private')
    elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', text):
        print('taxi')
    else:
        print('Another words')

# Задание 2
def task_2():
    text = input("Введите текст для подсчета слов: ")
    print(len(re.findall(r'\b\w[\w-]*\b', text)))

# Задание 3
def task_3():
    text = input("Введите текст для замены времени: ")
    for i in re.findall(r'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)', text):
        text = text.replace(i, '(TBD)')
    print(text)
    
    ext = input("Введите текст для поиска слов: ")
    print(re.findall(r'(?:[АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ]{2,}[ ]*)+', ext))

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

if __name__ == "__main__":
    main()
