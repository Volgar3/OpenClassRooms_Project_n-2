import csv
import os 

from requests import get

from bs4 import BeautifulSoup

def scrap_book(url):
    
    #création du folder
    folder_path = '/Users/deles/Documents/Projets/Projet_n°2/Scraper/catégorie'
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Dossier créé : {folder_path}")
    
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    #Récupération du tableau
    table = soup.find('table')

    #Code upc 
    rows = table.find_all('tr')

    #Titre 
    title = soup.find('h1').text

    #Description du livre
    p = soup.find_all('p')[3]
    description_produit = p.text

    #Listes des balises td contenenant le prix ttc/htc, nb de livre disponible et le nombre de review 
    tds = table.find_all('td')
    liste_td = []
    for td in tds: 
        liste_td.append(td)

    #Catégorie du livre 
    div = soup.find('div', class_= "container-fluid page")
    lis = div.find_all('li')
    liste_li = []
    for li in lis:
        liste_li.append(li)
    expected_cat_name = liste_li[2].text.strip()
    
    #Liens des images des livres
    image = div.find('img')
    
    #Note du livre 
    review = soup.find('p', class_= "star-rating")
    classes = review.get('class')
    

    # A rendre dynamique
    formatted_title = title.replace(" ", "-")
    link = f'https://books.toscrape.com/' + image['src'].replace("../..", "")
    
   
    # On retourne toutes les informations dans un dictionnaire que l'on rempli en lors du return en assigant une clé à un élément
    result =  {
        "title": title,
        "product_page_url": url,
        "universal_product_code": rows[0].find('td').text,
        "product_description": description_produit,
        "price_including_tax": liste_td[3].text.replace("Â"," "),
        "price_excluding_tax": liste_td[2].text.replace("Â"," "), 
        "Availability": liste_td[5].text,
        "review_rating": classes[1],
        "category": expected_cat_name,
        "image_url": link
    }
   
    #Création fichier CSV/écriture en-tete
    
    if result['category'] == expected_cat_name:
    
    # Chemin complet du fichier CSV avec le nom de la catégorie
        csv_file_path = os.path.join(folder_path, f"{expected_cat_name}.csv")

# Vérification de l'existence du fichier CSV
        file_exists = os.path.exists(csv_file_path)

# Ouverture du fichier en mode ajout
        with open(csv_file_path, "a", encoding="utf-8", newline='') as scrap_csv:
    
            writer = csv.DictWriter(scrap_csv, fieldnames=result.keys()) #"fieldnames=result.keys()" permet de ne pas créer une variable en tete 
            if not file_exists:
                writer.writeheader()
            writer.writerow(result)
            
    else:
        
        with open(expected_cat_name + ".csv", "w", encoding="utf-8", newline='') as scrap_csv:
            writer = csv.DictWriter(scrap_csv, fieldnames=result.keys())
            writer.writeheader()
            writer.writerow(result)

    return result

if __name__ == '__main__':
    result = scrap_book("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")