import unittest
from sum.add_numbers import Sum


class TestSum(unittest.TestCase):

    def test_sum(self):
        assert Sum.sum(1, 2) == 3
