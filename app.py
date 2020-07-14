# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #Return a page
    return render_template("index.html")
        
my_port = 5000

app.run(host="0.0.0.0", port=my_port, debug=True)
