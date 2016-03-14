#!/usr/bin/env python
from __future__ import division
import dateutil.relativedelta as dr
import datetime
import pytz
import sys

__author__ = 'youval.dar'

__doc__ = """
Calculate the date and time less_n_days ago or less_n_hours ago
"""


def get_back_date_time(less_n_days=None,less_n_hours=None,less_n_months=None, less_n_minutes=None):
    """
    Calculate the date and time less_n_days ago or less_n_hours ago or less_months ago

    Args:
        less_n_days (int): number of days
        less_n_hours (int): number of hours
        less_n_months (int): number of months
        less_n_minutes (int): number of minutes

    Returns:
        dt (str): 'YYYY-MM-DD:HH:MM:00' the date and hour of time less_n_days ago or less_n_hours ago,
                  in UTC time, 24 hours format
    """
    t = sum([less_n_hours != None,less_n_days != None,less_n_months != None, less_n_minutes != None])
    if t != 1 :
        print >> sys.stderr, "\nOne and only one parameter should be provided !!!\n"
        exit(0)
    if less_n_hours != None:
        # use hours to count back
        start_date_time = datetime.datetime.now() - dr.relativedelta(hours=abs(less_n_hours))
    elif less_n_days != None:
        # use days to count back
        start_date_time = datetime.datetime.now() - dr.relativedelta(days=abs(less_n_days))
    elif less_n_minutes != None:
        # use days to count back
        start_date_time = datetime.datetime.now() - dr.relativedelta(minutes=abs(less_n_minutes))
    else:
        # use days to count back
        start_date_time = datetime.datetime.now() - dr.relativedelta(months=abs(less_n_months))
    # adjust to UTC
    start_date_time.replace(tzinfo=pytz.utc)
    # format to YYYY-MM-DD:HH
    start_date_time = start_date_time.strftime("%Y-%m-%d:%H:%M:00")
    return start_date_time

