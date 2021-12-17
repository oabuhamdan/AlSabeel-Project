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
    ayah_Identifier = AyahIdentifier()
    with open(srt, 'r') as f:
        lines = f.readlines()
        ayah = []
        for line in lines:
            if is_content_Line(line):
                ayah.append(ayah_Identifier.is_ayah(line))
                print(ayah)


process_srt_file('النسوية فكرة غير بريئة.srt')
