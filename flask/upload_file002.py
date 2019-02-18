import datetime
import uuid
from flask import (Flask, request, url_for, redirect,
                    render_template, flash, session, g)
from flask_uploads import (UploadSet, configure_uploads, IMAGES, UploadNotAllowed)
from flaskext.couchdb import (CouchDBManager, Document)