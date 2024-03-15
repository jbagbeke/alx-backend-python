#!/usr/bin/env python3
"""
Type annotated function
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    Returns a tuple of the string and the sqaure of v as float
    """

    return k, v**v
