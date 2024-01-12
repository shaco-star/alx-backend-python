#!/usr/bin/env python3

"""
basics of async
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """

    Args:
        max_delay:

    Returns: wait time less than max_delay

    """
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
