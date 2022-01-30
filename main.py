import os
import time

from flask import Flask, request, render_template
from flask_cors import cross_origin, CORS

import util

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def identify():
    return render_template('ayah_identifier.html')


@app.route('/list')
def list_ayahs():
    return render_template('ayah_list.html', data={'ayahs': ''})


@app.route('/', methods=['POST'])
@cross_origin()
def my_form_post():
    t1 = time.time()
    ayahs = []
    if request.files:
        srt_file = request.files["srt_file"]
        srt_file.save(os.path.join('', srt_file.filename))
        ayahs = util.process_srt_file(srt_file.filename)
        os.remove(srt_file.filename)
    dur = f"Took {time.time() - t1} to load the file, build the hashtable, and analyze the ayah(s)"

    return render_template('ayah_identifier.html', data={'ayahs': ayahs, 'dur': dur})


@app.route('/list', methods=['POST'])
@cross_origin()
def list_ayahs_post():
    ayah = request.form['ayah']
    ayahs = util.list_ayahs(ayah)

    return render_template('ayah_list.html', data={'ayahs': ayahs})
