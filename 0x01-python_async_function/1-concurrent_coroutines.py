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

    for _ in range(n):
        t = await wait_random(max_delay)
        async_list.append(t)
    
    return async_list