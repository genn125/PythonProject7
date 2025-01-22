# 7.3 Оператор "with"
# Задача "Найдёт везде":



class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words (self):
        all_words = {}
        punctuation =  [',', '.', '=', '!', '?', ';', ':', '  ']
        with open(self.file_names, encoding='utf-8') as file:
            for i in file:
                i = i.lower()
                for j in i:
                    if j in punctuation:
                        i = i.replace(j, '')   # Избавление от пунктуации
                l = l + i
            all_words.update({self.file_names: l.split()})    # split - Разбитие строки .....


        return all_words
 info - [It's a text for task Найти везде,

Используйте его для самопроверки.

Успехов в решении задачи!

text text text]
finder2 = WordsFinder('test_file.txt', info)