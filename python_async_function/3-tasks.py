#!/usr/bin/env python3
"""Creates an asyncio.Task for the wait_random coroutine."""
import asyncio

wait_random = __import__('2-measure_runtime').wait_runtime


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for the wait_random coroutine.

    Returns:
        asyncio.Task: Task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
