# scraper-backend/scrapers/init.py

from real_python_scraper import scrape_realpython
from indeed_scraper import scrape_indeed
from pprint import pprint


def scrape_jobs(location, job_title):
    # Call the scrape function or any other scrapers here
    results = scrape_realpython(location, job_title) 
    # return results
    print(results)


