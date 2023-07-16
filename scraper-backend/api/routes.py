from flask import request, jsonify
from my_project.scraper.scraper import my_scrape_function

def my_route_function():
    url = request.json.get('url')
    result = my_scrape_function(url)
    # You might want to parse the result into JSON format, depends on your requirements.
    return jsonify(result), 200