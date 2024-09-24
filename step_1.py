from requests import get
from bs4 import BeautifulSoup

def scrap_book(url):
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
    
    #Liens des images des livres
    image = div.find('img')

    #Note du livre 
    review = soup.find('p', class_= "star-rating")
    classes = review.get('class')
    

    # A rendre dynamique
    formatted_title = title.replace(" ", "-")
    link = f'https://books.toscrape.com/catalogue/{formatted_title}' + image['src'].replace("../..", "")

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
        "category": liste_li[2].text.strip(),
        "image_url": link
    }
    
    return result
    
    
if __name__ == '__main__':
    result = scrap_book("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")  



