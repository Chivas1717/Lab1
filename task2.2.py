import math
class Rational:
    def __init__(self, num, denom):
        divisor = math.gcd(int(num), int(denom))
        self.num = int(num / divisor),
        self.denom = int(denom / divisor),
        print(self.denom)

    def __str__(self):
        print(f"{self.num}/{str(self.denom)}")

rational = Rational(2, 4)
rational.__str__()
