from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/dc103135bd01a862db962.png")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/dc103135bd01a862db962.png")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GeezRam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/UserbotCh")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1413768944").split()))


FAILED = "https://telegra.ph/file/dc103135bd01a862db962.png"
