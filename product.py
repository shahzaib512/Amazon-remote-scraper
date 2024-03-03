# product/product.py

class Product:
    def __init__(self, title, price, image_url, rating, scraping_timestamp):
        self.title = title
        self.price = price
        self.image_url = image_url
        self.rating = rating
        self.scraping_timestamp = scraping_timestamp
