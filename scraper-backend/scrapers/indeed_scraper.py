import requests
from bs4 import BeautifulSoup
import logging

# Create a logger
logger = logging.getLogger(__name__)


def scrape_indeed(job_title, location):
    logger.info(f"Scraping job listings for {job_title} in {location}...")

    # Format job title and location for the URL
    job_title = job_title.replace(' ', '+')
    location = location.replace(' ', '+').replace(',', '%2C')

    # Define the URL
    url = f"https://www.indeed.com/jobs?q={job_title}&l={location}&from=searchOnHP&vjk=1abacf56c6a4fa6e"

    logger.debug(f"Sending a GET request to: {url}")

    # Send a GET request to the website
    response = requests.get(url)

    logger.debug(f"Received response with status code: {response.status_code}")

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    logger.info(f"Found {len(job_postings)} job postings")

    # Find the job postings on the page 
    job_postings = soup.find_all('div', class_='cardOutline')

    # Extract the relevant information from each job posting
    jobs = []
    for job in job_postings:
        title = job.find('h2', class_='jobTitle').text
        company = job.find('span', class_='companyName').text
        location = job.find('div', class_='companyLocation').text
        compensation = job.find('div', class_='metadata salary-snippet-container').text
        description = job.find('div', class_='job-snippet').text
        post_date = job.find('span', class_='date').text

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'compensation': compensation,
            'description': description,
            'post_date': post_date
        })

    return jobs
