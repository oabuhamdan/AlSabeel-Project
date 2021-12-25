import os
import time

from flask_cors import cross_origin, CORS

import util

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
    ayahs = []
    if request.files:
        srt_file = request.files["srt_file"]
        srt_file.save(os.path.join('uploads/', srt_file.filename))
        ayahs = util.process_srt_file('uploads/' + srt_file.filename)
        os.remove('uploads/' + srt_file.filename)
    dur = f"Took {time.time() - t1} to load the file, build the hashtable, and analyze the ayah(s)"

    return render_template('ayah_identifier.html', data={'ayahs': ayahs, 'dur': dur})
