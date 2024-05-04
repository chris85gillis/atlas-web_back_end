#!/usr/bin/env python3
""" Collects 10 random numbers using an async
comprehension over async_generator."""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Returns:
        List[float]: List of 10 random numbers.
    """
    return [random_number async for random_number in async_generator()]
