
from .config import (
    BOT_TOKEN,
    API_ID,
    API_HASH,
    MONGO_URI,
    DATABASE_NAME,
    ADMIN_IDS,
    DB_CHANNEL_ID,
    BOT_USERNAME,
    BOT_NAME,
    BOT_VERSION,
    CHANNEL_LINK,
    DEVELOPER_LINK,
    Messages,
    Buttons
)

from .database import Database
from . import utils
from . import handlers

__version__ = '1.2'

__all__ = [
    'BOT_TOKEN',
    'API_ID',
    'API_HASH',
    'MONGO_URI',
    'DATABASE_NAME',
    'ADMIN_IDS',
    'DB_CHANNEL_ID',
    'BOT_USERNAME',
    'BOT_NAME',
    'BOT_VERSION',
    'CHANNEL_LINK',
    'DEVELOPER_LINK',
    'Messages',
    'Buttons',
    'Database',
    'utils',
    'handlers'
]

print(f"Alpha Share Bot v{__version__} Initialized!")
