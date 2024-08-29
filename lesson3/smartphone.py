class Smartphone:
    catalog = [1, 2, 3]
    
    def __init__(self, brand, model, number):
       self.brand = brand
       self.model = model
       self.number = number  

    def sayPhone (self):
       self.catalog[0] = self.brand
       print (f"{self.brand} - {self.model}. {self.number}")