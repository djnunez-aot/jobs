# scraper-backend/scrapers/init.py

from scrapers.zip_recruiter_scraper import scrape_ziprecruiter

def scrape_jobs(location, job_title):
    # Call the scrape function or any other scrapers here
    results = scrape_ziprecruiter(location, job_title)
    return results