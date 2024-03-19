#!/usr/bin/env python3
"""
Measures time it takes for function execution
"""
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures execution time for wait_n function
    """

    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()

    return ((end_time - start_time) / n)
