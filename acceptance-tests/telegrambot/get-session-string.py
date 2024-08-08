# Run this script to get the session string of a desired telegram client instance.

from urllib.parse import urlparse

import socks
from dotenv import dotenv_values
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = int(input("Your API ID: "))
api_hash = input("Your API hash: ")

proxy_url = dotenv_values().get('CRUSHBACK_TELEGRAM_PROXY_URL')
proxy = None
if proxy_url is not None:
    u = urlparse(proxy_url)
    proxy = (socks.PROXY_TYPE_SOCKS5, u.hostname, u.port or 80)
with TelegramClient(StringSession(), api_id, api_hash, proxy=proxy) as client:
    print("Session string:", client.session.save())
