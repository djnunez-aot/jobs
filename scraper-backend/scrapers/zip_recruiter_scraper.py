import requests
from bs4 import BeautifulSoup
import logging

# Create a logger
logger = logging.getLogger(__name__)

def scrape_ziprecruiter(job_title, location):
    logger.info(f"Scraping job listings for {job_title} in {location}...")

    # Format job title and location for the URL
    job_title = job_title.replace(' ', '+')
    location = location.replace(' ', '+').replace(',', '%2C')

    # Define the URL
    url = f"https://www.ziprecruiter.com/jobs-search?search={job_title}&location={location}&no_explore="

    logger.debug(f"Sending a GET request to: {url}")

    # Send a GET request to the website
    response = requests.get(url)

    logger.debug(f"Received response with status code: {response.status_code}")

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the job postings on the page 
    job_postings = soup.find_all('div', class_='job_details')

    logger.info(f"Found {len(job_postings)} job postings")

    # Extract the relevant information from each job posting
    jobs = []
    for job in job_postings:
        title = job.find('h1', class_='job_title').text
        company = job.find('a', class_='hiring_company').text
        location = job.find('a', class_='hiring_location').text
        compensation = job.find('span', class_='job_characteristics_data t_compensation').text
        description = job.find('div', class_='job_description').text
        post_date = job.find('span', class_='data').text

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'compensation': compensation,
            'description': description,
            'post_date': post_date
        })

    logger.info(f"Scraped {len(jobs)} job listings")

    return jobs
