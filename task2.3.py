class Product:
    def __init__(self, price, description, dimension):
        self._price = price
        self._description = description
        self._dimension = dimension


class Customer:
    def __init__(self,surname, name, patronymic, cellnum,):
        self._surname = surname
        self._name = name
        self._patronymic = patronymic
        self._cellnum = cellnum


class Order(Product, Customer):
    def __init__(self, customer, products):
        self._customer = customer
        self._products = products

    def wadawd(self):
        self._surname = "lol"

