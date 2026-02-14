def dec(func):

    def wrapper(first, second):
        if first < 0 or second < 0:
            func(first, second, '*')
        elif first == second:
            func(first, second, '+')
        elif first > second:
            func(first, second, '-')
        elif first < second:
            func(first, second, '/')
    return wrapper


@dec
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

calc(a, b)
