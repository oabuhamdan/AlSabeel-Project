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
        complete_ayahs = []
        ayah_words = []
        for line in lines:
            if is_content_line(line):
                line = keep_letters_only(line)
                new_complete_ayahs, sub_table = ayah_identifier.is_ayah(ayah_words, line, sub_table)
                complete_ayahs += new_complete_ayahs
        return complete_ayahs


def list_ayahs(prefix):
    ayah_identifier = AyahIdentifier()
    return ayah_identifier.list_ayahs(prefix)

# print(process_srt_file('d'))
