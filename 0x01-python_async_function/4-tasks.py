#!/usr/bin/env python3
'''Tasks'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''takes in 2 int arguments n and max_delay
       and return the list of all the delays'''
    tasks = [task_wait_random(max_delay=max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
