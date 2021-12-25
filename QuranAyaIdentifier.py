import json
import os.path
import re


class AyahIdentifier:
    hash_table = dict()
    only_arab_chars = '[^ء-ي\s]*'

    def __init__(self):
        if not os.path.isfile('output.txt'):
            ayas = self.load_file()
            self.process_file(ayas)
            self.output()
        else:
            self.read_hashtable()

    def load_file(self, file_path='quran-simple-clean.txt'):
        with open(file_path, 'r') as f:
            ayas = [line.strip() for line in f.readlines()]
            return ayas

    def update_hash_table(self, word, sub_table):
        if word not in sub_table:
            inner_sub_table = dict()
            sub_table[word] = inner_sub_table
            return inner_sub_table
        else:
            inner_sub_table = sub_table[word]
            return inner_sub_table

    def process_file(self, ayas):
        for aya in ayas:
            words = aya.split(' ')
            for i, word in enumerate(words):
                if i == 0:
                    inner_sub_table = self.update_hash_table(word, self.hash_table)
                else:
                    inner_sub_table = self.update_hash_table(word, inner_sub_table)

    def read_hashtable(self):
        with open('output.txt', 'r') as f:
            str = f.read().replace("'", '"')
            self.hash_table = json.loads(str)

    def output(self):
        with open('output.txt', 'w') as f:
            f.write(str(self.hash_table))

    def is_ayah(self, text, sub_table):
        words = [re.sub(self.only_arab_chars, '', x) for x in text.strip().split()]
        sub_table = self.hash_table if len(sub_table) == 0 else sub_table
        ayah_words = []
        for w in words:
            if w in sub_table:
                ayah_words.append(w)
                sub_table = sub_table[w]
            elif len(sub_table) == 0:
                return ayah_words, sub_table
            else:
                if len(ayah_words) > 0:
                    words.insert(0, w)
                ayah_words.clear()
                sub_table = self.hash_table

        return ayah_words if len(ayah_words) > 1 else [], sub_table
