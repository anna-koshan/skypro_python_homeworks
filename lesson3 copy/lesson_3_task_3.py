from mailing import Mailing 
from address import Address

to_address = Address("123456", "Москва", "ул. Советская", "д. 2", "45")
from_address = Address("789564", "Тюмень", "ул. Наличная", "д. 23", "56")
my_mailing = Mailing(to_address, from_address, 1500, "1245789635")
my_mailing.sayAddress()