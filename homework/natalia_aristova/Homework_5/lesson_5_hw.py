# Task 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

# Task 2

a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'

print(int(a[(a.index(':')+2):]) + 10)
print(int(b[(b.index(':')+2):]) + 10)
print(int(c[(c.index(':')+2):]) + 10)

# Task 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
