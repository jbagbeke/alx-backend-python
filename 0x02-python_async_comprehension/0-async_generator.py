#!/usr/bin/env python3
"""
Async generator function that
"""
from typing import AsyncGenerator
import asyncio
from random import randint


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Returns a random number between 0 and 10
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield randint(0, 10)
