import sys


def fibo(limit = 10):
    fn_2 = 0
    fn_1 = 1
    fn = 0
    count = 0

    while count < limit:
        yield fn
        count += 1
        if count == 1:
            fn += 1
        else:
            fn = fn_2 + fn_1
            fn_2 = fn_1
            fn_1 = fn


sys.set_int_max_str_digits(100000)
count = 0
for number in fibo(100001):
    if count == 5:
        print(f'Пятое число - {number}')
    elif count == 200:
        print(f'Двухсотое число - {number}')
    elif count == 1000:
        print(f'Тысячное число - {number}')
    elif count == 100000:
        print(f'Стотысячное число - {number}')

    count += 1
