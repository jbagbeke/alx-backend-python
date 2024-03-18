#!/usr/bin/env python3
"""
Async Basic Function declarations
"""
import asyncio
from random import randint


async def wait_random(max_delay: int = 10) -> float:
    """
    async function declaration with randint sleep time
    """
    rand_value = randint(0, max_delay)
    await asyncio.sleep(rand_value)
    return rand_value
