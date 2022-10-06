class Product:
    def __init__(self, price=0, description="Empty", height=0, width=0, length=0):
        self.price = price
        self.description = description
        self.height = height
        self.width = width
        self.length = length


class Customer:
    def __init__(self, name="Empty", surname="Empty", patronymic="Empty", phone_number="Empty"):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone_number = phone_number


class Order:
    def __init__(self, customer, *args):
        self.products = args
        self.customer = customer

    def total_price(self):
        total_price = 0
        for order in self.products:
            total_price += order.price
        return total_price


product_1 = Product(10, "Fork", 3, 5, 18)
product_2 = Product(20, "Doll", 30, 10, 3)
product_3 = Product(7, "Duck toy", 5, 8, 10)

customer_1 = Customer("Hudzovskyi", "Mark", "Yuriiovych", "+123567890")

order_1 = Order(customer_1, product_1, product_2, product_3)

print(order_1.total_price())