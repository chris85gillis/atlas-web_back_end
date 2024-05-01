#!/usr/bin/env python3
""" Measures the total execution time for wait_n(n, max_delay),
and returns total_time / n."""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds for each call.

    Returns:
        float: The average execution time per call.
    """
    startTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endTime = time.time()
    total_time = endTime - startTime
    return (total_time / n)
