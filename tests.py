import unittest
import pandas as pd
import numpy as np
import os
import sys
import datetime
file_dir = os.getcwd()
sys.path.append(file_dir)

from pulldata import read_datasource_time

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_read_datasource_time_checkdatetime(self):
        source_string = 'Last updated at: Sun Apr 23 2017 12:25:08 GMT+0100 (BST)'
        source_time = datetime.datetime(2017,4,23,12,25,8)

        self.assertEquals(read_datasource_time(source_string),source_time)


if __name__ == '__main__':
    unittest.main()