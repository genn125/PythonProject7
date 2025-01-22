# 7.3 Оператор "with"
# Задача "Найдёт везде":
"""
Monday’s Child

Monday’s child is fair of face
Tuesday’s child is full of grace
Wednesday’s child is full of woe
Thursday’s child has far to go,
Friday’s child is loving and giving,
Saturday’s child works hard for a living,
And the child that is born on the Sabbath day
Is bonny and blithe, and good and gay.

Mother Goose
"""

class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words (self):
        all_words = {}
        punctuation =  [',', '.', '=', '!', '?', ';', ':', '  ']
        a =''
        with open(self.file_names, 'r', encoding='utf-8') as file:
            for i in file:
                i = i.lower()
                for j in i:
                    if j in punctuation:
                        i = i.replace(j, '')
                a = a + i
            all_words.update({self.file_names: a.split()})
        return all_words


    def find(self, txt):
        dist = {}
        world = self.get_all_words()[self.file_names]
        for i in range(len(world)):
            if txt.lower() == world[i]:
                dist.update({self.file_names: i + 1})
                return dist


    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count

        return counters

finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

print(finder2.get_all_words())
print(finder2.find('is'))
print(finder2.count('iS'))