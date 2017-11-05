from flask import Flask, redirect, render_template, request, url_for
from data import DataFilter

app = Flask(__name__)
restaurantLinks = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/choices', methods=['POST'])
def choices():
    # Getting integer value from the user
    zipCode = request.form['zipcode']
    # Calling the html for the choices
    price = request.form['price']
    filterArea = DataFilter()
    # Getting Parameters for the area
    parameters = filterArea.getLocation(zipCode, price)
    location = filterArea.get_results(parameters)
    print(type(location))
    # Calling the html holding all of the final choices
    return render_template('choices.html', restauraunts=location)


@app.route('/', methods=['GET'])
def imageSelection():
    choice = int(request.form['choice'])
    if choice != 0:
        "hello"
    else:
        "remove the restaurant"




if __name__ == '__main__':
    port = 5000
    app.debug = True
    app.run(host='0.0.0.0', port=port)
