import asyncio

import aiohttp


async def main():
    s=aiohttp.ClientSession(cookies={"adf":"srgdtrerts"})
    c=s.cookie_jar.filter_cookies()
    print(s.cookie_jar)

asyncio.run(main())
