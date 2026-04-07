import argparse
import os
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description='Find logs by text')
    parser.add_argument('path', help='File name or directory')
    parser.add_argument('-t', '--text', help='Word to find')
    return parser.parse_args()


args = parse_args()

file_path = args.path
word_to_find = args.text

if os.path.isdir(file_path):
    files = list(filter(lambda name: name.endswith('.log'), os.listdir(file_path)))
    files.sort()
    files = list(map(lambda name: os.path.join(file_path, name), files))
else:
    files = [file_path]


data = {}

def get_date_from_line(line_content):
    if len(line_content) >= 23:
        date_candidate = line_content[:23]
        try:
            datetime.fromisoformat(date_candidate)
            return date_candidate
        except ValueError:
            pass
    return None


with open(files[0], encoding='utf-8') as log_file:
    print(files[0])
    for i, line in enumerate(log_file.readlines()[0:35]):
        line_date = get_date_from_line(line)
        if line_date:
            date_key = line_date
            data[line_date] = line
        else:
            data[date_key] += line

for key, entry in data.items():
    if word_to_find in entry:
        words = entry.split()
        for i in range(len(words)):
            if word_to_find in words[i]:
                start = max(0, i - 5)
                end = i + 6
                text = ' '.join(words[start:end])
                print(key, text)
                break
