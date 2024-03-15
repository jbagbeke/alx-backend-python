#!/usr/bin/env python3
"""
Returns a callable function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiples float by another
    """

    def myFunction(otherValue: float) -> float:
        return multiplier * otherValue

    return myFunction