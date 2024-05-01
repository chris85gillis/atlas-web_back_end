#!/usr/bin/env python3
"""Creates an asyncio.Task for the wait_random coroutine."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns a asyncio.Task.

    Args:
        max_delay (int): The maximum delay in seconds for the wait_random coroutine.

    Returns:
        asyncio.Task: Task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
