from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/submit-get/')
def submit_get():
    name = request.args.get('username')
    return f"Hello from GET, {name}!"


@app.route('/submit', methods=["POST"])
def submit():
    # TODO: Get form data from request.form
    # TODO: Save it to a file (append mode - make sure you are appending to the file, not overwriting the whole thing)
    name = None
    u_input = request.form['name']
    filepath = "C:\\Users\\matthew.kuilan\\Documents\\Names.txt"
    with open(filepath, 'a') as w:
        w.write(u_input + '\n')

    return redirect("/")


@app.route('/messages', methods=["GET"])
def messages():
    return None


if __name__ == '__main__':
    app.run(debug=True)
