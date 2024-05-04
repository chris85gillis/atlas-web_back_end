#!/usr/bin/env python3
"""Executes async_comprehension four times in parallel
using asyncio.gather and measures the total runtime."""
import asyncio
import time
from typing import List
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Returns:
        float: Total runtime.
    """
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    total_time = time.time() - start_time
    return total_time
