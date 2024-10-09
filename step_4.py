import os

from step_3 import scrap_categories

def scrap_categories_with_images(url):
    if not os.path.exists('images'):
        os.makedirs('images')
    scrap_categories(url, has_images=True)
    
    
    
if __name__ == '__main__':
    scrap_categories_with_images("https://books.toscrape.com/catalogue/category/books_1/index.html")
