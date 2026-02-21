#!/usr/bin/env python3
"""Module that provides an async coroutine for random delays."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return it.

    Args:
        max_delay: Maximum delay in seconds (default 10)

    Returns:
        The random delay value as a float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
