from flask import Flask, jsonify
from libgen_api import LibgenSearch

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "welcome to libgen api database"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404



@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an name was provided as part of the URL.
    # If name is provided, assign it to a variable.
    # If no name is provided, display an error in the browser.
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No book name field provided. Please specify an book name."

    # Create an empty list for our results
    
#     results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    s = LibgenSearch()
    results = s.search_title(name)
    
#     for book in books:
#         if book['id'] == id:
#             results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
