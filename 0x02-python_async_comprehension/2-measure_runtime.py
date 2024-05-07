#!/usr/bin/env python3

""" Module to measure the total runtime and return it """

from time import time
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Execute four times in parallel to measure runtime """
    start_time = time()
    await gather(*(async_comprehension() for _ in range(4)))
    run_time = time() - start_time

    return run_time
