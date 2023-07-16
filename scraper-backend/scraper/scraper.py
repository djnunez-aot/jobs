    import requests
from bs4 import BeautifulSoup

def my_scrape_function(url):
    # Make a request to the website
    r = requests.get(url)
    # Use the 'html.parser' to parse the page
    soup = BeautifulSoup(r.text, 'html.parser')
    # This function will return the parsed webpage
    return soup