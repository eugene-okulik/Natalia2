number = 5

while True:
    user_input = int(input('Введите задуманное число: '))
    if user_input == number:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова.')
