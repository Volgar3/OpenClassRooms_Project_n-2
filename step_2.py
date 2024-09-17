from step_1 import scrap_book
from bs4 import BeautifulSoup
from requests import get

def scrap_category(url):
    while url:
        response = get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        h3_liste = soup.find_all('h3')

        liste_url_livre = []
        for h3 in h3_liste:
        
            liste_a = h3.find('a')
            if liste_a and 'href' in liste_a.attrs:
            
                livre_url = 'https://books.toscrape.com/catalogue/' + liste_a['href'].replace('../../../', '')
           
                liste_url_livre.append(livre_url)

        for url in liste_url_livre:
            scrap_book(url)

        li = soup.find('li', class_= 'next')
        if li:
            bouton_next = li.find('a')
            next_page_url = f'https://books.toscrape.com/catalogue/category/books/mystery_3/{ bouton_next['href'] }'
            url = next_page_url
        else: 
            url = None

if __name__ == '__main__':
    scrap_category('https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html')