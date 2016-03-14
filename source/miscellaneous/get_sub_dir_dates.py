#!/usr/bin/env python
from __future__ import division
import sys
import os
import re

__author__ = 'youval.dar'



def get_sub_dir_dates(main_folder):
    """
    Get a list of dates in the format YYYY-MM-DD, for subdirectories of a table
    partitioned by dt, so that directories names are "dt=YYYY-MM-DD"

    Args:
        main_folder (str): path to look at

    Returns:
        dates (set):  {'YYYY-MM-DD',...}
    """
    # remove leading "hdfs://nameservice1"
    if main_folder.startswith('hdfs://nameservice1'):
        main_folder = main_folder[19:]
    ls_com = 'hdfs dfs -ls ' + main_folder
    dates =set()
    # Filter collect folders to delete
    d = '=([0-9]{4}-[0-9]{2}-[0-9]{2})'
    for x in os.popen(ls_com):
        x = x.strip()
        m = re.search(d,x)
        if bool(m):
            dt = m.group(1)
            dates.add(dt)
    return dates

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        get_folder_ls(args[0])