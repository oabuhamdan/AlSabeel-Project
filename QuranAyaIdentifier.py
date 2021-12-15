import json
import os.path


class AyahIdentifier:
    hash_table = dict()

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

    def is_ayah(self, text):
        words = text.strip().split()
        sub_array = self.hash_table
        for w in words:
            if w in sub_array:
                sub_array = sub_array[w]
            if len(sub_array) == 0:
                return True

        return False
