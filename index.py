from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def choices_made():
    # Zip = request.form['zip']
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = 5000
    app.debug = True
    app.run(host='0.0.0.0', port=port)

