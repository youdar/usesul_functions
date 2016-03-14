#!/usr/bin/python
from __future__ import division
from math import pow

__author__ = 'youval.dar'

def ip2int(ip_str):
    """
    Convert XXX.XXX.XXX.XXX to integer representation

    Args:
        ip_str (str): IP in a XXX.XXX.XXX.XXX string format

    Returns:
        ip_int (int): Integer IP representation
    """
    ip_int = None
    if isinstance(ip_str,str):
        # clean IP
        if ip_str.find(':') > 0:
            ip_str = ip_str[:ip_str.index(':')]
        octet = [int(x.strip()) for x in ip_str.split('.')]
        ip_int = octet[0] * pow(256,3) + octet[1] * pow(256,2) + octet[2] * 256 + octet[3]
    return ip_int


def int2ip(ip_int):
    """
    Convert integer to XXX.XXX.XXX.XXX representation

    Args:
        ip_int (int): Integer IP representation

    Returns:
        ip_str (str): IP in a XXX.XXX.XXX.XXX string format
    """
    ip_str = None
    if isinstance(ip_int,int):
        octet = [0,0,0,0]
        octet[0] = ip_int // pow(256,3)
        ip_int -= octet[0] * pow(256,3)
        octet[1] = ip_int // pow(256,2)
        ip_int -= octet[1] * pow(256,2)
        octet[2] = ip_int // 256
        ip_int -= octet[2] * 256
        octet[3] = ip_int
        octet = map(int,octet)
        octet = map(str,octet)
        ip_str = '.'.join(octet)
    return ip_str


def ip_range_expand(ip_str):
    """
    Convert Classless Inter-Domain Routing (CIDR) format, XXX.XXX.XXX.XXX/XX to
    ip_start and ip_end

    IP CIDR is an expansion of the IP addressing system that allows for a more efficient and appropriate
    allocation of addresses. CIDR changed fixed fields into variable-length fields, allowing addresses
    to be assigned with more granularity. The CIDR IP address includes a number that tells how the address
    is split between networks and hosts. For example, in the CIDR address 209.173.53.167/20 the /20 indicates
    that the first 20 bits are used for network ID and the remaining 12 (there are 32 bits in the IP address)
    are used for host ID.

    Args:

    Returns:
        ip_start (str):
        ip_end (str)
    """
    ip_start = None
    ip_end = None
    if isinstance(ip_str,str):
        # Todo: Finish function
        ip_start = 'xxx'
        ip_end = 'xxx'
    return ip_start, ip_end