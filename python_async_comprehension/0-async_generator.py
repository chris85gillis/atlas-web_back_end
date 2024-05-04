#!/usr/bin/env python3
"""Asynchronous generator that yields a random number 
between 0 and 10 after waiting for 1 second."""
import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields a random number 
    between 0 and 10 after waiting for 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
