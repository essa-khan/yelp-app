# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import yelp

app = Flask(__name__)

@app.route("/")
def index():
    #Return a page
    return render_template("index.html")

@app.route("/submit")
def submit():
    #Submission page
    user_submitted_term = request.values.get("term")
    user_submitted_location = request.values.get("location")
    
    results = yelp.search_businesses(user_submitted_term, user_submitted_location)
    return results
        
app.config['TEMPLATES_AUTO_RELOAD'] = True

my_port = 5000

app.run(host="0.0.0.0", port=my_port, debug=True)

