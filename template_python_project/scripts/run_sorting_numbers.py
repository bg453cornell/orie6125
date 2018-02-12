from __future__ import absolute_import

from sorting.services.sort_numbers import SortNumbers
from sorting.lib.constant import QUICKSORT
from sorting.initializers.log import SortingLog

logger = SortingLog(__name__)


if __name__ == '__main__':
    # Example:
    # python -m scripts.run_sorting_numbers
    numbers = [9, 15, 2]
    sort_numbers = SortNumbers(QUICKSORT)

    logger.info("Sort the numbers: ")
    logger.info(numbers)

    numbers = sort_numbers.sort_numbers(numbers)

    logger.info("Sorted numbers: ")
    logger.info(numbers)
