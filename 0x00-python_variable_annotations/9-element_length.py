#!/usr/bin/env python3
"""
Annoatates an already written function
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuple
    """

    return [(i, len(i)) for i in lst]
