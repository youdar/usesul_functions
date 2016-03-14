#!/usr/bin/env python
from __future__ import division
from get_sub_dir_dates import get_sub_dir_dates
from get_table_hdfs_location import get_table_hdfs_location
import unittest
import sys

__author__ = 'youval.dar'


class CollectDates(unittest.TestCase):

    def test_get_sub_dir_dates(self):
        print sys._getframe().f_code.co_name
        acme_table_name = 'youval_db.acme_with_account_info'
        dr = get_table_hdfs_location(acme_table_name,print_out=False)
        dates = list(get_sub_dir_dates(dr))
        print dates[0]


def run_selected_tests():
    """  Run selected tests

  1) List in "tests" the names of the particular test you want to run
  2) Comment out unittest.main()
  3) Un-comment unittest.TextTestRunner().run(run_selected_tests())
  """
    tests = ['test_something','test_something_else']
    suite = unittest.TestSuite(map(MyTestCase,tests))
    return suite


if __name__ == '__main__':
    # use for individual tests
    # unittest.TextTestRunner().run(run_selected_tests())

    # Use to run all tests
    unittest.main()
