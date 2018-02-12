from __future__ import absolute_import

import numpy as np

from sorting.lib.constant import QUICKSORT
from sorting.sorting_algorithms.abstract_sorting import AbstractSorting


class QuickSort(AbstractSorting):

    def __init__(self):
        """
        Implements the quick sort algorithm. See: https://en.wikipedia.org/wiki/Quicksort.

        """
        super(QuickSort, self).__init__(QUICKSORT)

    @property
    def get_name(self):
        """
        Returns the name of the sorting algorithm.

        :return: str
        """

        return self.name

    @classmethod
    def sort(cls, numbers):
        """
        Sort the list of numbers using quick sort.
        :param numbers: [float]
        :return: ([float]) Sorted list of the numbers.
        """

        if len(numbers) < 2:
            return numbers

        pivot = cls.get_pivot(numbers)

        numbers, j = cls.partition(numbers, pivot)
        number_pivot = numbers[j]

        numbers_1 = cls.sort(numbers[0: j])
        numbers_2 = cls.sort(numbers[j + 1:])
        return numbers_1 + [number_pivot] + numbers_2

    @classmethod
    def get_pivot(cls, numbers):
        """
        Returns the index of a pivot for quick sort.

        :param numbers: [float]
        :return: int
        """
        n = len(numbers)
        pivot = np.random.randint(n)
        return pivot

    @classmethod
    def partition(cls, numbers, pivot):
        """
        Partition step of quick sort.

        :param numbers: [float]
        :param pivot: int
        :return: [float], int
        """

        numbers = cls.swap_numbers(numbers, 0, pivot)
        j = 0
        t = len(numbers) - 1

        while j < t:
            if numbers[j + 1] <= numbers[j]:
                numbers = cls.swap_numbers(numbers, j, j + 1)
                j += 1
            else:
                numbers = cls.swap_numbers(numbers, j + 1, t)
                t -= 1
        return numbers, j

    @classmethod
    def swap_numbers(cls, numbers, i, j):
        """
        Swap numbers[i] and numbers[j]

        :param numbers: [float]
        :param i: int
        :param j: int
        :return: [float]
        """

        assert i < len(numbers) and j < len(numbers)

        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp
        return numbers
