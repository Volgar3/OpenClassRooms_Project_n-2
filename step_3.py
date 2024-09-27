from step_2 import scrap_category
from bs4 import BeautifulSoup
from requests import get
import csv


def scrap_categories(url, has_images=False):
    
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
   
    categories = soup.find_all("ul", class_= "nav nav-list")
    
    
    #Ici, étant donné que soup.find_all("ul") renvoie une liste, je dois utilisé une variable dans un boucle pour parcourir la liste
    urlpart = []
    for category in categories: 
        hrefs = category.find_all("a")[1:]
        for url in hrefs:
            href = url.get('href')
            urlpart.append(href)
    
    # On complète les url obtenues et on créé des fichiers csv pour chaque catégorie
    
    for x in urlpart:
        complete_url = "https://books.toscrape.com/catalogue/category/" + x.replace('../', '')
        scrap_category(complete_url, has_images=has_images)
            

    return  
    
    

if __name__ == '__main__':
    scrap_categories("https://books.toscrape.com/catalogue/category/books_1/index.html")