from __future__ import absolute_import

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class SortingLog(object):

    def __init__(self, name):
        self.name = name
        self._log = logging.getLogger(name)

    def info(self, msg):
        """
        :param msg: dict
        """

        self._log.info(msg)
