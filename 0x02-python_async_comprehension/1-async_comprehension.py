#!/usr/bin/env python3

""" Module for async comprehention """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Creates a list of 10 int number from a generator """
    return [x async for x in async_generator()]
