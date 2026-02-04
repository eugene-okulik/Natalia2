a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'
d = 'результат: 2'


def my_function(stroka):
    print(int(stroka[(stroka.index(':') + 2):]) + 10)


my_function(a)
my_function(b)
my_function(c)
my_function(d)
