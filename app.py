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
    
    return render_template("display_results.html", establishments=results, term=user_submitted_term, location=user_submitted_location)
        
app.config['TEMPLATES_AUTO_RELOAD'] = True

my_port = 5000

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=my_port, debug=True)

