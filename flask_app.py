from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/map", methods=['GET', 'POST'])
def map():
    if request.method == 'POST':
        if request.form.get('submit_button'):
            return render_template('mars.html')
        else:
            pass
    elif request.method == 'GET':
        return 'bye'


@app.route('/photos', methods=['GET', 'POST'])
def photos():
    if request.method == 'POST':
        if request.form.get('submit_button2'):
            return 'Photos will appear here soon!'


@app.route("/statistics", methods=['GET', 'POST'])
def statistics():
    if request.method == 'POST':
        if request.form.get('submit_button3'):
            return 'Statistics'


if __name__ == '__main__':
    app.run(debug=True)