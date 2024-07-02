from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import requests

def get_html(url):
    try:
        html = urlopen(url)
        return html
    except HTTPError as e:
        return e
    
def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/wiki/') and not re.search(':', href):
            full_url = f"http://en.wikipedia.org{href}"
            links.append(full_url)
    return links

def crawl(url, depth):
    """Recursively crawls the web starting from the given URL up to the specified depth."""
    if depth == 0:
        return

    html = get_html(url)
    if html is None:
        return

    print(f"Crawling: {url}")
    links = get_links(html)

    for link in links:
        crawl(link, depth - 1)


if __name__ == "__main__":
    start_url = "http://en.wikipedia.org/wiki/Web_crawler"
    crawl(start_url, 2)