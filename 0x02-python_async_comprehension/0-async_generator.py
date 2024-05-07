#!/usr/bin/env python3

""" Module for writing a coroutine for async generator """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Loop 10 times, each tym wait 1 second, yield random num btwn 0 & 10 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
