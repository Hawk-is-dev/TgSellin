import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")
MONGO_URI = os.getenv("MONGO_URI")
# Separate database name inside the same Mongo cluster, so this bot never
# touches another bot's data. Change only if you want a different name.
DATABASE_NAME = os.getenv("DATABASE_NAME", "zerox_otp_bot")
UPI_ID = os.getenv("UPI_ID", "Not Set")
CRYPTO_ADDRESS = os.getenv("CRYPTO_ADDRESS", "Not Set")

def _int_env(name: str):
    """Numeric chat ID from env (e.g. -1001234567890). None if not set."""
    val = (os.getenv(name) or "").strip()
    return int(val) if val.lstrip("-").isdigit() else None


# Force-join channels shown in /start. Only these — the private admin log
# group is NOT in this list.
#   chat : what Telegram checks membership against (@username, or numeric ID
#          for a private channel). None = membership is not checked for it.
#   link : the button users tap to join.
REQUIRED_CHANNELS = [
    # Private channel (invite link) — needs its numeric ID in FORCE_JOIN_PRIVATE_ID
    {"chat": _int_env("FORCE_JOIN_PRIVATE_ID"), "link": "https://t.me/+Gw6-s632_fI5NTQ1"},
    {"chat": "@Logs_4888", "link": "https://t.me/Logs_4888"},
    {"chat": "@ZEROX_8999", "link": "https://t.me/ZEROX_8999"},
]

# Private admin group that receives the detailed sale / OTP logs
# (invite link: https://t.me/+ENqrs28FfjFmYTE1). Bot must be a member/admin there.
# Needs the group's numeric ID. Not set = detailed logs are skipped.
ADMIN_LOG_GROUP_ID = _int_env("ADMIN_LOG_GROUP_ID")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing!")
if not MONGO_URI:
    raise ValueError("MONGO_URI is missing!")
