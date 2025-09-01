# config.py
# This file contains all the configuration variables for your Discord bot.
# Make sure to fill in all the required values before running the bot.

# ==============================================================================
# REQUIRED SETTINGS
# You MUST fill these out for the bot to start. The bot will not launch
# without valid IDs in this section.
# ==============================================================================

# To get IDs in Discord, you need to enable Developer Mode.
# Go to User Settings > Advanced > Developer Mode (turn it on).
# Then, right-click on a server, channel, or user to get the "Copy ID" option.

# The unique ID of the Discord server (guild) where the bot will operate.
GUILD_ID = 123456789012345678

# The ID of the channel where users should use bot commands.
COMMAND_CHANNEL_ID = 123456789012345678

# The ID of the main channel for bot announcements (joins, leaves, bans, etc.).
CHAT_CHANNEL_ID = 123456789012345678

# The ID of the primary voice channel that will be moderated (camera checks, etc.).
STREAMING_VC_ID = 123456789012345678

# The ID of the voice channel where users are moved for camera-off violations.
PUNISHMENT_VC_ID = 123456789012345678


# ==============================================================================
# OPTIONAL & MODERATION SETTINGS
# These have default values but can be customized to change bot behavior.
# ==============================================================================

# PASTE the IDs (seperated by commas) of any other voice channel where camera rules should also be enforced or leave blank [].
ALT_VC_ID = [123456789012345678, 123443565467765678] 

# A set of user IDs for users who have owner-level permissions for the bot.
# These users bypass all restrictions.
# Example: ALLOWED_USERS = {987654321098765432, 112233445566778899}
ALLOWED_USERS = {}

# A list of role names that grant admin-level permissions for the bot.
# These users can use admin commands but are still subject to camera/channel rules.
# Example: ADMIN_ROLE_NAME = ["Moderator", "Admin"]
ADMIN_ROLE_NAME = []

# The message sent via the !join command to users with an admin role.
JOIN_INVITE_MESSAGE = "You're invited to join the voice chat!"

# The message sent to users when they join the streaming VC.
RULES_MESSAGE = """
## Welcome to the Server!
**Rule 1:** Be respectful to others.
**Rule 2:** Keep your camera on in the streaming voice channel.
**Rule 3:** No hateful or inappropriate content.
"""

# A list of messages sent when a user uses the !info command.
INFO_MESSAGES = [
"""
This is an automated moderation bot.
Please follow the rules outlined in the `!rules` command.
"""
]

# The grace period (in seconds) a user has to turn on their camera after joining a VC.
CAMERA_OFF_ALLOWED_TIME = 30

# The duration (in seconds) of the timeout for a user's second camera-off violation.
TIMEOUT_DURATION_SECOND_VIOLATION = 60

# The duration (in seconds) of the timeout for a user's third (and subsequent) camera-off violation.
TIMEOUT_DURATION_THIRD_VIOLATION = 300

# A set of user IDs to exclude from all statistical tracking (!stats, !times).
# Example: STATS_EXCLUDED_USERS = {987654321098765432}
STATS_EXCLUDED_USERS = {}

# The channel ID where daily stats reports are automatically posted.
# If set to None, it will default to CHAT_CHANNEL_ID.
AUTO_STATS_CHAN = None  # Example: 123456789012345678 or None

# The time (in UTC) for the daily automatic stats report and reset.
AUTO_STATS_HOUR_UTC = 5  # 5 AM UTC
AUTO_STATS_MINUTE_UTC = 0

# The ID of a channel where only media (images, videos, links) is allowed.
# If MOD_MEDIA is True, messages without media will be deleted.
MEDIA_ONLY_CHANNEL_ID = None # Example: 123456789012345678 or None
MOD_MEDIA = True

