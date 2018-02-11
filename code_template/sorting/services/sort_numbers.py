from __future__ import absolute_import


from sorting.lib.constant import QUICKSORT
from sorting.initializers.log import SortingLog
from sorting.sorting_algorithms.quick_sort import QuickSort

logger = SortingLog(__name__)


class SortNumbers(object):

    _possible_sorting_algorithms = [QUICKSORT]

    def __init__(self, name_method):
        self.sorting_object = None
        if name_method == QUICKSORT:
            self.sorting_object = QuickSort()
        else:
            raise Exception("Unknown sorting algorithm")

    def sort_numbers(self, numbers):
        """
        Sort numbers.

        :param numbers: [float]
        :return: [float]
        """

        name_method = self.sorting_object.get_name
        logger.info("Sorting numbers with %s" % name_method)

        return self.sorting_object.sort(numbers)
