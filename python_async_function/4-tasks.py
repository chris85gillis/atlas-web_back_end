#!/usr/bin/env python3
"""Asynchronous coroutine that spawns wait_random
n times with the specified max_delay."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds for each call.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
