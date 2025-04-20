from os import getenv

API_ID = int(getenv("API_ID", "22642292"))
API_HASH = getenv("API_HASH", "4502d35191a2fcb02c8467f54789f0ea")
BOT_TOKEN = getenv("BOT_TOKEN", "") # Make sure this token is valid and the bot is active
OWNER_ID = list(map(int, getenv("OWNER_ID", "922270982").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sophiapartpwrggwgalloway:6sRSl1EyieTvAOG9@cluster0.rllqp.mongodb.net/?retryWrites=true&w=majority")

# Fix channel IDs that have incorrect format
def fix_channel_id(channel_id):
    # Convert to string first
    channel_id = str(channel_id)
    # Fix the format for channel IDs that start with -1002... to -100...
    if channel_id.startswith('-1002'):
        return '-100' + channel_id[5:]
    return channel_id

# Original: "-1002230414810" -> Fixed: "-100230414810"
LOG_GROUP = fix_channel_id(getenv("LOG_GROUP", "-1002230414810"))
# Original: "-1002304203111" -> Fixed: "-100304203111" 
CHANNEL_ID = int(fix_channel_id(getenv("CHANNEL_ID", "-1002304203111")))

FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "20"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000000000"))

#AutoDeleteTime
SECONDS = int(getenv("SECONDS", "300"))