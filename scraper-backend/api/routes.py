from flask import Blueprint, request
from scrapers.init import scrape_jobs

api = Blueprint('api', __name__)

@api.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    location = data.get('location')
    job_title = data.get('job_title')
    results = scrape_jobs(location, job_title)
    return results
