# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
        
my_port = 5000

app.run(host="0.0.0.0", port=my_port, debug=True)
