from math import gcd


class Rational:
    def __init__(self, num=1, denom=2):
        if denom == 0:
            raise ZeroDivisionError
        if not isinstance(num, int):
            raise TypeError("Wrong argument(s)")
        if not isinstance(denom, int):
            raise TypeError("Wrong argument(s)")
        self._num = num
        self._denom = denom

    def ab_form(self):
        if (self._num / self._denom) == 1:
            return 1
        else:
            return f"{self._num // gcd(self._num, self._denom)}/{self._denom // gcd(self._num, self._denom)}"

    def float_form(self):
        if self._num / self._denom == 1:
            return 1
        else:
            return self._num / self._denom


rational = Rational(1, 2)
print(rational.float_form())
print(rational.ab_form())
