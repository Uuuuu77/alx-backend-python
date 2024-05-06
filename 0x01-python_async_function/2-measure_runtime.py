#!/usr/bin/env python3

""" Module for measuring the runtime """

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Computes & returns average runtime to execute """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time
    return elapsed_time / n
