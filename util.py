import re

# pattern = re.compile(".* --> .*")
from QuranAyaIdentifier import AyahIdentifier

timing = re.compile(".* --> .*\n")
empty_or_number = re.compile('\d*\n')


def is_content_Line(line):
    if empty_or_number.match(line) or timing.match(line):
        return False
    else:
        return True


def process_srt_file(srt):
    ayah_identifier = AyahIdentifier()
    with open(srt, 'r') as f:
        lines = f.readlines()
        sub_table = {}
        ayah_words = []
        for line in lines:
            if is_content_Line(line):
                new_words, sub_table = ayah_identifier.is_ayah(line, sub_table)
                ayah_words += new_words
                print(ayah_words)


process_srt_file('النسوية فكرة غير بريئة.srt')
