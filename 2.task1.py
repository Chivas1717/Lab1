class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    # getter method
    def get_length(self):
        return self.length

    # setter method
    def set_length(self, x):
        try:
            if x < 0.0 or x > 20.0:
                print("set value from 0.0 to 20.0")
            else:
                self.length = float(x)
        except ValueError:
            print("not a float number")

    # getter method
    def get_width(self):
        return self.width

    # setter method
    def set_width(self, x):
        try:
            if x < 0.0 or x > 20.0:
                print("set value from 0.0 to 20.0")
            else:
                self.width = float(x)
        except ValueError:
            print("not a float number")

    def get_perimeter(self):
        return round(2 * (self.width + self.length), 3)

    def get_area(self):
        return round(self.width * self.length, 3)


rect = Rectangle()
rect.set_length(0.1)
rect.set_width(0.2)
print(rect.get_length())
print(rect.get_perimeter())
print(rect.get_area())
