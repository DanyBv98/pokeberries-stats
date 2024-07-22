import asyncio
from typing import Any

import aiohttp


async def fetch_json(url: str) -> Any:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_paginated_json(url: str) -> Any:
    results = []

    next_page_url = url
    while next_page_url:
        response = await fetch_json(next_page_url)
        results += response['results']
        next_page_url = response['next']

    return results

async def fetch_multiple_json(urls: list[str]) -> list[Any]:
    """
        Creates concurrent requests to fetch JSON for all of the provided URLs
        and adds all the results in a list which is returned.
    """
    return await asyncio.gather(*[fetch_json(url) for url in urls])
