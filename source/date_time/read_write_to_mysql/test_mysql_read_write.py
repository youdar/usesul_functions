#!/usr/bin/env python
from __future__ import division
import unittest
import mysql_read_write as mrw
import sys

__author__ = 'youval.dar'


class MysqlReadWritTest(unittest.TestCase):

    def setUp(self):
        # set up connection
        self.config = {
          'user': 'xxx',
          'password': 'xxx',
          'host': '1.1.1.1',
          'database': 'test_db'
        }
        self.tb_name = 'test'


    def test_insert_data_to_sql(self):
        print sys._getframe().f_code.co_name
        col_names = ('date_hour','cnt','ave_mos')
        data = [('test',2,3),('the',5,6),('insert',8,9),('now',80,19)]
        obj = mrw.MysqlReadWrite(connection_config=self.config, tb_name=self.tb_name)
        obj.push_data_to_mysql(col_names=col_names,data=data)


    def test_read_data_from_sql(self):
        print sys._getframe().f_code.co_name
        col_names = ['date_hour','cnt','ave_mos']
        obj = mrw.MysqlReadWrite(connection_config=self.config, tb_name=self.tb_name)
        (data, tb_desc) = obj.read_data_to_list()
        self.assertEqual(col_names,tb_desc)
        self.assertEqual(len(data),4)
        self.assertEqual(len(data[0]),3)



def run_selected_tests():
    """  Run selected tests

  1) List in "tests" the names of the particular test you want to run
  2) Comment out unittest.main()
  3) Un-comment unittest.TextTestRunner().run(run_selected_tests())
  """
    tests = ['test_insert_data_to_sql']
    suite = unittest.TestSuite(map(MysqlReadWritTest,tests))
    return suite


if __name__ == '__main__':
    # use for individual tests
    # unittest.TextTestRunner().run(run_selected_tests())

    # Use to run all tests
    unittest.main()
