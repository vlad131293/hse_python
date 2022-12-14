import unittest
from complex import Complex


class TestComplex(unittest.TestCase):

    def test_equal(self):
        first = Complex(1, 7)
        second = Complex(1, 7)
        self.assertEqual(first, second)

    def test_not_qual(self):
        first = Complex(2, 6)
        second = Complex(-1, 6)
        self.assertNotEqual(first, second)

    def test_str(self):
        expected = '(-1) + 2*j'
        self.assertEqual(str(Complex(-1, 2)), expected)

    def test_add(self):
        expected = '4 + (-4)*j'
        self.assertEqual(str(Complex(1, 2).add(Complex(3, -6))), expected)

    def test_sub(self):
        expected = '(-4) + (-11)*j'
        self.assertEqual(str(Complex(-1, -5).sub(Complex(3, 6))), expected)

    def test_mul(self):
        expected = '(-18) + 40*j'
        self.assertEqual(str(Complex(12, -2).mul(Complex(-2, 3))), expected)

    def test_dev(self):
        expected = '(-0.5) + (-1.5)*j'
        self.assertEqual(str(Complex(4, -2).dev(Complex(-2, 2))), expected)

    def test_mod(self):
        self.assertEqual(Complex(8, 6).mod(), 10.0)


if __name__ == "__main__":
    unittest.main()
