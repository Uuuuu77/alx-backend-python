#!/usr/bin/env python3

""" Module for complex types of string to float or int """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return a tuple of string and square of int or float """
    return k, float(v ** 2)
