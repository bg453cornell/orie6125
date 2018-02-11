import unittest

from nose.tools import raises

from sorting.sorting_algorithms.abstract_sorting import AbstractSorting


class B(AbstractSorting):
    def __init__(self):
        super(B, self).__init__('a')

    @property
    def get_name(self):
        super(B, self).get_name


class TestAbstractSorting(unittest.TestCase):

    def setUp(self):
        self.test = B()

    @raises(NotImplementedError)
    def test_get_name(self):
        self.test.get_name
