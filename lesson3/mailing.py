from address import Address

class Mailing:

    def __init__(self, to_address, from_address, cost, track):
       self.to_address = to_address
       self.from_address = from_address
       self.cost = cost
       self.track = track

    def sayAddress(self):
        print(f'Отправление {self.track} из {self.from_address.get_Info()} в {self.to_address.get_Info()}. Стоимость {self.cost} рублей.')
