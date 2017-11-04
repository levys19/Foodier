from flask import Flask, redirect, render_template, request, url_for
from option import Option
import json
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def choices_made():
    # Getting integer value from the user
    zip = int(request.form['text'])
    # Creating Option() for the parameters
    filterArea = Option()
    #Getting Parameters for the area
    parameters = filterArea.meal_search(zip,None)
    location = filterArea.get_results(parameters)
    return render_template('index.html', location = location)



if __name__ == '__main__':
    port = 5000
    app.debug = True
    app.run(host='0.0.0.0', port=port)
