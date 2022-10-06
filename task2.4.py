class Statistic:
    def __init__(self, file):
        self.file = file
        self.data = file.read()

    def characters(self):
        return len(self.data)

    def words(self):
        return len(self.data.split())

    def sentences(self):
        return len(self.data.split("."))


f = open("randomtxt.txt", "r")
test = Statistic(f)
print(test.characters())
print(test.words())
print(test.sentences())


