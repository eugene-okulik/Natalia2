text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,'
        ' dignissim vitae libero')
list_of_words = text.split()
updated_text = []

for word in list_of_words:
    if word.endswith(','):
        updated_text.append(word.replace(',', 'ing,'))
    elif word.endswith('.'):
        updated_text.append(word.replace('.', 'ing,'))
    else:
        updated_text.append(word + 'ing')

print(' '.join(updated_text))
