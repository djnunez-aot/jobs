# scraper-backend/scrapers/init.py

from real_python_scraper import scrape_realpython
from indeed_scraper import scrape_indeed
from pprint import pprint


# def scrape_jobs(location, job_title):
#     # Call the scrape function or any other scrapers here
#     results_zip = scrape_ziprecruiter(location, job_title)
#     results_indeed = scrape_indeed(location, job_title)

#     print(results)
#     # return results

results_realpython = scrape_realpython("Software Developer", "AA")
# results_indeed = scrape_indeed("Software Developer", "New York, NY")

pprint(results_realpython)
# print(results_indeed)
