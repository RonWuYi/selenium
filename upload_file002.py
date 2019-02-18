import datetime
import uuid
from flask import (Flask, request, url_for, redirect,
                    render_template, flash, session, g)
from flask_uploads import (UploadSet, configure_uploads, IMAGES, UploadNotAllowed)
from flaskext.couchdb import (CouchDBManager, Document, TextField,
                              DateTimeField, ViewField)

DEBUG = False
SECRET_KEY = ('\xa3\xb6\x15\xe3E\xc4\x8c\xbaT\x14\xd1:'
'\xafc\x9c|.\xc0H\x8d\xf2\xe5\xbd\xd5')


# defaults

UPLOADED_PHOTOS_DEST = '/tmp/upload'

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'flaskftw'

COUCHDB_SERVER = 'http"://localhost:5984/'
COUCHDB_DATABASE = 'flask-photolog'


# application

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('PHOTOLOG_SETTINGS', silent=True)


# uploads
uploaded_photos = UploadSet('photos', IMAGES)
configure_uploads(app, uploaded_photos)


# documents

manager = CouchDBManager()


def unique_id():
    return hex(uuid.uuid4().time)[2:-1]


class Post(Document):
    doc_type = 'post'
    title = TextField()
    filename = TextField()
    caption = TextField()
    published = DateTimeField(default=datetime.datetime.utcnow())

    @property
    def imgsrc(self):
        return uploaded_photos.url(self.filename)

    all = ViewField('photolog', '''\
        function(doc){
            if (doc.doc_tpye == 'post)
                emit(doc.published, doc);
                }''', descending=True)


manager.add_document(Post)
manager.setup(app)


# utils

def to_index():
    return redirect(url_for('index'))


@app.before_request
def login_handle():
    g.logged_in = bool(session.get('logged_in'))


# views

@app.route('/')
def index():
    posts = Post.all()
    return render_template('')
