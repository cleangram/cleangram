import asyncio
import logging

from cleangram.client import Bot


log = logging.getLogger(__name__)


class Polling:
    def __init__(self, app):
        self.app = app
        self._running = False

    async def start(self):
        log.info("Starting")

        self._running = True
        offset = 0
        async with Bot(self.app.tokens[0]) as bot:
            while self._running:
                updates = await bot.get_updates(offset=offset, timeout=3)
                if updates:
                    ids = [u.update_id for u in updates]
                    offset = max(ids) + 1
                    await asyncio.gather(
                        *[self.app.notify(update, bot) for update in updates]
                    )
                await asyncio.sleep(0.5)

    def run(self):
        try:
            asyncio.run(self.start())
        except (KeyboardInterrupt, SystemExit):
            logging.info("Shutdown")
