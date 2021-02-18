from unittest import TestCase
from rectangle import Rectangle
from two_d_point import TwoDPoint
import unittest

class TestRectangle(TestCase):

    def test_center(self):
        newRect = Rectangle(2.0, 1.0, 0.0, 1.0, 0.0, 0.0, 2.0, 0.0)
        self.assertEqual(TwoDPoint(1.0, 0.5), newRect.center())
        newRect2 = Rectangle(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0)
        self.assertEqual(TwoDPoint(0.0,0.0), newRect2.center())

    def test_area(self):
        newRect = Rectangle(2.0, 1.0, 0.0, 1.0, 0.0, 0.0, 2.0, 0.0)
        self.assertEqual(2.0, newRect.area())
        newRect2 = Rectangle(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0)
        self.assertEqual(16.0, newRect2.area())

print(Rectangle(2.0, 1.0, 0.0, 1.0, 0.0, 0.0, 2.0, 0.0)) # Print statement
print(Rectangle(2.0, 1.0, 0.0, 1.0, 0.0, 0.0, 2.0, 0.0) == (Rectangle(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0))) # Not equal to each other
print(Rectangle(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0) == Rectangle(2.0, 2.0, -2.0, 2.0, -2.0, -2.0, 2.0, -2.0)) # Equal to each other

if __name__ == "__main__":
    unittest.main()
# Test out eq and str method