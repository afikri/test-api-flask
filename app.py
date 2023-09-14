from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_api():
    response_data = {'message': 'Hello, My API!'}
    return jsonify(response_data), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run()
