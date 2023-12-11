#!/usr/bin/env python3

"""
basics of async
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
