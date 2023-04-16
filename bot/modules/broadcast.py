from telegram.ext import CommandHandler, Filters

from bot import LOGGER, dispatcher, user_data
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage

def broadcast_messages(update, context):
    reply_to = update.message.reply_to_message
    success = 0
    failed = 0
    for id_ in user_data.keys():
        try:
            context.bot.copy_message(chat_id=id_, from_chat_id=update.message.chat.id, message_id=reply_to.message_id)
            success += 1
        except Exception as err:
            LOGGER.error(err)
            failed += 1
    total_users = success + failed
    msg = f"<b>Broadcasting Complete</b>\n"
    msg += f"<b>\nTotal Users: </b>{total_users}"
    msg += f"<b>\nSucessful: </b>{success}"
    msg += f"<b>\nFailed: </b>{failed}"
    return sendMessage(msg, context.bot, update.message) 

broadcast_messages = CommandHandler("broadcast", broadcast_messages, filters=CustomFilters.owner_filter)
dispatcher.add_handler(broadcast_messages)
