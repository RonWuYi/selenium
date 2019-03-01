import os

class Config(object):
    UPLOAD_FOLDER = '/tmp/uploadfiles'
    # ALLOWED_EXTENSIONS = set(['txt', 'jpg', 'jpeg', 'png'])
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
    SECRET_KEY = 'dev'