from unittest import TestCase
from quadrilateral import Quadrilateral
import unittest
class TestQuadrilateral(TestCase):

    def test_side_lengths(self):
        #TODO
        self.assertEqual((1.0,1.0,1.0,1.0), Quadrilateral(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0).side_lengths()) # Checks if they are equal to each other
        self.assertEqual((4.0, 4.0, 4.0, 4.0), Quadrilateral(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0).side_lengths())
        self.assertFalse((4.0, 4.0, 4.0, 3.0) == Quadrilateral(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0)) # Checks to makes sure that the value is false

    def test_smallest_x(self):
        #TODO
        self.assertEqual(0.0, Quadrilateral(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0).smallest_x())
        self.assertEqual(-2.0, Quadrilateral(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0).smallest_x())
        self.assertFalse(0.0 == Quadrilateral(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0).smallest_x())


print(Quadrilateral(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0)) # Printing to make sure it gives the right str output
print(Quadrilateral(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0) == (Quadrilateral(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0))) # should print false
print(Quadrilateral(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0) == (Quadrilateral(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0))) # Should print true

if __name__ == "__main__":
    unittest.main()
# Test eq method and more on the str