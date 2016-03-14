#!/usr/bin/python
from __future__ import division

import sys
import unittest

import ip_conversion

__author__ = 'youval.dar'


class IpConversion(unittest.TestCase):


    def test_ip2int(self):
        print sys._getframe().f_code.co_name
        answer = ip_conversion.ip2int('50.207.16.18')
        self.assertEqual(answer, 852430866)
        answer = ip_conversion.ip2int('50.207.16.18:1234')
        self.assertEqual(answer, 852430866)

    def test_int2ip(self):
        print sys._getframe().f_code.co_name
        answer = ip_conversion.int2ip(852430866)
        self.assertEqual(answer, '50.207.16.18')


    # def test_ip_range_expand(self):
    #     # todo: finish conversion function
    #     print sys._getframe().f_code.co_name
    #     ip_start,ip_end  = ip_conversion.ip_range_expand('50.207.16.18/8')
    #     self.assertEqual(ip_start, '50.0.0.0')
    #     self.assertEqual(ip_end, '50.255.255.255')
    #     #
    #     ip_start,ip_end  = ip_conversion.ip_range_expand('50.207.16.18/32')
    #     self.assertEqual(ip_start, '50.207.16.18')
    #     self.assertEqual(ip_end, '50.207.16.18')
    #     #
    #     ip_start,ip_end  = ip_conversion.ip_range_expand('50.207.16.18/31')
    #     self.assertEqual(ip_start, '50.207.16.18')
    #     self.assertEqual(ip_end, '50.207.16.19')


def run_selected_tests():
    """  Run selected tests

  1) List in "tests" the names of the particular test you want to run
  2) Comment out unittest.main()
  3) Un-comment unittest.TextTestRunner().run(run_selected_tests())
  """
    tests = ['test_file_formats', 'test_iselection_is_in_correct_order']
    suite = unittest.TestSuite(map(IpConversion, tests))
    return suite


if __name__ == '__main__':
    # use for individual tests
    # unittest.TextTestRunner().run(run_selected_tests())

    # Use to run all tests
    unittest.main(verbosity=0)
