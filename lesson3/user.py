class User:   

    def __init__(self, first_name, last_name):
       self.firstname = first_name
       self.lastname = last_name

    def sayName (self):
       print (f"Имя: {self.firstname}")

    def sayLast (self):
        print (f"Фамилия: {self.lastname}")

    def sayFirstLast (self):
        print (f"Имя и фамилия: {self.firstname} {self.lastname}")