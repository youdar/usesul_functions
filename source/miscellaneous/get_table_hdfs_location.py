#!/usr/bin/env python
from __future__ import division
import subprocess
import sys
import re

__author__ = 'youval.dar'

__doc__ = """
Get the HDFS Location of a Hive Table

Example:
$python /home/youval.dar/youval/dev-hadoop-pyspark/source/general_functions/miscellaneous/get_table_hdfs_location.py youval_db.accounts_info_summary
"""


def get_table_hdfs_location(table_name,print_out=True):
    """

    Args:
        table_name (str): Hive table name

    Returns:
        table_path (str): Table data path on HDFS
    """
    path_str = False
    cmd = 'describe formatted %s' % table_name
    # for testing - will produce output for log
    # out_str = subprocess.check_call(['impala-shell','-q',cmd])
    out_str = subprocess.Popen(['impala-shell','-q',cmd],stdout=subprocess.PIPE)
    for x in out_str.stdout:
        p = re.match(r'^ *\| *Location: *\|',x)
        if p:
            path_str = x.split('|')[2].strip()
    out_str.stdout.close()
    if path_str:
        if print_out:
            print >> sys.stdout, '\n' + path_str + '\n'
        else:
            return path_str
    else:
        if print_out:
            print >> sys.stdout, "Could not get path using %s" % cmd
        else:
            return ''


if __name__ == '__main__' :
    args = sys.argv[1:]
    if len(args) != 1:
        print __doc__
    else:
        get_table_hdfs_location(args[0])



