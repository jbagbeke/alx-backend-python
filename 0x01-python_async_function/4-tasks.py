#!/usr/bin/env python3
"""
Concurrent async function declarations
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Running coroutines n number of times
    """
    async_list = []
    sort_tasks = []

    for _ in range(n):
        async_list.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(async_list):
        delay = await task
        sort_tasks.append(float(delay))

    return (sort_tasks)
