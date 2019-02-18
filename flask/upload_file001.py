from flask import send_from_directory, Flask


UPLOAD_FOLDER = '/home/hdc/PycharmProjects/selenium/uploadfiles'
ALLOWED_EXTENSIONS = set(['txt', 'jpg', 'jpeg', 'png'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/uploads/<filename>')
def upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
