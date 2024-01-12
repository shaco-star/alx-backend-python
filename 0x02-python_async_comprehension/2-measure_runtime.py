#!/usr/bin/env python3

"""
Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute
async_comprehension four times in parallel
using asyncio.gather.

"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """

    Returns:  total runtime

    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
