from flask import Flask, request, Markup, render_template, Markup
import os
import json
app = Flask(__name__)

@app.route("/home")
def render_response():
    state = request.args["states"]
    return render_template('home.html',options = get_state_options(),response = your_interesting_demographic_function2(state))
def get_state_options():
    options = ""
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    state = []
    for c in counties:
        if not c["State"] in state:
              state.append(c["State"])
    for s in state:
       options += Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options
def your_interesting_demographic_function(stateName):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for c in counties:
        if c["state"] in state
@app.route("/")
def render_main():
    return render_template('home.html',options = get_state_options())
if __name__=="__main__":
    app.run(debug=False, port=54321)
