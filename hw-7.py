import os

# Задание 1
def read_last(lines, file):
    with open(file, 'r', encoding='utf-8') as f:
        lines_c = f.readlines()
        if len(lines_c) >= lines and lines > 0:
            for line in lines_c[-lines:]:
                print(line.strip())

# Задание 2
def print_docs(directory):
    use_files = os.walk(directory)
    for folder in use_files:
        print(f'в папке {folder[0]} находятся \n данные папки {", ".join([infolder for infolder in folder[1]])} \n данные файлы {", ".join([file for file in folder[2]])} \n')

# Задание 3
def longest_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines_c = f.readlines()
        longest_set = set()
        for line in lines_c:
            words = line.split()
            longest_set.add(max(words, key=len))
        if len(longest_set) > 0:
            return max(longest_set, key=len)

# Задание 4
def redactor():
    filename = input('Имя файла: ') + '.txt'
    with open(filename, 'w+', encoding='utf-8') as file:
        text = 'Содержание файла'
        print(text)
        while True:
            text = input()
            if text == '':
                break
            file.write(f'{text}\n')

# Основная программа
def main():
    print("Выберите номер задания (1, 2, 3, 4):")
    number = input("Введите номер задания: ")

    if number == '1':
        n = int(input("Введите количество строк для чтения: "))
        read_last(n, r'C:/Users/taras/repo/random/article.txt')
    elif number == '2':
        print_docs('C:/Users/taras/repo/abstract')
    elif number == '3':
        result = longest_words('C:/Users/taras/repo/random/article.txt')
        if result:
            print(f'Самое длинное слово: {result}')
    elif number == '4':
        redactor()
    else:
        print("Некорректный номер задания. Пожалуйста, введите 1, 2, 3 или 4.")

if __name__ == "__main__":
    main()
