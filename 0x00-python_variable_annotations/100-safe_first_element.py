#!/usr/bin/env python3

""" Module for correct duck-typed annotations """

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, Optional[None]]:
    """ Takes a sequence of any and returns any type or none """
    if lst:
        return lst[0]
    else:
        return None
