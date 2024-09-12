class Address:
   
    def __init__(self, index, city, street, home, room):
       self.index = index
       self.city = city
       self.street = street
       self.home = home
       self.room = room

    def sayInfo (self):
        return f'{self.index}, {self.city}, {self.street}, {self.home} - {self.room}'

    
