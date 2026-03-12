import os
import datetime


lesson_13_hw_path = os.path.dirname((__file__))
homework_folder_path = os.path.dirname(os.path.dirname((lesson_13_hw_path)))
eugene_okulik_folder = os.path.join(homework_folder_path, 'eugene_okulik')
data_file_path = os.path.join(eugene_okulik_folder, 'hw_13', 'data.txt')
print(data_file_path)

with open(data_file_path, 'r', encoding='utf-8') as data_file:
    for line in data_file.readlines():
        date = datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
        if 'распечатать эту дату, но на неделю позже' in line:
            print(f'{date} через неделю будет {date + datetime.timedelta(days=7)}')
        elif 'распечатать какой это будет день недели' in line:
            print(f"{date} - это {date.strftime('%A')}")
        elif 'распечатать сколько дней назад была эта дата' in line:
            print(f'{(datetime.datetime.now() - date).days} дней назад было {date}')

