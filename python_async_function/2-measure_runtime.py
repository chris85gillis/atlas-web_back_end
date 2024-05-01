#!/usr/bin/env python3
""" Measures the total execution time for wait_n(n, max_delay),
and returns total_time / n."""
import time
from typing import List
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds for each call.

    Returns:
        float: The average execution time per call.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(run(measure_time(n, max_delay)))
    