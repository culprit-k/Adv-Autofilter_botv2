#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from pyrogram import filters

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID"))

API_HASH = os.environ.get("API_HASH")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DB_URI = os.environ.get("DB_URI")

USER_SESSION = os.environ.get("USER_SESSION")

AUTH_CHANNEL = int(os.environ.get('AUTH_CHANNEL', '0'))

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

async def is_joined(_, client, update):
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False

    if not file_uid:
        return True

    if not AUTH_CHANNEL:
        return True
    try:
        user_id = update.from_user.id
    except:
        return False
    try:
        chat_member = await client.get_chat_member(
            chat_id = AUTH_CHANNEL,
            user_id = user_id
        )
    except:
        return False

    if chat_member.status in ['left', 'kicked']:
        return False
    else:
        return True

filters.joined = filters.create(is_joined)
