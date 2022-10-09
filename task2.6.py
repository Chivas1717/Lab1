class BinaryTree:
    def __init__(self, code, price):
        if not isinstance(code, int):
            raise TypeError("Wrong product code")
        if not isinstance(price, int):
            raise TypeError("Wrong price")
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
# Compare the new value with the parent node
        if self.code:
            if code < self.code:
                if self.left is None:
                    self.left = BinaryTree(code, price)
                else:
                    self.left.insert(code, price)
            elif code > self.code:
                if self.right is None:
                    self.right = BinaryTree(code, price)
                else:
                    self.right.insert(code, price)
        else:
            self.code = code
            self.price = price

    def find_product(self, code, quantity):
        if not isinstance(code, int):
            raise TypeError("Wrong product code")
        if not isinstance(quantity, int):
            raise TypeError("Wrong quantity")
        if self.code == code:
            return quantity * self.price
        if self.left:
            if self.code > code:
                return self.left.find_product(code, quantity)
        if self.right:
            if self.code < code:
                return self.right.find_product(code, quantity)
        raise ValueError("Product code not found")

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.code, self.price),
        if self.right:
            self.right.printTree()


root = BinaryTree(27, 5)
root.insert(14, 7)
root.insert(35, 10)
root.insert(31, 3)
root.insert(10, 4)
root.insert(19, 5)
code = int(input())
quantity = int(input())
print(root.find_product(code, quantity))
# root.printTree()