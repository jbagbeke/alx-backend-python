#!/usr/bin/env python3
"""
Async generator function that
"""
from typing import Generator
import asyncio
from random import randint


async def async_generator() -> Generator[float, None, None]:
    """
    Returns a random number between 0 and 10
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield float(randint(0, 10))
