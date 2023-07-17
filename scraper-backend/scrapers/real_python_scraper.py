import requests
from bs4 import BeautifulSoup
import logging

# Create a logger
logger = logging.getLogger(__name__)


def scrape_realpython(job_keywords, location):
    print(f"Scraping job listings for {job_keywords} in {location}...")

    # Format job title and location for the URL
    job_keywords = job_keywords.split()
    location = location.replace(" ", "+").replace(",", "%2C")

    print(job_keywords)

    # Define the URL
    url = f"https://realpython.github.io/fake-jobs/"

    print(f"Sending a GET request to: {url}")

    # Send a GET request to the website
    response = requests.get(url, timeout=10)

    print(f"Received response with status code: {response.status_code}")

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the job postings on the page
    job_postings = soup.find_all("div", class_="card-content")

    print(f"Found {len(job_postings)} job postings")

    # Extract the relevant information from each job posting
    jobs = []
    for job in job_postings:
        title = job.find("h2", class_="title is-5").get_text()
        company = job.find("h3", class_="subtitle is-6 company").get_text()
        location = job.find("p", class_="location").get_text(strip=True)
        post_date = job.find("time").get_text()

        for keyword in job_keywords:
            if keyword in title:
                jobs.append(
                    {
                        "title": title,
                        "company": company,
                        "location": location,
                        "post_date": post_date,
                    }
                )

    logger.info(f"Scraped {len(jobs)} job listings")

    return jobs
