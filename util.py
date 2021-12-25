import re
from maha.cleaners.functions import keep_arabic_letters

from QuranAyaIdentifier import AyahIdentifier

timing = re.compile(".* --> .*\n")
empty_or_number = re.compile('\d*\n')


def is_content_line(line):
    return not (empty_or_number.match(line) or timing.match(line))


def keep_letters_only(line):
    return keep_arabic_letters(line)


def process_srt_file(srt):
    ayah_identifier = AyahIdentifier()
    with open(srt, 'r') as f:
        lines = f.readlines()
        sub_table = {}
        ayahs = []
        ayah_words = []
        for line in lines:
            if is_content_line(line):
                line = keep_letters_only(line)
                new_words, sub_table = ayah_identifier.is_ayah(line, sub_table)
                if len(new_words) == 0:
                    ayah_words = []
                ayah_words += new_words
                if len(sub_table) == 0:
                    ayahs.append(ayah_words)
                    ayah_words = []
        return ayahs


# print(process_srt_file("d"))
