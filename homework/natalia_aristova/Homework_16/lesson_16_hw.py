import dotenv
import mysql.connector as mysql
import os
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

lesson_16_hw_path = os.path.dirname((__file__))
homework_folder_path = os.path.dirname(os.path.dirname((lesson_16_hw_path)))
eugene_okulik_folder = os.path.join(homework_folder_path, 'eugene_okulik')
hw_data_folder = os.path.join(eugene_okulik_folder, 'Lesson_16')
data_file_path = os.path.join(hw_data_folder, 'hw_data', 'data.csv')
print(data_file_path)

all_info = '''SELECT s.name, s.second_name, g.title as 'group_title', b.title as 'book_title',
w.title as 'subject_title', l.title as 'lesson_title',  m.value as 'mark_value'
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
'''

cursor.execute(all_info)
data_db = cursor.fetchall()
db.close()

with open(data_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

missed_data = []
for i in data:
    if i not in data_db:
        missed_data.append(i)

print(missed_data)
