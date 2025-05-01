from flask import Flask, request, render_template, redirect

app = Flask(__name__)
filepath = "C:\\Users\\matthew.kuilan\\Documents\\Names.txt"


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/submit', methods=["POST"])
def submit():
    name = request.form['name']
    email = request.form['email']
    with open(filepath, 'a') as w:
        w.write(name + ': ' + email + '\n')

    return redirect("/messages")


@app.route('/messages', methods=["GET"])
def messages():
    with open(filepath, 'r') as r:
        string = r.read()
    return f"<pre>{string}</pre>"


if __name__ == '__main__':
    app.run(debug=True)