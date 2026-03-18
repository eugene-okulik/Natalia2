import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor(dictionary=True)
add_student = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values_for_student = ('Abdul', 'Rehman')
cursor.execute(add_student, values_for_student)
db.commit()
student_id = cursor.lastrowid

add_book = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values_for_book = [
    ('Forgive1', student_id),
    ('Forgive2', student_id),
    ('Forgive3', student_id)
]
cursor.executemany(add_book, values_for_book)
db.commit()

add_group = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values_for_group = ('New group', '01.12.2026', '01.06.2026')
cursor.execute(add_group, values_for_group)
db.commit()
group_id = cursor.lastrowid

update_students_group = 'UPDATE students SET group_id = %s WHERE id = %s'
values_for_update_group = (group_id, student_id)
cursor.execute(update_students_group, values_for_update_group)
db.commit()

add_subject = 'INSERT INTO subjects (title) VALUES (%s)'
values_for_subject = [
    ('Bio',),
    ('Geo',)
]
cursor.executemany(add_subject, values_for_subject)
db.commit()
subject1_id = cursor.lastrowid
print(subject1_id)
subject2_id = cursor.lastrowid+1
print(subject2_id)

add_lesson = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
values_for_lessons=[
    ('1-1', subject1_id),
    ('1-2', subject1_id),
    ('2-1', subject2_id),
    ('2-2', subject2_id)
]
cursor.executemany(add_lesson, values_for_lessons)
db.commit()
lesson1_id=cursor.lastrowid
print(lesson1_id)
lesson2_id=cursor.lastrowid+1
print(lesson2_id)
lesson3_id=cursor.lastrowid+2
print(lesson3_id)
lesson4_id=cursor.lastrowid+3
print(lesson4_id)

add_marks = 'INSERT INTO marks (value, lesson_id, student_id ) VALUES (%s, %s, %s)'
values_for_marks = [
    (3, lesson1_id, student_id),
    (4, lesson2_id, student_id),
    (5, lesson3_id, student_id),
    (5, lesson4_id, student_id)
]
cursor.executemany(add_marks, values_for_marks)
db.commit()

cursor.execute(f'SELECT value FROM marks WHERE student_id ={student_id}')
marks = cursor.fetchall()
print(f'Marks of student with id = {student_id}')
for mark in marks:
    print(mark['value'])

cursor.execute(f'SELECT title FROM books WHERE taken_by_student_id = {student_id}')
books = cursor.fetchall()
print(f'Taken books by student with id = {student_id}')
for book in books:
    print(book['title'])

all_info = ''' SELECT s.name as 'Student name', s.second_name as 'Student last name', 
g.title as 'Group name', m.value as 'Mark', b.title as 'Book title', l.title as 'Lesson', w.title as 'Subject'
FROM students s
left join books b
on s.id = b.taken_by_student_id
left join `groups` g
on s.group_id = g.id
left join marks m
on s.id = m.student_id
left join lessons l
on m.lesson_id = l.id
left join subjects w
on l.subject_id = w.id
WHERE s.id = %s
'''
cursor.execute(all_info, (student_id,))
data = cursor.fetchall()
for line in data:
    print(line)
db.close()
