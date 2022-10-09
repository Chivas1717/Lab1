class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    # getter method
    def get_length(self):
        return self.length

    # setter method
    def set_length(self, x):
        if not (isinstance(x, (float, int))):
            raise TypeError("Length must be a float")
        if x <= 0 or x >= 20:
            raise ValueError("Length must be in range [0,20]")
        self.length = float(x)


    # getter method
    def get_width(self):
        return self.width

    # setter method
    def set_width(self, x):
        if not (isinstance(x, (float, int))):
            raise TypeError("Width must be a float");
        if x <= 0 or x >= 20:
            raise ValueError("Width must be in range [0,20]");
        self.width = float(x)

    def get_perimeter(self):
        return round(2 * (self.width + self.length), 3)

    def get_area(self):
        return round(self.width * self.length, 3)


rect = Rectangle(1, 7)
rect.set_length(0.1)
rect.set_width(0.2)
print(rect.get_length())
print(rect.get_perimeter())
print(rect.get_area())
