class Node:
    def __init__(self, code, price):

        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
# Compare the new value with the parent node
        if self.code:
            if code < self.code:
                if self.left is None:
                    self.left = Node(code, price)
                else:
                    self.left.insert(code, price)
            elif code > self.code:
                if self.right is None:
                    self.right = Node(code, price)
                else:
                    self.right.insert(code, price)
        else:
            self.code = code
            self.price = price

    def find_product(self, code, quantity):
        if not isinstance(code, int):
            print("Wrong product code")
        if not isinstance(quantity, int):
            print("Wrong quantity")
        if self.code == code:
            return quantity * self.price
        if self.left:
            if self.code > code:
                return self.left.find_product(code, quantity)
        if self.right:
            if self.code < code:
                return self.right.find_product(code, quantity)
        print("Not founded an product code")

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.code, self.price),
        if self.right:
            self.right.printTree()


root = Node(27, 5)
root.insert(14, 7)
root.insert(35, 10)
root.insert(31, 3)
root.insert(10, 4)
root.insert(19, 5)
code = int(input())
quantity = int(input())
print(root.find_product(code, quantity))
# root.printTree()