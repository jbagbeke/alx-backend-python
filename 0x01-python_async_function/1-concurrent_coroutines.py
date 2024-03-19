#!/usr/bin/env python3
"""
Concurrent async function declarations
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Running coroutines n number of times
    """
    async_list = []
    sort_tasks = []

    for i in range(n):
        delay_task = wait_random(max_delay)
        async_list.append(delay_task)

    for task in asyncio.as_completed((async_list)):
        async_task = await task
        sort_tasks.append(async_task)

    return (sort_tasks)
