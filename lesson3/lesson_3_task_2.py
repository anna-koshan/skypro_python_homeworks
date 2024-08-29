from smartphone import Smartphone

catalog = [
    Smartphone("SE", "iPhone", "+791234567899"),
    Smartphone("13 mini", "iPhone", "+791232123456"),
    Smartphone("Galaxi S24", "Samsung", "+79315552266"),
    Smartphone("Galaxi S24+", "Samsung", "+79216548833"),
    Smartphone("Galaxi S24 Ultra", "Samsung", "+79114798735")
]

for phone in catalog:
    phone.sayPhone()