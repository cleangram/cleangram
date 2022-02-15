from typing import Tuple

from cleangram.types import Update, TelegramType


def get_event_and_type(update: Update) -> Tuple[TelegramType, str]:
    if message := update.message:
        return message, "message"
    elif edited_message := update.edited_message:
        return edited_message, "edited_message"
    elif channel_post := update.channel_post:
        return channel_post, "channel_post"
    elif edited_channel_post := update.edited_channel_post:
        return edited_channel_post, "edited_channel_post"
    elif inline_query := update.inline_query:
        return inline_query, "inline_query"
    elif chosen_inline_result := update.chosen_inline_result:
        return chosen_inline_result, "chosen_inline_result"
    elif callback_query := update.callback_query:
        return callback_query, "callback_query"
    elif shipping_query := update.shipping_query:
        return shipping_query, "shipping_query"
    elif pre_checkout_query := update.pre_checkout_query:
        return pre_checkout_query, "pre_checkout_query"
    elif poll := update.poll:
        return poll, "poll"
    elif poll_answer := update.poll_answer:
        return poll_answer, "poll_answer"
    elif my_chat_member := update.my_chat_member:
        return my_chat_member, "my_chat_member"
    elif chat_member := update.chat_member:
        return chat_member, "chat_member"
    elif chat_join_request := update.chat_join_request:
        return chat_join_request, "chat_join_request"
    raise NameError("Update event not found")
