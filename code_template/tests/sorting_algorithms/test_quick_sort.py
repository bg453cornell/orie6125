from __future__ import absolute_import

import unittest

from sorting.sorting_algorithms.quick_sort import QuickSort
from sorting.lib.constant import QUICKSORT


class TestQuickSort(unittest.TestCase):

    def setUp(self):
        self.sort = QuickSort()

    def test_get_name(self):
        assert self.sort.get_name == QUICKSORT
