#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments"""

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
