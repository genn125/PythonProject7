



class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words (self):
        all_words = {}
        punctuation =  [',', '.', '=', '!', '?', ';', ':', '  ']
        l=''
        with open(self.file_names, 'r', encoding='utf-8') as file:
            for i in file:
                i = i.lower()
                for j in i:
                    if j in punctuation:
                        i = i.replace(j, '')
                l = l + i
            all_words.update({self.file_names: l.split(),})
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
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего