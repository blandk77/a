#!/usr/bin/env python3
from bot.helper.telegram_helper.bot_commands import BotCommands

YT_HELP_MESSAGE = [
    """
    <b>🎥 YouTube & yt-dlp Command Guide</b>
    
    Send links or files along with <i>/{BotCommands.YtdlCommand[0]}</i> or reply to a command to mirror or leech from yt-dlp supported sites to Telegram, Google Drive, or DDLs using engines like RClone or yt-dlp. 🌐
    
    <b>✨ Available Arguments</b>
    <ul>
        <li><b>-n</b> or <b>-name</b>: Rename the file</li>
        <li><b>-z</b> or <b>-zip</b>: Zip files or links (optional password)</li>
        <li><b>-up</b> or <b>-upload</b>: Upload to Google Drive, RClone, or DDL</li>
        <li><b>-b</b> or <b>-bulk</b>: Download multiple links</li>
        <li><b>-i</b>: Download multiple links by replying</li>
        <li><b>-m</b>, <b>-sd</b>, or <b>-samedir</b>: Download multiple links to the same directory</li>
        <li><b>-opt</b> or <b>-options</b>: Add custom yt-dlp options</li>
        <li><b>-s</b> or <b>-select</b>: Select files from yt-dlp links</li>
        <li><b>-rcf</b>: Add RClone flags</li>
        <li><b>-id</b>: Google Drive folder ID or link</li>
        <li><b>-index</b>: Index URL for Google Drive</li>
        <li><b>-c</b> or <b>-category</b>: Select Google Drive category (case insensitive)</li>
        <li><b>-ud</b> or <b>-dump</b>: Select dump chat (name, chat_id, or username)</li>
        <li><b>-ss</b> or <b>-screenshots</b>: Generate screenshots for videos</li>
        <li><b>-t</b> or <b>-thumb</b>: Add custom thumbnail</li>
    </ul>
    """,
    """
    <b>🚀 How to Use</b>
    
    <b>🔗 Send Link with Command</b><br>
    <code>/cmd https://youtube.com/watch?v=xxx -s -n newname -opt format:best</code>
    
    <b>💬 Reply to Link</b><br>
    <code>/cmd -n newname -z password -opt format:best</code>
    
    <b>📝 Rename File</b> (-n or -name)<br>
    <code>/cmd https://example.com/video.mp4 -n newname</code><br>
    <i>Note: Don't include file extension.</i>
    
    <b>📸 Generate Screenshots</b> (-ss or -screenshots)<br>
    <code>/cmd https://example.com/video.mp4 -ss 3</code><br>
    <i>Generates 3 screenshots per video.</i>
    
    <b>🖼️ Custom Thumbnail</b> (-t or -thumb)<br>
    <code>/cmd https://example.com/video.mp4 -t https://telegra.ph/image.jpg</code><br>
    <i>Use Telegram link or direct image URL.</i>
    
    <b>🎚️ Quality Selection</b> (-s or -select)<br>
    <code>/cmd https://youtube.com/watch?v=xxx -s</code><br>
    <i>Select quality even if default is set in yt-dlp options.</i>
    
    <b>📦 Zip Files</b> (-z or -zip)<br>
    <code>/cmd https://example.com/file -z</code><br>
    <code>/cmd https://example.com/file -z secretpass</code>
    
    <b>⚙️ Custom yt-dlp Options</b> (-opt or -options)<br>
    <code>/cmd https://youtube.com/watch?v=xxx -opt playliststart:^10|fragment_retries:^inf</code><br>
    <i>Use ^ before integers/floats. Supports tuples and dicts with double quotes.</i>
    
    <b>🔗 Multi-Links (Reply)</b> (-i)<br>
    <code>/cmd -i 10</code><br>
    <i>Downloads 10 links by replying to the first link.</i>
    
    <b>📂 Same Directory</b> (-m, -sd, or -samedir)<br>
    <code>/cmd -i 10 -m foldername</code>
    
    <b>☁️ Custom Drive Upload</b> (-id & -index)<br>
    <code>/cmd -id drive_folder_link -index https://example.com/0:</code>
    
    <b>🏷️ Category Selection</b> (-c or -category)<br>
    <code>/cmd -c category_name</code><br>
    <i>Works with Bot Categories or UserTDs.</i>
    
    <b>📤 Dump Chat Selection</b> (-ud or -dump)<br>
    <code>/cmd -ud dump_name</code><br>
    <i>Use name, @username, or chat_id. Use -ud all for all dump chats.</i>
    
    <b>⬆️ Upload Options</b> (-up or -upload)<br>
    <code>/cmd https://example.com/file -up rcl</code><br>
    <code>/cmd https://example.com/file -up mrcc:main:dump</code><br>
    <i>Supports rclone, gdrive, or DDL. Use mrcc: for manual config paths.</i>
    
    <b>⚡ RClone Flags</b> (-rcf)<br>
    <code>/cmd https://example.com/file -rcf --buffer-size:8M</code><br>
    <i>Check <a href='https://rclone.org/flags/'>RClone Flags</a>.</i>
    
    <b>📚 Bulk Download</b> (-b or -bulk)<br>
    Reply to a text message or file with links separated by new lines.<br>
    <b>Example:</b><br>
    <code>
    link1 -n newname -up remote1:path1
    link2 -z -n newname
    </code><br>
    <code>/cmd -b</code><br>
    <i>Use -b start:end to specify link range.</i>
    
    <b>📌 Notes</b>
    <ul>
        <li>Check yt-dlp options <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>here</a>.</li>
        <li>Avoid partial -m in bulk; use for all links or multi without bulk.</li>
    </ul>
    """
]

MIRROR_HELP_MESSAGE = [
    """
    <b>📥 Mirror & Leech Command Guide</b>
    
    Send links or files with <i>/{BotCommands.MirrorCommand[0]}</i> or reply to mirror/leech to Telegram, Google Drive, or DDLs using RClone, Aria2, or qBittorrent. 🚀
    
    <b>✨ Available Arguments</b>
    <ul>
        <li><b>-n</b> or <b>-name</b>: Rename file</li>
        <li><b>-z</b> or <b>-zip</b>: Zip files (optional password)</li>
        <li><b>-e</b>, <b>-extract</b>, <b>-uz</b>, or <b>-unzip</b>: Extract archives</li>
        <li><b>-up</b> or <b>-upload</b>: Upload to Google Drive, RClone, or DDL</li>
        <li><b>-b</b> or <b>-bulk</b>: Download multiple links</li>
        <li><b>-i</b>: Download multiple links by reply</li>
        <li><b>-m</b>, <b>-sd</b>, or <b>-samedir</b>: Download to same directory</li>
        <li><b>-d</b> or <b>-seed</b>: Seed torrents</li>
        <li><b>-s</b> or <b>-select</b>: Select torrent files</li>
        <li><b>-u</b> or <b>-user</b>: Username for authenticated links</li>
        <li><b>-p</b> or <b>-pass</b>: Password for authenticated links</li>
        <li><b>-j</b> or <b>-join</b>: Join split files</li>
        <li><b>-rcf</b>: RClone flags</li>
        <li><b>-id</b>: Google Drive folder ID or link</li>
        <li><b>-index</b>: Index URL for Google Drive</li>
        <li><b>-c</b> or <b>-category</b>: Select Google Drive category</li>
        <li><b>-ud</b> or <b>-dump</b>: Select dump chat</li>
        <li><b>-ss</b> or <b>-screenshots</b>: Generate screenshots</li>
        <li><b>-t</b> or <b>-thumb</b>: Add custom thumbnail</li>
    </ul>
    """,
    """
    <b>🚀 How to Use</b>
    
    <b>🔗 Send with Command</b><br>
    <code>/cmd https://example.com/file.zip -n newname</code>
    
    <b>💬 Reply to Link/File</b><br>
    <code>/cmd -n newname -z -e -up gdrive</code>
    
    <b>📝 Rename File</b> (-n or -name)<br>
    <code>/cmd https://example.com/file.zip -n newname</code><br>
    <i>Note: Not supported for torrents.</i>
    
    <b>🔐 Authenticated Links</b> (-u or -p)<br>
    <code>/cmd https://example.com/file -u user -p pass</code>
    
    <b>📸 Screenshots</b> (-ss or -screenshots)<br>
    <code>/cmd https://example.com/video.mp4 -ss 3</code>
    
    <b>🖼️ Custom Thumbnail</b> (-t or -thumb)<br>
    <code>/cmd https://example.com/video.mp4 -t https://telegra.ph/image.jpg</code>
    
    <b>📦 Zip/Extract</b> (-z or -e)<br>
    <code>/cmd https://example.com/file.zip -e pass</code><br>
    <code>/cmd https://example.com/file -z pass</code><br>
    <i>Note: Extract happens before zipping.</i>
    
    <b>🧲 Torrent Selection</b> (-s or -select)<br>
    <code>/cmd magnet:?xt=urn:btih:xxx -s</code>
    
    <b>🌱 Torrent Seeding</b> (-d or -seed)<br>
    <code>/cmd magnet:?xt=urn:btih:xxx -d 0.7:10</code><br>
    <i>Format: ratio:time (minutes), e.g., 0.7:10 or :10.</i>
    
    <b>🔗 Multi-Links (Reply)</b> (-i)<br>
    <code>/cmd -i 10</code>
    
    <b>📂 Same Directory</b> (-m, -sd, or -samedir)<br>
    <code>/cmd -i 10 -m foldername</code>
    
    <b>☁️ Custom Drive Upload</b> (-id & -index)<br>
    <code>/cmd -id drive_folder_link -index https://example.com/0:</code>
    
    <b>🏷️ Category Selection</b> (-c or -category)<br>
    <code>/cmd -c category_name</code>
    
    <b>📤 Dump Chat</b> (-ud or -dump)<br>
    <code>/cmd -ud @username</code>
    
    <b>⬆️ Upload Options</b> (-up or -upload)<br>
    <code>/cmd https://example.com/file -up mrcc:main:dump</code>
    
    <b>⚡ RClone Flags</b> (-rcf)<br>
    <code>/cmd https://example.com/file -rcf --buffer-size:8M</code>
    
    <b>📚 Bulk Download</b> (-b or -bulk)<br>
    <code>
    link1 -n newname -up remote1:path1
    link2 -z -n newname
    </code><br>
    <code>/cmd -b</code>
    
    <b>🔗 Join Split Files</b> (-j or -join)<br>
    <code>/cmd -i 3 -j -m foldername</code>
    
    <b>☁️ RClone Download</b><br>
    <code>/cmd mrcc:main:dump/file.iso</code>
    
    <b>📬 Telegram Links</b><br>
    <i>Supported: Public, Private, Super links. Requires USER_SESSION_STRING for private links.</i>
    
    <b>📌 Notes</b>
    <ul>
        <li>qBittorrent commands start with <i>qb</i>.</li>
        <li>Use <a href='https://rclone.org/flags/'>RClone Flags</a> for -rcf.</li>
    </ul>
    """
]

RSS_HELP_MESSAGE = """
<b>📰 RSS Feed Setup Guide</b>

Add RSS feeds to automatically download content. 📡

<b>📝 Format</b><br>
<code>Title https://rss-url.com -c /cmd -inf 1080p|mkv -exf flv|xxx -d 0.7:10 -z pass</code>

<b>✨ Arguments</b>
<ul>
    <li><b>-c</b>: Command to execute (e.g., <i>/{BotCommands.YtdlCommand[0]}</i>)</li>
    <li><b>-inf</b>: Include words filter (e.g., 1080p|mkv|hevc)</li>
    <li><b>-exf</b>: Exclude words filter (e.g., flv|web|xxx)</li>
    <li><b>-d</b>: Seed settings (ratio:time)</li>
    <li><b>-z</b>: Zip settings (optional password)</li>
</ul>

<b>🚀 Example</b><br>
<code>Anime https://rss-url.com -inf 1080p|mkv|hevc -exf flv|xxx -c /ytdl -up mrcc:remote:path</code><br>
<i>Filters titles with 1080p, mkv, or hevc, excluding flv or xxx.</i>

<b>📌 Filter Notes</b>
<ul>
    <li>Use | for AND, or for OR.</li>
    <li>Add spaces or special characters to avoid wrong matches.</li>
    <li>Example: <code>-inf 1080 or 720p|.web.|hevc</code></li>
</ul>

<b>⏰ Timeout</b>: 60 seconds
"""

CLONE_HELP_MESSAGE = [
    """
    <b>📂 Clone Command Guide</b>
    
    Copy files or folders from Google Drive, Gdtot, Filepress, Filebee, Appdrive, Gdflix, or RClone paths using <i>/{BotCommands.CloneCommand[0]}</i>. ☁️
    
    <b>✨ Available Arguments</b>
    <ul>
        <li><b>-up</b> or <b>-upload</b>: Upload to Google Drive, RClone, or DDL</li>
        <li><b>-i</b>: Multi-link downloads by reply</li>
        <li><b>-rcf</b>: RClone flags</li>
        <li><b>-id</b>: Google Drive folder ID or link</li>
        <li><b>-index</b>: Index URL for Google Drive</li>
        <li><b>-c</b> or <b>-category</b>: Select Google Drive category</li>
    </ul>
    """,
    """
    <b>🚀 How to Use</b>
    
    <b>🔗 Clone Link</b><br>
    <code>/cmd https://drive.google.com/folder/xxx</code>
    
    <b>🔗 Multi-Links (Reply)</b> (-i)<br>
    <code>/cmd -i 10</code>
    
    <b>☁️ RClone Path</b> (-rcf)<br>
    <code>/cmd mrcc:main:dump/file.iso -rcf --buffer-size:8M</code>
    
    <b>📂 Custom Drive Upload</b> (-id & -index)<br>
    <code>/cmd -id drive_folder_link -index https://example.com/0:</code>
    
    <b>🏷️ Category Selection</b> (-c)<br>
    <code>/cmd -c category_name</code>
    
    <b>📌 Notes</b>
    <ul>
        <li>Default upload uses RCLONE_PATH from config.env if -up is not specified.</li>
        <li>Use -c or category buttons for UserTD uploads.</li>
    </ul>
    """
]

CATEGORY_HELP_MESSAGE = """
<b>🏷️ Category Selection Guide</b>

Change the upload category for an active download using <i>/{BotCommands.CategorySelect}</i>. Reply to an active download or provide a task ID.

<b>🚀 Example</b><br>
<code>/cmd -id drive_folder_link -index https://example.com/0: gid</code>

<b>📌 Note</b><br>
Drive ID must be a folder ID or link, and index must be a valid URL.
"""

help_string = [
    """
    <b>🌟 Basic Commands</b>
    
    <b>📥 Mirror Commands</b>
    <ul>
        <li><i>/{BotCommands.MirrorCommand[0]}</i> or <i>/{BotCommands.MirrorCommand[1]}</i>: Download and upload to cloud</li>
        <li><i>/{BotCommands.CategorySelect}</i>: Select upload category</li>
    </ul>
    
    <b>🧲 qBittorrent Commands</b>
    <ul>
        <li><i>/{BotCommands.QbMirrorCommand[0]}</i> or <i>/{BotCommands.QbMirrorCommand[1]}</i>: Download torrents</li>
        <li><i>/{BotCommands.BtSelectCommand}</i>: Select torrent files</li>
    </ul>
    
    <b>📹 YouTube Commands</b>
    <ul>
        <li><i>/{BotCommands.YtdlCommand[0]}</i> or <i>/{BotCommands.YtdlCommand[1]}</i>: Download yt-dlp links</li>
        <li><i>/{BotCommands.YtdlLeechCommand[0]}</i> or <i>/{BotCommands.YtdlLeechCommand[1]}</i>: Download and upload to Telegram</li>
    </ul>
    
    <b>📤 Leech Commands</b>
    <ul>
        <li><i>/{BotCommands.LeechCommand[0]}</i> or <i>/{BotCommands.LeechCommand[1]}</i>: Upload to Telegram</li>
        <li><i>/{BotCommands.QbLeechCommand[0]}</i> or <i>/{BotCommands.QbLeechCommand[1]}</i>: Torrent to Telegram</li>
    </ul>
    
    <b>📂 Google Drive Commands</b>
    <ul>
        <li><i>/{BotCommands.CloneCommand[0]}</i>: Copy to cloud</li>
        <li><i>/{BotCommands.CountCommand}</i>: Count Drive files</li>
        <li><i>/{BotCommands.DeleteCommand}</i>: Delete Drive files (Owner/Sudo)</li>
    </ul>
    
    <b>🛑 Cancel Tasks</b>
    <ul>
        <li><i>/{BotCommands.CancelMirror}</i>: Cancel by task ID or reply</li>
    </ul>
    """,
    """
    <b>👤 User Commands</b>
    
    <b>⚙️ Settings</b>
    <ul>
        <li><i>/{BotCommands.UserSetCommand[0]}</i> or <i>/{BotCommands.UserSetCommand[1]}</i>: Open user settings</li>
    </ul>
    
    <b>🔑 Authentication</b>
    <ul>
        <li><i>/login</i>: Skip token system (Private)</li>
    </ul>
    
    <b>📊 Stats</b>
    <ul>
        <li><i>/{BotCommands.StatusCommand[0]}</i> or <i>/{BotCommands.StatusCommand[1]}</i>: View active tasks</li>
        <li><i>/{BotCommands.StatsCommand[0]}</i> or <i>/{BotCommands.StatsCommand[1]}</i>: Server stats</li>
        <li><i>/{BotCommands.PingCommand[0]}</i> or <i>/{BotCommands.PingCommand[1]}</i>: Check bot ping</li>
    </ul>
    
    <b>📰 RSS Feed</b>
    <ul>
        <li><i>/{BotCommands.RssCommand}</i>: Manage RSS subscriptions</li>
    </ul>
    """,
    """
    <b>🔐 Owner & Sudo Commands</b>
    
    <b>⚙️ Bot Management</b>
    <ul>
        <li><i>/{BotCommands.BotSetCommand[0]}</i> or <i>/{BotCommands.BotSetCommand[1]}</i>: Bot settings</li>
        <li><i>/{BotCommands.UsersCommand}</i>: User stats</li>
    </ul>
    
    <b>🔒 Authorization</b>
    <ul>
        <li><i>/{BotCommands.AuthorizeCommand[0]}</i> or <i>/{BotCommands.AuthorizeCommand[1]}</i>: Authorize users/chats</li>
        <li><i>/{BotCommands.UnAuthorizeCommand[0]}</i> or <i>/{BotCommands.UnAuthorizeCommand[1]}</i>: Unauthorize users/chats</li>
        <li><i>/{BotCommands.AddSudoCommand}</i>: Add sudo user</li>
        <li><i>/{BotCommands.RmSudoCommand}</i>: Remove sudo user</li>
        <li><i>/{BotCommands.AddBlackListCommand[0]}</i> or <i>/{BotCommands.AddBlackListCommand[1]}</i>: Blacklist user</li>
        <li><i>/{BotCommands.RmBlackListCommand[0]}</i> or <i>/{BotCommands.RmBlackListCommand[1]}</i>: Unblacklist user</li>
    </ul>
    
    <b>📢 Broadcast</b>
    <ul>
        <li><i>/{BotCommands.BroadcastCommand[0]}</i> or <i>/{BotCommands.BroadcastCommand[1]}</i>: Message all users</li>
    </ul>
    
    <b>🗑️ Google Drive</b>
    <ul>
        <li><i>/{BotCommands.GDCleanCommand[0]}</i> or <i>/{BotCommands.GDCleanCommand[1]}</i>: Clear Drive folder</li>
    </ul>
    
    <b>🔄 Maintenance</b>
    <ul>
        <li><i>/{BotCommands.RestartCommand[0]}</i> or <i>/{BotCommands.RestartCommand[1]}</i>: Restart bot</li>
        <li><i>/{BotCommands.RestartCommand[2]}</i>: Restart all bots</li>
        <li><i>/{BotCommands.LogCommand}</i>: Get log file</li>
    </ul>
    
    <b>💻 Advanced Execution</b>
    <ul>
        <li><i>/{BotCommands.ShellCommand}</i>: Run shell commands</li>
        <li><i>/{BotCommands.EvalCommand}</i>: Run Python code</li>
        <li><i>/{BotCommands.ExecCommand}</i>: Run exec commands</li>
        <li><i>/{BotCommands.ClearLocalsCommand}</i>: Clear locals</li>
        <li><i>/exportsession</i>: Generate session string</li>
    </ul>
    
    <b>🖼️ Extras</b>
    <ul>
        <li><i>/{BotCommands.AddImageCommand}</i>: Add images</li>
        <li><i>/{BotCommands.ImagesCommand}</i>: View image grid</li>
    </ul>
    """,
    """
    <b>🎥 Miscellaneous Commands</b>
    
    <b>⚡ Speed & Media</b>
    <ul>
        <li><i>/{BotCommands.SpeedCommand[0]}</i> or <i>/{BotCommands.SpeedCommand[1]}</i>: Test server speed</li>
        <li><i>/{BotCommands.MediaInfoCommand[0]}</i> or <i>/{BotCommands.MediaInfoCommand[1]}</i>: Get MediaInfo</li>
    </ul>
    
    <b>🌐 Search</b>
    <ul>
        <li><i>/{BotCommands.ListCommand}</i>: Search Google Drive</li>
        <li><i>/{BotCommands.SearchCommand}</i>: Search torrents</li>
    </ul>
    
    <b>🎬 Media Search</b>
    <ul>
        <li><i>/{BotCommands.IMDBCommand}</i>: Search IMDb</li>
        <li><i>/{BotCommands.AniListCommand}</i>: Search AniList</li>
        <li><i>/{BotCommands.AnimeHelpCommand}</i>: Anime guide</li>
        <li><i>/{BotCommands.MyDramaListCommand}</i>: Search MyDramaList</li>
    </ul>
    """
]

