from __future__ import absolute_import

from abc import ABCMeta, abstractmethod


class AbstractSorting(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        """

        :param name: str
        """
        self.name = name

    @property
    def get_name(self):
        raise NotImplementedError("Not implemented")

    @classmethod
    @abstractmethod
    def sort(cls, numbers):
        raise NotImplementedError("Not implemented")
