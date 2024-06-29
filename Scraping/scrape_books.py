import requests
from bs4 import BeautifulSoup
import json

main_url = "https://www.rokomari.com/book/category/403/foreign-language-books"
parameter = "xyz=&inStock=on"
BASE_URL = f"{main_url}?{parameter}"


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


def get_total_pages(content):
    soup = BeautifulSoup(content, "html.parser")
    parent_div = soup.find("div", class_="pagination")

    if parent_div:
        pages = parent_div.find_all("a")
        return int(pages[-2].text)
    return 0


def parse_books(content):
    soup = BeautifulSoup(content, "html.parser")
    parent_divs = soup.find_all("div", class_="book-list-wrapper")
    book_list = []

    if parent_divs:
        for child in parent_divs:
            book_title = child.find("h4", class_="book-title")
            book_author = child.find("p", class_="book-author")
            book_price_element = child.find("p", class_="book-price")
            image_element = child.find("img")
            website_link = child.find("a")
            link = f"https://www.rokomari.com/{website_link['href']}"

            if book_price_element:
                prices = list(book_price_element.stripped_strings)

                if len(prices) > 1:
                    original_price, discount_price = prices
                else:
                    original_price = prices[0]
                    discount_price = None

                book_list.append(
                    {
                        "title": book_title.text,
                        "image": image_element["data-src"],
                        "author": book_author.text,
                        "original_price": original_price,
                        "discount_price": discount_price,
                        "link": link,
                    }
                )

    return book_list


def save_data(data):
    with open("Data/books.json", "w", buffering=1024) as f:
        json.dump(data, f, indent=2)


def get_url(index):
    return f"{BASE_URL}&page={index}"


def get_books(pages):
    books = []

    if pages > 0:
        for index in range(1, pages+1):
            url = get_url(index)
            response = make_request(url)
            book_list = parse_books(response.content)
            books.append(book_list)
    return books


def main():
    URL = f"{BASE_URL}&page=1"
    response = make_request(URL)

    pages = get_total_pages(response.content)
    books = get_books(pages)
    save_data(books)

main()
