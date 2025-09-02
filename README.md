# DysCord

This is a powerful, fully modular Discord bot designed to automate voice channel moderation and provide deep server insights. It enforces camera usage in designated voice channels through escalating punishments and offers detailed analytics, all managed through a clean, interactive button menu. Built on a fully asynchronous architecture with persistent data storage, it ensures robust and reliable server management.

[Key Features](https://github.com/EolnMsuk/DysCord#-key-features) -> [Command List](https://github.com/EolnMsuk/DysCord#-command-list) -> [How to Setup](https://github.com/EolnMsuk/DysCord#%EF%B8%8F-setup--configuration)

-----

## ✨ Key Features

### 🛡️ Automated Voice Channel Moderation

  * **Camera Enforcement**: Automatically mutes/deafens users who join moderated voice channels without their camera on.
  * **Escalating Punishments**: Applies a sequence of punishments for users who repeatedly fail to enable their camera within a configurable time limit: first, a move to a "punishment" VC; then a short timeout; and finally, a longer timeout for subsequent violations.
  * **Admin Immunity**: Bot owners are immune to automated moderation actions.

### 📊 Persistent State & Analytics

  * **State Persistence**: All critical data—analytics, user violations, active timeouts, and event history—is saved to `data.json` and reloaded on startup, ensuring no data is lost after a crash or restart.
  * **VC Time Tracking**: Tracks the cumulative time users spend in moderated voice channels, with leaderboards available via the `!times` command.
  * **Daily Auto-Stats**: Posts a full analytics report daily at a configured UTC time, then automatically clears all statistics for the next day.

### ⚙️ Server Management & Utilities

  * **Interactive Menus**: Core user commands are accessible through a persistent button menu that periodically refreshes, keeping the command channel clean.
  * **Media-Only Channels**: Can be configured to enforce rules in specific channels by automatically deleting any messages that do not contain an image, video, or link.
  * **Comprehensive Logging**: Utilizes `loguru` for detailed, color-coded logs of all commands, moderation actions, and server events, which are automatically saved to `bot.log`.

### 🔔 Comprehensive Event Notifications

The bot keeps administrators informed with a robust, event-driven notification system. It uses rich, detailed embeds to provide real-time updates for all significant server activities:

  * **Member Activity**: Joins, Leaves (batched for mass departures), Kicks, Bans, and Unbans.
  * **Moderation Actions**: Timeouts Added/Removed and Role Changes.
  * **Bot Status**: Sends a notification when the bot comes online.

-----

## 📋 Command List

### 👤 User Commands

*(Requires being in the Streaming VC with camera on)*

  * `!info` / `!about`: Shows server information and rules.
  * `!rules`: Displays the server rules.
  * `!times`: Shows the top 10 most active VC users by time.

### 🛡️ Admin Commands

*(Requires Admin Role or being an Allowed User + Camera On)*

  * `!help`: Sends the interactive help menu.
  * `!bans` / `!banned`: Lists all banned users in the server.
  * `!timeouts`: Shows currently timed-out users.
  * `!rtimeouts`: Removes all active timeouts from users.
  * `!display <user>`: Shows a detailed profile for a user.
  * `!commands`: Shows this list of all commands.

### 👑 Owner Commands (Allowed Users Only)

*(No channel or VC restrictions)*

  * `!purge <count>`: Deletes a specified number of messages.
  * `!hush`: Server-mutes all non-admin users in the Streaming VC.
  * `!rhush` / `!removehush`: Removes server-mutes.
  * `!secret`: Server-mutes and deafens all non-admin users.
  * `!rsecret` / `!removesecret`: Removes mutes and deafens.
  * `!modon` / `!modoff`: Toggles the automated VC camera moderation.
  * `!disablenotifications` / `!enablenotifications`: Toggles join/leave/ban event notifications.
  * `!disable <user>`: Prevents a user from using any bot commands.
  * `!enable <user>`: Re-enables a command-disabled user.
  * `!ban <user>`: Interactively bans one or more users.
  * `!unban <user_id>`: Interactively unbans one or more users by their ID.
  * `!unbanall`: Interactively unbans every user from the server.
  * `!top`: Lists the top 10 oldest server members and oldest Discord accounts.
  * `!roles`: Lists all server roles and their members.
  * `!admin` / `!owner`: Lists all configured bot owners and admins.
  * `!whois`: Shows a 24-hour report of all server activity (joins, leaves, bans, etc.).
  * `!stats`: Shows a detailed analytics report of command usage and VC violations.
  * `!join`: DMs a join invite to all users with a configured admin role.
  * `!clearstats`: Clears all statistical data (VC times, command usage).
  * `!clearwhois`: Clears all historical event data (joins, leaves, bans).
  * `!shutdown`: Safely saves all data and shuts down the bot.

-----

## ⚙️ Setup & Configuration

### 1\. Prerequisites

  * **Python 3.9+**: Install from [python.org](https://www.python.org/downloads/). Make sure to check **"Add Python to PATH"** during installation.
  * **Dependencies**: Open a terminal or command prompt, then run the following command:
    ```
    pip install discord.py python-dotenv loguru
    ```

### 2\. Create a Discord Bot

1.  Navigate to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
2.  Go to the **"Bot"** tab and enable the following **Privileged Gateway Intents**:
      * ✅ **Message Content Intent**
      * ✅ **Server Members Intent**
3.  Click **"Reset Token"** to reveal your bot's token. **Copy this value immediately and store it securely.**
4.  Go to the **"OAuth2" -\> "URL Generator"** tab. Select the `bot` and `applications.commands` scopes.
5.  In the "Bot Permissions" section below, select `Administrator`.
6.  Copy the generated URL and use it to invite the bot to your server.

### 3\. File Setup

1.  Create a folder for your bot and place the Python files (`bot.py`, `helper.py`, `tools.py`) inside.
2.  Create a new file named `.env` in the same folder.
3.  Open the `.env` file and add your Discord bot token. Replace the placeholder text with the actual token you copied.
    ```env
    # .env file
    BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
    ```

### 4\. Configure `config.py`

Open `config.py` and replace the placeholder values with your server's specific IDs and settings. To get IDs, enable Developer Mode in Discord (User Settings -\> Advanced), then right-click a server, channel, or user and select "Copy ID".

```python
# --- REQUIRED SETTINGS ---
GUILD_ID = 123456789012345678                # Your Discord Server ID
COMMAND_CHANNEL_ID = 123456789012345678      # Channel for bot commands and menus
CHAT_CHANNEL_ID = 123456789012345678         # Channel for join/leave/ban notifications
STREAMING_VC_ID = 123456789012345678         # Main voice channel to moderate
PUNISHMENT_VC_ID = 123456789012345678        # VC where users are moved for a first violation

# --- PERMISSIONS ---
# User IDs with full bot access (immune to moderation, no command restrictions)
ALLOWED_USERS = {123456789012345678, 987654321098765432} 
# Roles that can use admin-level commands (still require camera on)
ADMIN_ROLE_NAME = ["Admin", "Moderator"] 

# --- OPTIONAL FEATURES ---
# (Set to [] to disable)
# A list of additional voice channels to moderate with the same camera rules
ALT_VC_ID = []
# Channel for daily auto-stats reports. If None, uses CHAT_CHANNEL_ID.
AUTO_STATS_CHAN = 123456789012345678
# Channel where only messages with media (images, links) are allowed.
MEDIA_ONLY_CHANNEL_ID = None         
# Enable/disable media-only channel moderation
MOD_MEDIA = True                     
# User IDs to exclude from all stats and leaderboards
STATS_EXCLUDED_USERS = {123456789012345678} 

# --- TIMING & MESSAGES ---
# UTC hour for the daily auto-stats report and data clear (0-23)
AUTO_STATS_HOUR_UTC = 5
# Seconds a user can have their camera off in a moderated VC before punishment
CAMERA_OFF_ALLOWED_TIME = 30
# Timeout duration in seconds for a user's second violation
TIMEOUT_DURATION_SECOND_VIOLATION = 60
# Timeout duration in seconds for a user's third (and subsequent) violations
TIMEOUT_DURATION_THIRD_VIOLATION = 300
# Messages sent by the !info command
INFO_MESSAGES = ["Welcome! Please keep your camera on while in the main voice channel."]
# Message sent by the !join command
JOIN_INVITE_MESSAGE = "An admin has requested your presence in the voice channel!"
```

-----

## Running the Bot

1.  Open your command prompt or terminal.
2.  Navigate to the bot's folder (`cd path/to/your/bot`).
3.  Run the bot using the following command:
    ```
    python bot.py
    ```
4.  The bot will initialize and send an "online" message to your configured chat channel.

### Troubleshooting

  * **Token Error**: Ensure your `.env` file is correctly named (it must be `.env`, not `env.txt`), is in the same folder as `bot.py`, and contains the correct Discord bot token.
  * **Bot Doesn't Respond**: Make sure you have enabled the "Message Content Intent" and "Server Members Intent" in the Discord Developer Portal.
  * **Other Issues**: Check the `bot.log` file created in the bot's folder for detailed error messages.
