from step_1 import scrap_book
from bs4 import BeautifulSoup
from requests import get

def scrap_category(url):
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    while url: 
        h3_liste = soup.find_all('h3')

        liste_url_livre = []
        for h3 in h3_liste:
        
            Liste_a = h3.find('a')
            if Liste_a and 'href' in Liste_a.attrs:
            
                livre_url = 'https://books.toscrape.com/catalogue/' + Liste_a['href'].replace('../../../', '')
           
                liste_url_livre.append(livre_url)

        for url in liste_url_livre:
            print(url)



        li = soup.find('li', class_= 'next')
        Bouton_next = li.find('a')
        
        if Bouton_next:
            next_page_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html' + Bouton_next['href']
            url = next_page_url
        else: 
            break

    print(url)



    #scrap_book(url)

    
if __name__ == '__main__':
    scrap_category('https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html')