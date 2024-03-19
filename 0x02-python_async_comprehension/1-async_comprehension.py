#!/usr/bin/env python3
"""
Calls async_generator function using async comprehension
"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Uses async comprehension to call async_generator function
    """

    async_list = [i async for i in async_generator()]
    return async_list
