import csv
import os

from bs4 import BeautifulSoup
from requests import get

from step_1 import scrap_book

def scrap_category(url, has_images=False):
    
    #Création fichier CSV/écriture en-tete
    
    cat_name = url.split('/')[-2]
    print(cat_name)
    with open(cat_name + ".csv", "w", encoding="utf-8", newline='') as scrap_csv:
        en_tete = ["title", "product_page_url", "universal_product_code", "product_description", "price_including_tax",
                   "price_excluding_tax", "Availability", "review_rating", "category", "image_url"]
        writer = csv.DictWriter(scrap_csv, fieldnames=en_tete)
        writer.writeheader()

        while url:
            response = get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            h3_liste = soup.find_all('h3')

            #Récupération de chaque url des livres se trouvant dans une catégorie
            liste_url_livre = []
            for h3 in h3_liste:
                liste_a = h3.find('a')
                if liste_a and 'href' in liste_a.attrs:
                    livre_url = 'https://books.toscrape.com/catalogue/' + liste_a['href'].replace('../../../', '')
                    liste_url_livre.append(livre_url)

            #Utilisation de la fonction scrap_book(url) de la step_1 pour obtenir les informations de chaque livre
            for url in liste_url_livre:
                books_data = scrap_book(url)
                if has_images:
                    image_data = get(books_data['image_url']).content
                    print(books_data['image_url'])
                    with open(f'images/{books_data['title']}.{books_data['image_url'].rsplit('.', 1)[1]}', 'wb') as image:
                        image.write(image_data)

                writer.writerow(books_data)     
            
            #Vérification d'un bouton "next"
            li = soup.find('li', class_='next')
            if li:
                next_button = li.find('a')
                next_page_url = f"https://books.toscrape.com/catalogue/category/books/mystery_3/{next_button['href']}"
                url = next_page_url
            else:
                url = None

if __name__ == '__main__':
    scrap_category('https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html')
