#!/usr/bin/env python
from __future__ import division
import sys
import csv

__author__ = 'youval.dar'

"""
Split string by ',' ignoring comma that are enclosed in parentheses
"""


def run(string=''):
    if not string:
        string = '"29975552","29976063","asia","korea, (south)","kr","99","","seoul teukbyeolsi","","94","seoul","89"'
    m = csv.reader([string]).next()
    print len(m)
    print m


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        run(args[0])
    else:
        run()