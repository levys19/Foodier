from flask import Flask, redirect, render_template, request, url_for
from data import DataFilter

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/choicesMade', methods=['POST'])
def choicesMade():
    # Getting integer value from the user
    zipCode = request.form['text']
    # Calling the html for the choices
    cuisine = request.form['cuisine']
    cuisine = cuisine.upper()
    priceRange = request.form['priceRange']
    filterArea = DataFilter()
    # Getting Parameters for the area
    parameters = filterArea.getLocation(zipCode, priceRange)
    location = filterArea.get_results(parameters)
    # Calling the html holding all of the final choices
    return render_template('index.html', location = location)


if __name__ == '__main__':
    port = 5000
    app.debug = True
    app.run(host='0.0.0.0', port=port)
