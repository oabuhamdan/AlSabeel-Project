import time

from flask_cors import cross_origin, CORS
from QuranAyaIdentifier import AyahIdentifier

from flask import Flask, request, render_template

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def my_form():
    return render_template('ayah_identifier.html')


@app.route('/', methods=['POST'])
@cross_origin()
def my_form_post():
    t1 = time.time()
    ayah_Identifier = AyahIdentifier()
    ayah = request.form['ayah']
    res = f'"{ayah}" is {" an Ayah" if ayah_Identifier.is_ayah(ayah) else "not an Ayah":}'
    dur = f"Took {time.time() - t1} to load the file, build the hashtable, and analyze the ayah(s)"

    return render_template('ayah_identifier.html', data={'res': res, 'dur': dur})


if __name__ == '__main__':
    app.run()
