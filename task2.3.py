class Product:
    def __init__(self, price=0, description="Empty", height=0, width=0, length=0):
        if price < 0:
            raise ValueError
        if not isinstance(price, int):
            raise TypeError("Price must be a number")
        # if not isinstance((height, width, length), int):
        #     raise TypeError("Dimension must be a number")
        self.price = price
        self.description = description
        self.height = height
        self.width = width
        self.length = length

    def __str__(self):
        return f"{self.description}'s price is {self.price}. Dimensions are: {self.height}x{self.width}x{self.length}"


class Customer:
    def __init__(self, name="Empty", surname="Empty", patronymic="Empty", phone_number="Empty"):
        # if not isinstance(phone_number, (int, float)):
        #     raise TypeError("Mobile phone isn't a number")
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone_number = phone_number


class Order:
    def __init__(self, customer, *args):
        if not isinstance(customer, Customer):
            raise TypeError("There is no customer")
        self.products = []
        self.customer = customer
        self.products_quantity = []
        for i in args:
            self.add_product(i)
        self.money = 0

    def add_product(self, product):
        if product in self.products:
            self.products_quantity[self.products.index(product)] += 1
        else:
            self.products.append(product)
            self.products_quantity.append(1)

    def delete_product(self, product):
        if product in self.products:
            if self.products_quantity[self.products.index(product)] > 1:
                self.products_quantity[self.products.index(product)] -= 1
            else:
                self.products.pop(self.products.index(product))
                self.products_quantity.pop(self.products.index(product))

    def total_price(self):
        total_price = 0
        for order in self.products:
            total_price += order.price * self.products_quantity[self.products.index(order)]
        return total_price

    def __str__(self):
        return f'The price of order for {self.customer.surname} {self.customer.name} is {self.total_price()}'


product_1 = Product(10, "Fork", 3, 5, 18)
product_2 = Product(20, "Doll", 30, 10, 3)
product_3 = Product(7, "Duck toy", 5, 8, 10)
print(product_3.__str__())
customer_1 = Customer("Hudzovskyi", "Mark", "Yuriiovych", "+123567890")

order_1 = Order(customer_1, product_1, product_2, product_3)
order_1.add_product(product_1)
order_1.delete_product(product_2)
print(order_1.total_price())
