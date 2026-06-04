# -*- coding: utf-8 -*-
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from database.database import *
from config import *

@Client.on_message(filters.private & filters.incoming)
async def forcesub(c, m):
    if not UPDATE_CHANNEL:
        await m.continue_propagation()
        return
        
    owner = await c.get_users(int(OWNER_ID))
    try:
        user = await c.get_chat_member(UPDATE_CHANNEL, m.from_user.id)
        if user.status == "kicked":
            await m.reply_text("**Yᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ɪɴ Oᴜʀ ᴄʜᴀɴɴᴇʟ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ 😜**", quote=True)
            return
    except UserNotParticipant:
        buttons = [[InlineKeyboardButton(text='Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ 🔖', url=f"https://t.me/{UPDATE_CHANNEL}")]]
        if m.text and 'start' in m.text and len(m.text.split(' ')) > 1:
            try:
                data = m.text.split(' ')[1]
                if '_' in data:
                    chat_id, msg_id = data.split('_')
                    buttons.append([InlineKeyboardButton('🔄 Rᴇғʀᴇsʜ', callback_data=f'refresh+{chat_id}+{msg_id}')])
            except:
                pass
        await m.reply_text(
            f"Hey {m.from_user.mention(style='md')} ʏᴏᴜ ɴᴇᴇᴅ ᴊᴏɪɴ Mʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ᴜsᴇ ᴍᴇ 😉\n\n"
            "__Pʀᴇss ᴛʜᴇ Fᴏʟʟᴏᴡɪɴɢ Bᴜᴛᴛᴏɴ ᴛᴏ ᴊᴏɪɴ Nᴏᴡ 👇__",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
        return
    except Exception as e:
        print(f"Error in forcesub: {e}")
        return
        
    await m.continue_propagation()

@Client.on_callback_query(filters.regex('^refresh'))
async def refresh_cb(c, m):
    if UPDATE_CHANNEL:
        try:
            await c.get_chat_member(UPDATE_CHANNEL, m.from_user.id)
        except UserNotParticipant:
            await m.answer('Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ʏᴇᴛ ᴊᴏɪɴᴇᴅ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ. \nFɪʀsᴛ ᴊᴏɪɴ ᴀɴᴅ ᴛʜᴇɴ ᴘʀᴇss ʀᴇғʀᴇsʜ ʙᴜᴛᴛᴏɴ 🤤', show_alert=True)
            return
        except Exception as e:
            print(f"Error in refresh_cb: {e}")
            return

    _, chat_id, msg_id = m.data.split("+")
    
    source_id = int(DB_CHANNEL_ID) if DB_CHANNEL_ID else int(chat_id)
    msg = await c.get_messages(source_id, int(msg_id))
    
    if not msg or msg.empty:
        await m.answer("🥴 Sᴏʀʀʏ ʙʀᴏ ʏᴏᴜʀ ғɪʟᴇ ᴡᴀs ᴍɪssɪɴɢ", show_alert=True)
        return

    caption = msg.caption.markdown if msg.caption else ""
    data = await get_data(str(m.from_user.id))
    
    if data and data.up_name:
        caption += "\n\n\n**--Uᴘʟᴏᴀᴅᴇʀ Dᴇᴛᴀɪʟs:--**\n\n"
        if chat_id.startswith('-100'):
            channel = await c.get_chat(int(chat_id))
            caption += f"**📢 Cʜᴀɴɴᴇʟ Nᴀᴍᴇ:** __{channel.title}__\n\n"
            if channel.username: caption += f"**🗣 Usᴇʀ Nᴀᴍᴇ:** @{channel.username}\n\n"
        else:
            user = await c.get_users(int(chat_id))
            caption += f"**🍁 Nᴀᴍᴇ:** {user.mention}\n\n"
            if user.username: caption += f"**🖋 Usᴇʀ Nᴀᴍᴇ:** @{user.username}\n\n"

    await msg.copy(m.from_user.id, caption=caption)
    await m.message.delete()
