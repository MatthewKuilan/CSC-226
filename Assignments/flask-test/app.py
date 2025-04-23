from flask import Flask, request

app = Flask(__name__)

@app.route('/submit-get')
def submit_get():
    name = request.args.get('username')
    return f"Hello from GET, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
