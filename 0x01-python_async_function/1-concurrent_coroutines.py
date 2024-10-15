#!/usr/bin/env python3
'''async routine called wait_n that takes in 2 int 
arguments (in this order): n and max_delay'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
    '''takes in 2 int arguments n and max_delay
       and return the list of all the delays'''
    tasks = [asyncio.create_task(wait_random(max_delay=max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
