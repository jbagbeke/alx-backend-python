#!/usr/bin/env python3
"""
Concurrent async function declarations
"""
import asyncio
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Running coroutines n number of times
    """
    async_list = []
    sort_tasks = []

    for _ in range(n):
        async_list.append(wait_random(max_delay))
    
    for task in asyncio.as_completed(async_list):
        sort_tasks.append(await task)

    return (sort_tasks)
