class Complex:

    def __init__(self, re, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        if self.re >= 0 and self.im >= 0:
            return f"{self.re} + {self.im}*j"

        elif self.re < 0 and self.im >= 0:
            return f"({self.re}) + {self.im}*j"

        elif self.re >= 0 and self.im < 0:
            return f"{self.re} + ({self.im})*j"

        elif self.re < 0 and self.im < 0:
            return f"({self.re}) + ({self.im})*j"

    def __eq__(self, num):
        return self.re == num.re and self.im == num.im

    def add(self, num):
        return Complex(self.re + num.re, self.im + num.im)

    def sub(self, num):
        return Complex(self.re - num.re, self.im - num.im)

    def mul(self, num):
        res = Complex(
            self.re * num.re - self.im * num.im,
            num.re * self.im + self.re * num.im
        )
        return res

    def dev(self, num):
        res = Complex(
            (self.im * num.re - self.re * num.im) /
            (num.re ** 2 + num.im ** 2),
            (self.re * num.re + self.im * num.im) /
            (num.re ** 2 + num.im ** 2)
        )
        return res

    def mod(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5
