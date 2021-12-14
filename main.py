import time
from QuranAyaIdentifier import *

t1 = time.time()
ayas = load_file()
process_file(ayas)
for ayah in ['إلا الذين آمنوا وعملوا الصالحات فلهم أجر غير ممنون', 'هل أتى على الإنسان حين من الدهر']:
    print(f'Ayah "{ayah}" is {" an Ayah" if is_ayah(ayah) else "not an Ayah":}')

print(f"Took {time.time() - t1} to load the file, build the hashtable, and analyze the ayah(s)")
output()
