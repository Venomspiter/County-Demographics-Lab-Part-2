from flask import flask, request, Markup, render_template,flask, Markup
import os
import json
app = Flask(__name__)

with open('county_demographics.json') as demographics_data:
       counties = json.load(demographics_data)

@app.route("/")
def render_main():
    return render_template('home.html', options = get_state_options())

@app.route("/home")
def render_response():
    state = request.args["state"]
    return render_template('home.html', options = get_state_options(),response = your_interesting_demographic_function2(state))
def get_state_options():
    options = ""
    state = ""
    for c in counties
        

def your_interesting_demographic_function(stateName):

if __name__=="__main__":
    app.run(debug=False, port=54321)
