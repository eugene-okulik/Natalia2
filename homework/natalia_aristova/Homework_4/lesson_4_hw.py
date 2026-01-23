my_dict={}
my_dict['tuple'] = (1, 3, 6, 7, None, 'text')
my_dict['list'] = [1, 3, 6, 7, None, 'text']
my_dict['dict'] = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31}
my_dict['set'] = {1, 3, 6, 7, None, 'text'}

print(my_dict['tuple'][-1])

my_dict['list'].append('new_element')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = (1.1, 2.2, 3.3)
my_dict['dict'].pop('jan')

my_dict['set'].add(8)
my_dict['set'].discard(None)

print(my_dict)
