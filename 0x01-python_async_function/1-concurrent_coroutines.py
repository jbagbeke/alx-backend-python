#!/usr/bin/env python3
"""
Concurrent async function declarations
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Running coroutines n number of times
    """
    async_list = []

    for i in range(n):
        t = "t{}".format(i)
        t = asyncio.create_task(wait_random(max_delay))
        async_list.append(t)

    results = await asyncio.gather(*async_list)
    return results
