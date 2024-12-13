import pandas as pd

# Задание 1
def chickenpox_by_sex():
    df = pd.read_csv('random/NISPUF17.csv')

    got_vac = df[df['P_NUMVRC'] > 0] 
    males = got_vac[got_vac['sex'] == 1]
    male_chickenpox = len(males[males['hd_cpx'] == 2])
    male_ratio = len(males[males['hd_cpx'] == 1]) / male_chickenpox if male_chickenpox > 0 else 0
 
    females = got_vac[got_vac['sex'] == 2]
    female_chickenpox = len(females[females['hd_cpx'] == 2])  
    female_ratio = len(females[females['hd_cpx'] == 1]) / female_chickenpox if female_chickenpox > 0 else 0
    
    ratio_dict = {'male': male_ratio, 'female': female_ratio}

    return ratio_dict

# Основная программа
def main():
    print("Выберите номер задания (1):")
    number = input("Введите номер задания: ")

    if number == '1':
        print(chickenpox_by_sex())
    else:
        print("Некорректный номер задания. Пожалуйста, введите 1.")
