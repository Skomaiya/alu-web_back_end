#!/usr/bin/env python3
"""
This script defines an asynchronous function `wait_random` that waits for
a random delay and returns the delay value.

Functions:
    wait_random(max_delay): Returns a random float value up to max_delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive) and returns the delay.

    Args:
        max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay value.
    """
    result = random.uniform(0, max_delay)
    await asyncio.sleep(result)
    return result
