class Book:
    material = 'paper'
    text = True

    def __init__(self, title, author, page_amount, ISBN, reserved):
        self.title = title
        self.author = author
        self.page_amount = page_amount
        self.ISBN = ISBN
        self.reserved = reserved

    def info(self):
        if self.reserved:
            print(f'Tile: {self.title}, Author: {self.author}, pages: {self.page_amount}, material: {self.material},'
                  f' reserved')
        else:
            print(f'Tile: {self.title}, Author: {self.author}, pages: {self.page_amount}, material: {self.material}')


class Textbook(Book):

    def __init__(self, title, author, page_amount, ISBN, reserved, subject, grade, tasks):
        super().__init__(title, author, page_amount, ISBN, reserved)
        self.subject = subject
        self.grade = grade
        self.tasks = tasks

    def info_textbook(self):
        if self.reserved:
            print(f'Tile: {self.title}, Author: {self.author}, pages: {self.page_amount}, subject: {self.subject},'
                  f' class; {self.grade}, reserved')
        else:
            print(f'Tile: {self.title}, Author: {self.author}, pages: {self.page_amount}, subject: {self.subject}, '
                  f'class; {self.grade}')


first_book = Book('Idiot', 'Dostoevsky', 378, 123, False)
second_book = Book('War and Peace', 'Tolstoy', 1378, 1234, False)
third_book = Book('Hello', 'Ivanov', 245, 223, False)
fourth_book = Book('Buy', 'Petrov', 68, 334, False)
fifth_book = Book('Planet', 'Sidorov', 987, 673, False)

first_book.reserved = True

first_book.info()
second_book.info()
third_book.info()
fourth_book.info()
fifth_book.info()

first_textbook = Textbook('Algebra', 'Peterson', 378, 54321, False,
                          'algebra', 7, True)
second_textbook = Textbook('English', 'Smirnova', 278, 3334, False,
                           'english', 10, True)
third_textbook = Textbook('Geography', 'Shikov', 145, 11111223, False,
                          'geography', 8, True)

first_textbook.reserved = True

first_textbook.info_textbook()
second_textbook.info_textbook()
third_textbook.info_textbook()
