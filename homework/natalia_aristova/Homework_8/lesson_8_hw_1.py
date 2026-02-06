import random


salary = int(input('Введите размер вашей зарплаты в долларах: '))
bonus = bool(random.randint(0, 1))

if bonus:
    salary_with_bonus = int(salary + salary * random.random())
    print(f'{salary}, {bonus} - ${salary_with_bonus}')
else:
    print(f'{salary}, {bonus} - ${salary}')
