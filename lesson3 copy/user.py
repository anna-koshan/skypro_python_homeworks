class User:   

    def __init__(self, first_name, last_name):
       self.firstname = first_name
       self.lastname = last_name

    def get_first_name (self):
       print (f"Имя: {self.firstname}")

    def get_last_name (self):
        print (f"Фамилия: {self.lastname}")

    def get_full_name (self):
        print (f"Имя и фамилия: {self.firstname} {self.lastname}")