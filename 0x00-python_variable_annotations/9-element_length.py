#!/usr/bin/env python3

""" Module for an iterable object """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Takes list with sequence and return a tuple of sequence and int """
    return [(x, len(x)) for x in lst]
