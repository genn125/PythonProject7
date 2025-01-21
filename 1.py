# from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):      # Номер строки
            tell = file.tell()                             # Номер байта
            file.write(string + '\n')
            strings_positions[(i, tell)] = string
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('Текст.txt', info)
for elem in result.items():
    print(elem)