from step_3 import scrap_categories

def scrap_categories_with_images(url):
    scrap_categories(url, has_images=True)

if __name__ == '__main__':
    scrap_categories_with_images("https://books.toscrape.com/index.html")