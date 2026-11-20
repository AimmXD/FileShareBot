from typing import Union
from pyrogram.types import Message, CallbackQuery
import config

def is_admin(update: Union[Message, CallbackQuery]) -> bool:
    """
    Check if the user is an admin.
    Works with both Message and CallbackQuery objects.
    
    Args:
        update: The Message or CallbackQuery object to check
        
    Returns:
        bool: True if user is admin, False otherwise
    """
    user_id = (
        update.from_user.id if isinstance(update, Message)
        else update.message.from_user.id
    )
    return user_id in config.ADMIN_IDS
