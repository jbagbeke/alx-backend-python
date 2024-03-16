#!/usr/bin/env python3
"""
Type annotation of function
"""
from typing import Union, TypeVar, Mapping, Any


T = TypeVar('T')
un1 = Union[T, None]
un2 = Union[Any, T]
mp = Mapping


def safely_get_value(dct: mp, key: Any, default: un1 = None) -> un2:
    """
    Adding type annotaions to function
    """

    if key in dct:
        return dct[key]
    else:
        return default
