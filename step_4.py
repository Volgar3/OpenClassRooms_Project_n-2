from step_3 import scrap_categories
import os

def scrap_categories_with_images(url):
    if not os.path.exists('images'):
        os.makedirs('images')
    scrap_categories(url, has_images=True)


# def scrap_categories_with_images(url):
    
#     response = get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     #Obtention des urls
#     url = []
#     part_img_urls = soup.find_all("img", class_="thumbnail")

#     # Extraire les URLs partielles
#     for part_img_url in part_img_urls:
#         url.append(part_img_url['src'])

#     # Concaténer la base URL à chaque URL partielle
#     complete_urls = []
#     for x in url:
#         complete_url = "https://books.toscrape.com" + x.replace('../../..', '')
#         complete_urls.append(complete_url)

#     # Afficher toutes les URLs complètes après la boucle
#     for complete_url in complete_urls:
#         print(complete_url)
 
    
    
if __name__ == '__main__':
    scrap_categories_with_images("https://books.toscrape.com/catalogue/category/books_1/index.html")
