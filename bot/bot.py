#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @SpEcHIDe

import sys
from pyrogram import Client, __version__

from . import API_HASH, APP_ID, LOGGER, BOT_TOKEN, AUTH_CHANNEL

from .user import User

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "bot/plugins"
            },
            workers=4,
            bot_token=BOT_TOKEN,
            sleep_threshold=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        
        if AUTH_CHANNEL:
            try:
                link = await self.export_chat_invite_link(AUTH_CHANNEL)
                self.invitelink = link
            except Exception as a:
                print(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning("Please Double check the AUTH_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission")
                sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  started! "
        )
        self.username = bot_details.username
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
