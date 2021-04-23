from flask import Flask, jsonify
from libgen_api import LibgenSearch

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to libgen api database"

@app.route('/<path:data>')
def find_book(data):
    print('data')

    return jsonify(LibgenSearch().search_title(list(data)))

if __name__ == '__main__':
    app.run(debug=True) 
