class Fraction:
    def __init__(self, numerator=1, denominator=1):
        self._numerator=numerator
        self._denominator=denominator

    def reduction(self):

        def gcd(numerator, denominator):
            remainder = numerator % denominator
            if remainder == 0:
                return denominator
            else:
                return gcd(max(denominator, remainder),min(denominator, remainder))

        gcdNum = gcd(max(self._numerator, self._denominator), min(self._numerator, self._denominator))
        return "{0:.0f}/{1:.0f}".format(self._numerator/gcdNum, self._denominator/gcdNum)