#!/usr/bin/env python3
"""
Takes a list of mixed data types and returns a sum as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the ints and floats as a float
    """

    return sum(mxd_lst)
