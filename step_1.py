from requests import get
from bs4 import BeautifulSoup

def scrap_book(url):
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find('table')
    rows = table.find_all('tr')
    return {
        "product_page_url": url,
        "universal_ product_code": rows[0].find('td').text
    }

if __name__ == '__main__':
    result = scrap_book("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    print(result)