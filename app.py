from flask import Flask, render_template, request
import image_recog
import time
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload_file', methods=['get', 'post'])
def upload_file():
    try:
        file = request.files['file']
        path = os.getcwd() + '\\images\\'
        filename = str(int(time.time()*1000)) + '_' + file.filename
        file.save(path + filename)

        result = image_recog.image_recog(path + filename)

        return f'<script>window.alert("{result}");window.history.back();</script>'
    except:
        return '<script>window.alert("error");window.history.back();</script>'



if __name__ == '__main__':
    app.run()
