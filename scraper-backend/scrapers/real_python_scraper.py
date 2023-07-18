import requests
from bs4 import BeautifulSoup

# Define the URL
url = f"https://realpython.github.io/fake-jobs/"


def scrape_realpython(job_search_keywords, job_search_locations):
    print(
        f"Scraping job listings for {job_search_keywords} in {job_search_locations}..."
    )

    # Format job title and location for the URL
    job_search_keywords = job_search_keywords.split()

    print(job_search_keywords)

    print(f"Sending a GET request to: {url}")

    # Send a GET request to the website
    response = requests.get(url, timeout=10)

    print(f"Received response with status code: {response.status_code}")

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the job postings on the page
    job_postings = soup.find_all("div", class_="card-content")

    print(f"Found {len(job_postings)} job postings")

    # Extract the relevant information from selected job posting
    jobs = []
    for job in job_postings:
        title = job.find("h2", class_="title is-5").get_text()
        company = job.find("h3", class_="subtitle is-6 company").get_text()
        location = job.find("p", class_="location").get_text(strip=True)
        post_date = job.find("time").get_text()

        title_keywords = title.split()
        location_keyword = location.split()

        # for job_keyword in job_search_keywords:
        #     if job_keyword in title:
        #         for job_location in job_search_locations:
        #             if job_location in location:
        #                 jobs.append(
        #                     {
        #                         "title": title,
        #                         "company": company,
        #                         "location": location,
        #                         "post_date": post_date,
        #                     }
        #                 )

        if (bool(set(job_search_keywords) & set(title_keywords))) and (
            bool(set(job_search_locations) & set(location_keyword))
        ):
            print(title_keywords)
            print(location_keyword)
            jobs.append(
                {
                    "title": title,
                    "company": company,
                    "location": location,
                    "post_date": post_date,
                }
            )

    print(f"Scraped {len(jobs)} job listings")

    return jobs
