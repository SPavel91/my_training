class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding= 'utf-8') as file:
                text = file.read().lower()
                punctuation_chars = [',', '.', '!', '?', ';', ':', ' - ', '\n']
                for char in punctuation_chars:
                    text = text.replace(char, ' ')
                    text.split()
                all_words[self.file_names[0]] = text.split()
        return all_words

    def find(self, word):
        find_list = self.get_all_words()
        word_low = word.lower()
        for file_name, words in find_list.items():
            for index, w in enumerate(words):
                if w == word_low:
                    return {self.file_names[0]: index + 1}

    def count(self, word):
        find_list = self.get_all_words()
        word_low = word.lower()
        count = 0
        for file_name, words in find_list.items():
            count += words.count(word_low)
        return {file_name: count for file_name in find_list}


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова

print(finder2.find('TEXT'))  # 3 слово по счёту

print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
