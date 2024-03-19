#!/usr/bin/env python3
"""
Returns an Asyncio.Task of function from task 0
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns asyncio.Task of wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
