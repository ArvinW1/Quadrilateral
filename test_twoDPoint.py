from unittest import TestCase
from two_d_point import TwoDPoint
import unittest

class TestTwoDPoint(TestCase):

    def test_from_coordinates(self): # Not sure if this is how it is supposed to be tested
        # TODO
        Expected = []
        Expected.append(TwoDPoint(1.0,1.0))
        Expected.append(TwoDPoint(0.0,1.0))
        Expected.append(TwoDPoint(0.0,0.0))
        Expected.append(TwoDPoint(1.0,0.0))
        lst = [1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0]
        self.assertEqual(Expected, TwoDPoint.from_coordinates(lst))
        Expected2 = []
        Expected2.append(TwoDPoint(1.0,1.0))
        lst2 = [2.0, 2.0]
        self.assertFalse(Expected2 == TwoDPoint.from_coordinates(lst2)) # These are two points that are not equal to each other

if __name__ == "__main__":
    unittest.main()
 # Test out add method and sub method in the twoDpoint 
