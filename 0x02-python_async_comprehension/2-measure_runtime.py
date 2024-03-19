#!/usr/bin/env python3
"""
Time measure four asynchronous processes
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> time:
    """
    Measures execution time for four async functions
    """

    async_list = [async_comprehension(),
                  async_comprehension(),
                  async_comprehension(),
                  async_comprehension()]
    async_batches = asyncio.gather(*async_list)

    start_time = time()
    await async_batches
    end_time = time()

    return (end_time - start_time)
