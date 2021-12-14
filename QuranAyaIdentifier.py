import pandas as pd

hash_table = dict()


def update_hash_table(word, sub_table):
    if word not in sub_table:
        inner_sub_table = dict()
        sub_table[word] = inner_sub_table
        return inner_sub_table
    else:
        inner_sub_table = sub_table[word]
        return inner_sub_table


def load_file(file_path='quran-simple-clean.txt'):
    with open(file_path, 'r') as f:
        ayas = [line.strip() for line in f.readlines()]
        return ayas


def process_file(ayas):
    for aya in ayas:
        words = aya.split(' ')
        for i, word in enumerate(words):  # الحمد لله رب العالمين
            if i == 0:
                inner_sub_table = update_hash_table(word, hash_table)
            else:
                inner_sub_table = update_hash_table(word, inner_sub_table)


def output():
    with open('output.txt', 'w') as f:
        f.write(str(hash_table))


def is_ayah(text):
    words = text.strip().split()
    sub_array = hash_table
    for w in words:
        if w in sub_array:
            sub_array = sub_array[w]
        if len(sub_array) == 0:
            return True

    return False

