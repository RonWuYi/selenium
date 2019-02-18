import os
from flask import Flask, flash, request, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = ''