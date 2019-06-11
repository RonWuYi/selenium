from flask import Flask
from flaskext.xmlrpc import XMLRPCHandler, Fault

app = Flask(__name__)

handler = XMLRPCHandler('api')
handler.connect(app, '/')


@handler.register()
def hello(name="world"):
    if not name:
        raise Fault("unknown_recipient", "I need someone to greet!")
    return "Hello, %s!" % name


app.run()
