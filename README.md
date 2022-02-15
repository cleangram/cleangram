[![Pypi](https://img.shields.io/pypi/v/cleangram?style=flat-square)](https://pypi.org/project/cleangram/)
[![Telegram Bot API](https://img.shields.io/badge/Bot%20API-5.7-blue?logo=telegram&style=flat-square)](https://core.telegram.org/bots/api)
[![Channel](https://img.shields.io/badge/dynamic/xml?color=blue&label=Channel&query=.%2F%2F*[%40class%3D%27tgme_page_extra%27]&url=https%3A%2F%2Ft.me%2Fcleangram&logo=telegram&link=https://t.me/cleangram&style=flat-square)](https://t.me/+_IGqbnmF5fZmZDky)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
# Cleangram

## Getting Started

```commandline
pip install cleangram
```

### Echo bot

```python
from cleangram import App, Bot, Message, env

tg = App()


@tg.message()
async def echo(msg: Message, bot: Bot):
    await bot.send_message(msg.chat.id, msg.text)


tg.polling.run(env.TELEGRAM_BOT_TOKEN)
```
