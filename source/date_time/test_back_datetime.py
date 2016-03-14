#!/usr/bin/env python
from __future__ import division
import back_datetime
import unittest
import sys

__author__ = 'youval.dar'


class TestBackDateTime(unittest.TestCase):

    def test_start_date_time(self):
        """ test deduction is done correctly  """
        print sys._getframe().f_code.co_name
        ref = back_datetime.get_back_date_time(less_n_days=0)
        d = back_datetime.get_back_date_time(less_n_days=2)
        h = back_datetime.get_back_date_time(less_n_hours=2)
        m = back_datetime.get_back_date_time(less_n_months=2)
        mn = back_datetime.get_back_date_time(less_n_minutes =2)
        # time format YYYY-MM-DD:HH:00:00
        print 'ref :',ref
        print 'd-2 :',d
        print 'h-2 :',h
        print 'm-2 :',m
        print 'mn-2:',mn
        self.assertEqual(len(d),19)
        self.assertEqual(len(h),19)
        self.assertEqual(len(m),19)
        self.assertNotEqual(int(ref[8:10]),int(d[8:10]))
        self.assertNotEqual(int(ref[11:13]),int(h[11:13]))
        self.assertNotEqual(int(ref[5:7]),int(m[5:7]))


def run_selected_tests():
    """  Run selected tests

  1) List in "tests" the names of the particular test you want to run
  2) Comment out unittest.main()
  3) Un-comment unittest.TextTestRunner().run(run_selected_tests())
  """
    tests = ['test_something','test_something_else']
    suite = unittest.TestSuite(map(TestBackDateTime,tests))
    return suite


if __name__ == '__main__':
    # use for individual tests
    # unittest.TextTestRunner().run(run_selected_tests())

    # Use to run all tests
    unittest.main()
