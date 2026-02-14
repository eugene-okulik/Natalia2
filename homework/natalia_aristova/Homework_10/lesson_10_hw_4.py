PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_list = PRICE_LIST.split()
items = [x for x in my_list if my_list.index(x) % 2 == 0]
values = [int(x[:-1]) for x in my_list if my_list.index(x) % 2 != 0]
final_dict = dict(zip(items, values))
print(final_dict)
