import math


class Rational:
    def __init__(self, num=1, denom=2):
        if denom == 0:
            print("denominator cannot be equal to 0")
            denom = 2
        elif num > denom:
            print("numerator cannot be bigger then denominator")
            num = 1
        divisor = int(math.gcd(int(num), int(denom)))
        self._num = int(num / divisor)
        self._denom = int(denom / divisor)

    def __str__(self):
        if self._num / self._denom == 1:
            print(1)
        else:
            print(f"{self._num}/{str(self._denom)}")


rational = Rational(2,0)
rational.__str__()
