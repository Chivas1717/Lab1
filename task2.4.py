import re


class Statistic:
    def __init__(self, file):
        self.file = file

    def characters(self):
        try:
            file = open(self.file, "r")
        except FileNotFoundError:
            pass
        characters = 0
        for i in file:
            characters += len(i)
            characters -= len(i.split()) - 1
        file.close()
        return characters

    def words(self):
        try:
            file = open(self.file, "r")
        except FileNotFoundError:
            pass
        words = sum(
            len(re.findall(r"[a-zA-Zа-яА-ЯёЁіІїЇ0-9]*[,.'-]?[a-zA-Zа-яА-ЯёЁіІєЄїЇ0-9]+", lines)) for lines in file)
        return words

    def sentences(self):
        try:
            file = open(self.file)
        except FileNotFoundError:
            pass
        sentences = sum(len(re.findall(r"[A-ZА-ЯЁІЇ][^\.!?]*[\.!?]+", lines)) for lines in file)
        file.close()
        return sentences


test = Statistic("randomtxt.txt")
print(test.characters())
print(test.words())
print(test.sentences())


