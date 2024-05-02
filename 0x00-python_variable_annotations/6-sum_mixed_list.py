#!/usr/bin/env python3

""" Module for mixed list of integer and floats """

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns summ of list of ints and float """
    return sum(mxd_list)
