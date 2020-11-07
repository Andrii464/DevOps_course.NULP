import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def rangenum(XXL):

    if XXL:
        j = 0
    else:
        j = 1
    for i in range(j,101,2):
        print(i)
