#!/usr/bin/env python3

""" Module for more type annotations """

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """ Takes a sequence of any and returns any type or none """
    if key in dct:
        return dct[key]
    else:
        return default
