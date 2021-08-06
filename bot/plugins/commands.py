#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⭕ OUR CHANNEL LINKS ⭕', url="https://t.me/MovieHouse_Linkz"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⭕ OUR CHANNEL LINKS ⭕', url="https://t.me/MovieHouse_Linkz"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⭕ OUR CHANNEL LINKS ⭕', url="https://t.me/MovieHouse_Linkz"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

 buttons = [[
        InlineKeyboardButton('👥 𝐆𝐑𝐎𝐔𝐏 - 𝟏', url='https://t.me/Movie_House_1'),
        InlineKeyboardButton('𝐆𝐑𝐎𝐔𝐏 - 𝟐 👥', url ='https://t.me/Movie_House_Group_2')
    ],[
        InlineKeyboardButton('⭕ 𝐎𝐔𝐑 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐋𝐈𝐍𝐊𝐒 ⭕', url='https://t.me/MovieHouse_Linkz')
    ],[
        InlineKeyboardButton('🖥️ 𝐍𝐄𝐖 𝐎𝐓𝐓 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 🖥️', url='https://t.me/NewDvdUpdatesKerala')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_sticker(sticker="CAACAgEAAxkBAAJEemDQhN67WfA0jR_5ftZStaRMR20YAALKAAN-3IBGwOBvi-NZUuMeBA")


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_sticker(sticker="CAACAgEAAxkBAAJEemDQhN67WfA0jR_5ftZStaRMR20YAALKAAN-3IBGwOBvi-NZUuMeBA")
