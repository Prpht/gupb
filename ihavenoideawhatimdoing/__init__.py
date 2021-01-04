import asyncio
import os
import selectors

selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
