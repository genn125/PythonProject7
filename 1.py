# from pprint import pprint

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
def custom_write(file_name, strings):
    strings_positions = {}
    n = 0
    file = open(file_name, 'w', encoding='utf-8')
    for i in info:

        tell = (file.tell())
        n += 1
        file.write(f'{i}\n')

        strings_positions.update({(n, tell): i})
    return strings_positions
    file.close()

result = custom_write('Текст.txt', info)
for strings_positions in result.items():
    print(strings_positions)


#



