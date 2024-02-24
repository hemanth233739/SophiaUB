from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from pyrogram import enums

@Sophia.on_message(filters.command("broadcastall", prefixes=HANDLER) & filters.user(OWNER_ID))
async def broadcast_all(_, message):
    SUCCESS = 0
    FAILED = 0
    if message.reply_to_message:
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT:
                try:
                    await Sophia.forward_messages(dialog.chat.id, message.chat.id, message.reply_to_message_id)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Broadcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("➲ Master, Please enter a text to broadcast or reply a message to broadcast.")
        text = message.text.split(None, 1)[1]
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT:
                try:
                    await Sophia.send_message(dialog.chat.id, text)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Broadcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")