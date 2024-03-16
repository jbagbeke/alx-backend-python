#!/usr/bin/env python3
"""
Augmenting code with type annotation
"""
from typing import Sequence, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Type annotation of function
    """

    if lst:
        return lst[0]
    else:
        return None
