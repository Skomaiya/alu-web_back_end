#!/usr/bin/env python3
"""
This script defines an async routine `wait_n` that spawns `wait_random`
n times and returns a sorted list of delays.
"""

from typing import List
from wait_random import wait_random
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` n times with the specified max_delay and returns
    a list of delays in ascending order.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay in seconds for each `wait_random`.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = []
    for delay in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delays.append(await delay)
    return delays
