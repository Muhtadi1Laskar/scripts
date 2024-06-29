import requests
from bs4 import BeautifulSoup

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
        return None

def parse_data(content):
    soup = BeautifulSoup(content, "html.parser")
    parent_div = soup.find('div')
    return parent_div

def main():
    response = make_request()
    data = parse_data(response.content)

    return None

main()