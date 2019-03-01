
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import psycopg2
import psycopg2.extensions

app = Flask(__name__)

def stream_messages(channel):
    conn = psycopg2.connect(database='mydb', user='postgres',password='postgres',host='172.16.66.244')
    conn.set_isolation_level()