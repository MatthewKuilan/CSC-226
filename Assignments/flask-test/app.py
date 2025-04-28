from flask import Flask, request, render_template, redirect

app = Flask(__name__)
filepath = "C:\\Users\\matthew.kuilan\\Documents\\Names.txt"


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/submit', methods=["POST"])
def submit():
    # TODO: Get form data from request.form
    # TODO: Save it to a file (append mode - make sure you are appending to the file, not overwriting the whole thing)
    name = request.form['name']
    message = request.form['message']
    with open(filepath, 'a') as w:
        w.write(name + ': ' + message + '\n')

    return redirect("/messages")


@app.route('/messages', methods=["GET"])
def messages():
    # TODO: Read file content and return as plain text or HTML
    with open(filepath, 'r') as r:
        string = r.read()
    return f"<pre>{string}</pre>"


if __name__ == '__main__':
    app.run(debug=True)
