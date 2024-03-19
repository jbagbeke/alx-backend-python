#!/usr/bin/env python3
"""
Returns an Asyncio.Task of function from task 0
"""
import asyncio
from typing import IO
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> IO:
    """
    Returns asyncio.Task of wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