PASSWORD_ERROR_MESSAGE = """
<b>🔐 Password Required</b>

This link requires a password! Use <b>::</b> between the link and password (no spaces).

<b>📝 Example</b><br>
<code>https://example.com/file.zip::my password</code>

<i>Note: Passwords can include spaces.</i>
"""

default_desp = {
    "AS_DOCUMENT": "Upload files as documents (default: False, uploads as media).",
    "ANIME_TEMPLATE": "Custom AniList template (HTML tags supported).",
    "AUTHORIZED_CHATS": "User/chat IDs to authorize (space-separated).",
    "AUTO_DELETE_MESSAGE_DURATION": "Time (seconds) before bot deletes messages. Set to -1 to disable.",
    "BASE_URL": "Bot deployment URL (e.g., http://myip or http://myip:port).",
    "BASE_URL_PORT": "Port for BASE_URL (default: 80).",
    "BLACKLIST_USERS": "Block users from using bot (space-separated user IDs).",
    "BOT_MAX_TASKS": "Max parallel tasks (including queue).",
    "STORAGE_THRESHOLD": "Min free storage (GB) before downloads are canceled.",
    "LEECH_LIMIT": "Max torrent/direct/yt-dlp leech size (GB).",
    "CLONE_LIMIT": "Max Google Drive clone size (GB).",
    "MEGA_LIMIT": "Max Mega download size (GB).",
    "TORRENT_LIMIT": "Max torrent download size (GB).",
    "DIRECT_LIMIT": "Max direct link download size (GB).",
    "YTDLP_LIMIT": "Max yt-dlp download size (GB).",
    "PLAYLIST_LIMIT": "Max playlist items.",
    "IMAGES": "Telegraph image links (space-separated).",
    "IMG_SEARCH": "Keywords for image download (comma-separated).",
    "IMG_PAGE": "Page number for image downloads (default: 1).",
    "IMDB_TEMPLATE": "Custom IMDb template (HTML tags, emojis supported).",
    "AUTHOR_NAME": "Author name for Telegraph pages.",
    "AUTHOR_URL": "Author URL for Telegraph pages (e.g., channel link).",
    "COVER_IMAGE": "Telegraph cover image (Telegraph link).",
    "TITLE_NAME": "Title for Telegraph pages (/list command).",
    "GD_INFO": "Description for Google Drive uploads.",
    "DELETE_LINKS": "Delete links on task start (default: False).",
    "EXCEP_CHATS": "Chats exempt from logging (space-separated chat IDs).",
    "SAFE_MODE": "Hide task details for safety (default: False).",
    "SOURCE_LINK": "Add source link button (default: False).",
    "SHOW_EXTRA_CMDS": "Enable extra commands (e.g., /unzipxxx, /zipxxx).",
    "BOT_THEME": "Bot theme (e.g., minimal). See <a href='https://t.ly/9rVXq'>sample</a>.",
    "USER_MAX_TASKS": "Max tasks per user in group.",
    "DAILY_TASK_LIMIT": "Max tasks per user per day.",
    "DISABLE_DRIVE_LINK": "Disable Google Drive link button (default: False).",
    "DAILY_MIRROR_LIMIT": "Daily mirror size limit (GB).",
    "GDRIVE_LIMIT": "Max Google Drive leech/zip size (GB).",
    "DAILY_LEECH_LIMIT": "Daily leech size limit (GB).",
    "USER_TASKS_LIMIT": "Max tasks per user.",
    "FSUB_IDS": "Force-subscribe chat IDs (space-separated, bot must be admin).",
    "BOT_PM": "Send files/links to bot PM (default: False).",
    "BOT_TOKEN": "Telegram bot token from @BotFather.",
    "CMD_SUFFIX": "Custom text/number appended to commands.",
    "DATABASE_URL": "MongoDB URL for storing auth, settings, and tasks.",
    "DEFAULT_UPLOAD": "Default upload destination (rc, gd, or ddl).",
    "DOWNLOAD_DIR": "Local download folder path.",
    "MDL_TEMPLATE": "Custom MyDramaList template (HTML tags supported).",
    "CLEAN_LOG_MSG": "Clean leech log and PM messages (default: False).",
    "LEECH_LOG_ID": "Chat ID for leech uploads (superGroup/channel, -100xxxxxx).",
    "MIRROR_LOG_ID": "Chat ID for mirror logs (space-separated for multiple).",
    "EQUAL_SPLITS": "Split files larger than LEECH_SPLIT_SIZE (default: False).",
    "EXTENSION_FILTER": "File extensions to exclude (space-separated).",
    "GDRIVE_ID": "Google Drive folder/team drive ID for uploads.",
    "INCOMPLETE_TASK_NOTIFIER": "Notify incomplete tasks after restart (default: False).",
    "INDEX_URL": "Google Drive index URL.",
    "IS_TEAM_DRIVE": "Use TeamDrive for uploads (default: False).",
    "SHOW_MEDIAINFO": "Add MediaInfo button for leeched files (default: False).",
    "SCREENSHOTS_MODE": "Enable screenshots via -ss (default: False).",
    "CAP_FONT": "Caption font for leech (b, i, u, s, code, spoiler).",
    "LEECH_FILENAME_PREFIX": "Custom prefix for leeched file names.",
    "LEECH_FILENAME_SUFFIX": "Custom suffix for leeched file names.",
    "LEECH_FILENAME_CAPTION": "Custom caption for leeched files/videos.",
    "LEECH_FILENAME_REMNAME": "Words to remove from leeched file names.",
    "LOGIN_PASS": "Permanent pass to skip token system.",
    "TOKEN_TIMEOUT": "Token timeout for group members (seconds).",
    "DEBRID_LINK_API": "Debrid-link.com API for leeching.",
    "REAL_DEBRID_API": "Real-debrid.com API for torrents/hosters.",
    "LEECH_SPLIT_SIZE": "File split size (default: 2GB, 4GB for premium).",
    "MEDIA_GROUP": "Group split file parts (default: False).",
    "MEGA_EMAIL": "Mega.nz email for premium account.",
    "MEGA_PASSWORD": "Mega.nz password.",
    "OWNER_ID": "Telegram user ID of the bot owner.",
    "QUEUE_ALL": "Max parallel download/upload tasks.",
    "QUEUE_DOWNLOAD": "Max parallel download tasks.",
    "QUEUE_UPLOAD": "Max parallel upload tasks.",
    "RCLONE_FLAGS": "RClone flags (key:value|key).",
    "RCLONE_PATH": "Default RClone upload path.",
    "RCLONE_SERVE_URL": "RClone serve URL (e.g., http://myip:port).",
    "RCLONE_SERVE_USER": "RClone serve username.",
    "RCLONE_SERVE_PASS": "RClone serve password.",
    "RCLONE_SERVE_PORT": "RClone serve port (default: 8080).",
    "RSS_CHAT_ID": "Chat ID for RSS links (add -100 for channels).",
    "RSS_DELAY": "RSS refresh interval (seconds, min 900).",
    "SEARCH_API_LINK": "Torrent search API link.",
    "SEARCH_LIMIT": "Search result limit per site.",
    "SEARCH_PLUGINS": "qBittorrent search plugins (GitHub raw links).",
    "STATUS_LIMIT": "Max tasks shown in status (default: 10).",
    "STATUS_UPDATE_INTERVAL": "Status update interval (seconds, min 10).",
    "STOP_DUPLICATE": "Check for Drive duplicates (default: False).",
    "SUDO_USERS": "Sudo user IDs (space-separated).",
    "TELEGRAM_API": "Telegram API ID from my.telegram.org.",
    "TELEGRAM_HASH": "Telegram API hash from my.telegram.org.",
    "TIMEZONE": "Preferred timezone for restart messages.",
    "TORRENT_TIMEOUT": "Timeout for dead torrents (seconds).",
    "UPSTREAM_REPO": "GitHub repo for bot updates.",
    "UPSTREAM_BRANCH": "Branch for updates (default: master).",
    "UPGRADE_PACKAGES": "Auto-install new requirements (default: False).",
    "SAVE_MSG": "Add save message button (default: False).",
    "SET_COMMANDS": "Auto-set bot commands (default: False).",
    "JIODRIVE_TOKEN": "Jiodrive.xyz token for downloads.",
    "USER_TD_MODE": "Enable User Google Drive TD (default: False).",
    "USER_TD_SA": "Service account email for UserTD uploads.",
    "USER_SESSION_STRING": "Session string for Telegram downloads/RSS.",
    "USE_SERVICE_ACCOUNTS": "Use service accounts for Google Drive (default: False).",
    "WEB_PINCODE": "Ask for pincode in web torrent selection (default: False).",
    "YT_DLP_OPTIONS": "Default yt-dlp options (e.g., format:best|nocheckcertificate:True)."
}
