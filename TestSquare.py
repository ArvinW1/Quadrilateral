from unittest import TestCase
from square import Square
from quadrilateral import Quadrilateral
import unittest

class TestSquare(TestCase):

    def test_snap(self):
        newSqu = Square(2.5, 2.5, 0.4, 2.5, 0.4, 0.4, 2.5, 0.4) # Positive Case
        snappedQuad = Quadrilateral(3.0, 3.0, 0.0, 3.0, 0.0, 0.0, 3.0, 0.0)
        self.assertEqual(snappedQuad, newSqu.snap())
        newSqu = Square(1.7, 1.7, 1.5, 1.7, 1.5, 1.5, 1.7, 1.5) # Positive Cases
        self.assertEqual(newSqu,  newSqu.snap())
        newSqu = Square(-2.5, -2.5, -0.6, -2.5, -0.6, -0.6, -2.5, -0.6) # Negative Cases
        snappedQuad = Quadrilateral(-2.0, -2.0, -1.0, -2.0, -1.0, -1.0, -2.0, -1.0)
        self.assertEqual(snappedQuad, newSqu.snap())
        newSqu = Square(-2.6, -2.6, -0.4, -2.6, -0.4, -0.4, -2.6, -0.4) # Negative Cases
        snappedQuad = Quadrilateral(-3.0, -3.0, 0.0, -3.0, 0.0, 0.0, -3.0, 0.0)
        self.assertEqual(snappedQuad, newSqu.snap())

print(Square(2.5, 2.5, 0.4, 2.5, 0.4, 0.4, 2.5, 0.4)) # Printing Square
print(Square(2.5, 2.5, 0.4, 2.5, 0.4, 0.4, 2.5, 0.4) == Square(2.5, 2.5, 0.4, 2.5, 0.4, 0.4, 2.5, 0.4)) # Equal to each other
print(Square(2.5, 2.5, 0.4, 2.5, 0.4, 0.4, 2.5, 0.4) == Square(1.7, 1.7, 1.5, 1.7, 1.5, 1.5, 1.7, 1.5)) # Not equal to each other
if __name__ == "__main__":
    unittest.main()
# Test out eq and str method 