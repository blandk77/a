#!/usr/bin/env python3
from bot.helper.telegram_helper.bot_commands import BotCommands

YT_HELP_MESSAGE = [
    """
<b>📹 YouTube & yt-dlp Command Guide</b>

<i>Send links or files with command or reply to a command to download from YouTube or other yt-dlp supported sites and upload to Telegram, Google Drive, or DDL servers using tools like RClone or yt-dlp.</i>

➲ <b><u>Available Arguments</u></b>:

1. <b>-n</b> or <b>-name</b>: Rename the downloaded file.
2. <b>-z</b> or <b>-zip</b>: Zip files or links (optional password).
3. <b>-up</b> or <b>-upload</b>: Choose upload destination (Drive, RClone, or DDL).
4. <b>-b</b> or <b>-bulk</b>: Download multiple links from a message or file.
5. <b>-i</b>: Download multiple links by replying to the first link.
6. <b>-m</b>, <b>-sd</b>, or <b>-samedir</b>: Download multiple links into the same directory.
7. <b>-opt</b> or <b>-options</b>: Add custom yt-dlp options (e.g., format or playlist settings).
8. <b>-s</b> or <b>-select</b>: Select files from yt-dlp links, even with specified quality.
9. <b>-rcf</b>: Add RClone flags for uploads.
10. <b>-id</b>: Specify Google Drive folder ID or link.
11. <b>-index</b>: Index URL for Google Drive uploads.
12. <b>-c</b> or <b>-category</b>: Select a Google Drive category (case-insensitive).
13. <b>-ud</b> or <b>-dump</b>: Select a dump chat (name, chat ID, or username).
14. <b>-ss</b> or <b>-screenshots</b>: Generate screenshots for leeched videos.
15. <b>-t</b> or <b>-thumb</b>: Add a custom thumbnail for specific leech.

➲ <b><u>Usage Examples</u></b>:

• <b>With Command Line</b>:  
<i>/{BotCommands.YtdlCommand[0]}</i> https://youtube.com/watch?v=xxx -s -n newname -opt format:best

• <b>By Replying to Link</b>:  
<i>/{BotCommands.YtdlCommand[0]}</i> -n newname -z mypass -opt playliststart:^10

• <b>Rename File</b> (<b>-n</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> https://youtube.com/watch?v=xxx -n newvideo  
<span class="tg-spoiler">Note: Do not include file extension.</span>

• <b>Screenshots</b> (<b>-ss</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> https://youtube.com/watch?v=xxx -ss 3  
*Generates 3 screenshots per video file.*

• <b>Custom Thumbnail</b> (<b>-t</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> https://youtube.com/watch?v=xxx -t https://telegra.ph/image.jpg  
*Use a Telegram link or direct image URL.*

• <b>Quality Selection</b> (<b>-s</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> https://youtube.com/watch?v=xxx -s  
*Overrides default quality for specific links.*

• <b>Zip Files</b> (<b>-z</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> https://youtube.com/watch?v=xxx -z mypass  
*Creates a password-protected zip.*

• <b>Custom yt-dlp Options</b> (<b>-opt</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> https://youtube.com/watch?v=xxx -opt playliststart:^10|format:best  
<span class="tg-spoiler">Note: Use ^ before integers/floats. Check <a href="https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184">yt-dlp options</a>.</span>

• <b>Multi Links</b> (<b>-i</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> -i 5  
*Reply to the first link to download 5 links.*

• <b>Same Directory</b> (<b>-m</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> -i 5 -m myfolder  
*Downloads 5 links into 'myfolder'.*

• <b>Custom Drive Upload</b> (<b>-id</b>, <b>-index</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> -id drive_folder_link -index https://example.com/0:  
*Folder ID/link and index URL required.*

• <b>Category Selection</b> (<b>-c</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> -c movies  
*Selects the 'movies' category for upload.*

• <b>Dump Chat</b> (<b>-ud</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> -ud @mychannel  
*Uploads to specified chat or use 'all' for all dump chats.*

• <b>Custom Upload</b> (<b>-up</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> https://youtube.com/watch?v=xxx -up rcl  
*Or use direct path: -up mrcc:main:dump*

• <b>RClone Flags</b> (<b>-rcf</b>):  
<i>/{BotCommands.YtdlCommand[0]}</i> https://youtube.com/watch?v=xxx -rcf --buffer-size:8M  
*See <a href="https://rclone.org/flags/">RClone flags</a>.*

• <b>Bulk Download</b> (<b>-b</b>):  
*Reply to a message/file with links:*  
link1 -n newname -up remote1:path1  
link2 -z mypass -n newname2  
<i>/{BotCommands.YtdlCommand[0]}</i> -b  
*Use -b start:end to specify a range of links.*

<span class="tg-spoiler"><b>Notes</b>: Check <a href="https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184">yt-dlp API options</a> for advanced settings.</span>
""",
]

MIRROR_HELP_MESSAGE = [
    """
<b>📥 Mirror & Leech Command Guide</b>

<i>Send links or files with command or reply to a command to mirror or leech to Telegram, Google Drive, or DDL servers using RClone, Aria2, or qBittorrent.</i>

➲ <b><u>Available Arguments</u></b>:

1. <b>-n</b> or <b>-name</b>: Rename the downloaded file.
2. <b>-z</b> or <b>-zip</b>: Zip files or links (optional password).
3. <b>-e</b>, <b>-extract</b>, or <b>-uz</b>: Extract archived files.
4. <b>-up</b> or <b>-upload</b>: Choose upload destination (Drive, RClone, or DDL).
5. <b>-b</b> or <b>-bulk</b>: Download multiple links from a message or file.
6. <b>-i</b>: Download multiple links by replying to the first link.
7. <b>-m</b>, <b>-sd</b>, or <b>-samedir</b>: Download multiple links into the same directory.
8. <b>-d</b> or <b>-seed</b>: Seed torrents with ratio/time.
9. <b>-s</b> or <b>-select</b>: Select files from torrents.
10. <b>-u</b> or <b>-user</b>: Username for authenticated links.
11. <b>-p</b> or <b>-pass</b>: Password for authenticated links.
12. <b>-j</b> or <b>-join</b>: Join split files.
13. <b>-rcf</b>: Add RClone flags for uploads.
14. <b>-id</b>: Specify Google Drive folder ID or link.
15. <b>-index</b>: Index URL for Google Drive uploads.
16. <b>-c</b> or <b>-category</b>: Select a Google Drive category.
17. <b>-ud</b> or <b>-dump</b>: Select a dump chat (name, chat ID, or username).
18. <b>-ss</b> or <b>-screenshots</b>: Generate screenshots for leeched videos.
19. <b>-t</b> or <b>-thumb</b>: Add a custom thumbnail.

➲ <b><u>Usage Examples</u></b>:

• <b>With Command Line</b>:  
<i>/{BotCommands.MirrorCommand[0]}</i> https://example.com/file.zip -n newname

• <b>By Replying to Link/File</b>:  
<i>/{BotCommands.MirrorCommand[0]}</i> -n newname -z mypass -e

• <b>Rename File</b> (<b>-n</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> https://example.com/file.zip -n newfile  
<span class="tg-spoiler">Note: Does not work with torrents.</span>

• <b>Authentication</b> (<b>-u</b>, <b>-p</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> https://example.com/file.zip -u user -p pass

• <b>Screenshots</b> (<b>-ss</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> https://example.com/video.mp4 -ss 3  
*Generates 3 screenshots per video.*

• <b>Custom Thumbnail</b> (<b>-t</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> https://example.com/video.mp4 -t https://telegra.ph/image.jpg

• <b>Extract/Zip</b> (<b>-e</b>, <b>-z</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> https://example.com/file.zip -e mypass -z newpass  
*Extracts first, then zips with password.*

• <b>Torrent Selection</b> (<b>-s</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> magnet:?xt=urn:btih:xxx -s

• <b>Seed Torrent</b> (<b>-d</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> magnet:?xt=urn:btih:xxx -d 0.7:10  
*Seeds with 0.7 ratio or 10 minutes.*

• <b>Multi Links</b> (<b>-i</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> -i 5  
*Reply to the first link to download 5 links.*

• <b>Same Directory</b> (<b>-m</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> -i 5 -m myfolder  
*Downloads 5 links into 'myfolder'.*

• <b>Custom Drive Upload</b> (<b>-id</b>, <b>-index</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> -id drive_folder_link -index https://example.com/0:

• <b>Category Selection</b> (<b>-c</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> -c movies

• <b>Dump Chat</b> (<b>-ud</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> -ud @mychannel  
*Or use 'all' for all dump chats.*

• <b>Custom Upload</b> (<b>-up</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> https://example.com/file.zip -up mrcc:main:dump

• <b>RClone Flags</b> (<b>-rcf</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> https://example.com/file.zip -rcf --buffer-size:8M

• <b>Bulk Download</b> (<b>-b</b>):  
*Reply to a message/file with links:*  
link1 -n newname -up remote1:path1  
link2 -z mypass -n newname2  
<i>/{BotCommands.MirrorCommand[0]}</i> -b  
*Use -b start:end for specific link ranges.*

• <b>Join Split Files</b> (<b>-j</b>):  
<i>/{BotCommands.MirrorCommand[0]}</i> -i 3 -j -m myfolder  
*Joins split files before processing.*

• <b>RClone Download</b>:  
<i>/{BotCommands.MirrorCommand[0]}</i> mrcc:main:dump/ubuntu.iso

• <b>Telegram Links</b>:  
*Supports public, private, or super links.*  
<i>/{BotCommands.MirrorCommand[0]}</i> https://t.me/c/channel_id/message_id

<span class="tg-spoiler"><b>Notes</b>: Commands starting with 'qb' are for torrents only.</span>
""",
]

RSS_HELP_MESSAGE = """
<b>📰 RSS Feed Setup Guide</b>

<i>Configure RSS feeds to automatically download content based on filters and commands.</i>

➲ <b><u>Format</u></b>:  
Title [link] -c [command] -inf [include_words] -exf [exclude_words] -d [ratio:time] -z [password]

➲ <b><u>Arguments</u></b>:  
• <b>-c</b>: Command to execute (e.g., <i>/{BotCommands.YtdlCommand[0]}</i>).  
• <b>-inf</b>: Include words filter (e.g., 1080p|mkv|hevc).  
• <b>-exf</b>: Exclude words filter (e.g., flv|web|xxx).  

➲ <b><u>Example</u></b>:  
Anime https://rss-url.com -inf 1080p|mkv|hevc -exf flv|xxx -c <i>/{BotCommands.YtdlCommand[0]}</i> -up mrcc:remote:path  
*Parses titles with '1080p', 'mkv', or 'hevc' and excludes 'flv' or 'xxx'.*

➲ <b><u>Filter Tips</u></b>:  
• Use <b>|</b> for AND, <b>or</b> for OR.  
• Add spaces or special characters to avoid incorrect matches (e.g., ' 1080 ' to avoid '10805695').  
• Example: -inf 1080p|720p|.web.|hevc -exf flv|xxx  
*Timeout: 60 seconds.*

<span class="tg-spoiler"><b>Notes</b>: Avoid mixing unrelated filters like '1080|mp4 or 720|web'.</span>
"""

CLONE_HELP_MESSAGE = [
    """
<b>📂 Clone Command Guide</b>

<i>Copy files or folders from Google Drive, Gdtot, Filepress, Filebee, Appdrive, Gdflix, or RClone paths using command or reply.</i>

➲ <b><u>Available Arguments</u></b>:

1. <b>-up</b> or <b>-upload</b>: Choose upload destination (Drive, RClone, or DDL).
2. <b>-i</b>: Download multiple links by replying to the first link.
3. <b>-rcf</b>: Add RClone flags for uploads.
4. <b>-id</b>: Specify Google Drive folder ID or link.
5. <b>-index</b>: Index URL for Google Drive uploads.
6. <b>-c</b> or <b>-category</b>: Select a Google Drive category.

➲ <b><u>Usage Examples</u></b>:

• <b>Google Drive Link</b>:  
<i>/{BotCommands.CloneCommand[0]}</i> https://drive.google.com/folder/xxx

• <b>Multi Links</b> (<b>-i</b>):  
<i>/{BotCommands.CloneCommand[0]}</i> -i 5  
*Reply to the first link to copy 5 links.*

• <b>RClone Path</b> (<b>-rcf</b>):  
<i>/{BotCommands.CloneCommand[0]}</i> mrcc:main:dump/file.zip -rcf --buffer-size:8M

• <b>Custom Drive Upload</b> (<b>-id</b>, <b>-index</b>):  
<i>/{BotCommands.CloneCommand[0]}</i> -id drive_folder_link -index https://example.com/0:

• <b>Category Selection</b> (<b>-c</b>):  
<i>/{BotCommands.CloneCommand[0]}</i> -c movies

<span class="tg-spoiler"><b>Notes</b>: If -up is not specified, uses RCLONE_PATH from config.env. Use -c for UserTD uploads.</span>
""",
]

CATEGORY_HELP_MESSAGE = """
<b>📂 Category Selection Guide</b>

<i>Change the upload category for an active download by replying to the task or providing a task ID.</i>

➲ <b><u>Usage</u></b>:  
<i>/{BotCommands.CategorySelect}</i> -id drive_folder_link -index https://example.com/0: [gid]  
*Reply to an active download or specify the task ID.*

<span class="tg-spoiler"><b>Note</b>: Drive ID must be a folder ID or link, and index must be a valid URL.</span>
"""

help_string = [
    """
<b>🌟 Basic Commands</b>

<i>Core commands for downloading, uploading, and managing files.</i>

➲ <b><u>Mirror Commands</u></b>:  
• <i>/{BotCommands.MirrorCommand[0]}</i> or <i>/{BotCommands.MirrorCommand[1]}</i>: Download and upload to cloud drive.  
• <i>/{BotCommands.CategorySelect}</i>: Select custom upload category.

➲ <b><u>qBittorrent Commands</u></b>:  
• <i>/{BotCommands.QbMirrorCommand[0]}</i> or <i>/{BotCommands.QbMirrorCommand[1]}</i>: Download torrents and upload to cloud.  
• <i>/{BotCommands.BtSelectCommand}</i>: Select torrent files.

➲ <b><u>YouTube Commands</u></b>:  
• <i>/{BotCommands.YtdlCommand[0]}</i> or <i>/{BotCommands.YtdlCommand[1]}</i>: Download yt-dlp supported links.  
• <i>/{BotCommands.YtdlLeechCommand[0]}</i> or <i>/{BotCommands.YtdlLeechCommand[1]}</i>: Download and upload to Telegram.

➲ <b><u>Leech Commands</u></b>:  
• <i>/{BotCommands.LeechCommand[0]}</i> or <i>/{BotCommands.LeechCommand[1]}</i>: Upload to Telegram.  
• <i>/{BotCommands.QbLeechCommand[0]}</i> or <i>/{BotCommands.QbLeechCommand[1]}</i>: Torrent to Telegram.  

➲ <b><u>Google Drive Commands</u></b>:  
• <i>/{BotCommands.CloneCommand[0]}</i>: Copy to cloud drive.  
• <i>/{BotCommands.CountCommand}</i> [drive_url]: Count files in Google Drive.  
• <i>/{BotCommands.DeleteCommand}</i> [drive_url]: Delete from Google Drive (Owner/Sudo).

➲ <b><u>Cancel Tasks</u></b>:  
• <i>/{BotCommands.CancelMirror}</i>: Cancel a task by ID or reply.
""",
    """
<b>👤 User Commands</b>

<i>Manage your bot settings and check stats.</i>

➲ <b><u>Settings</u></b>:  
• <i>/{BotCommands.UserSetCommand[0]}</i> or <i>/{BotCommands.UserSetCommand[1]}</i> [query]: Open user settings.

➲ <b><u>Authentication</u></b>:  
• <i>/login</i>: Access bot without temp pass (Private).

➲ <b><u>Stats</u></b>:  
• <i>/{BotCommands.StatusCommand[0]}</i> or <i>/{BotCommands.StatusCommand[1]}</i>: View active tasks.  
• <i>/{BotCommands.StatsCommand[0]}</i> or <i>/{BotCommands.StatsCommand[1]}</i>: Server stats.  
• <i>/{BotCommands.PingCommand[0]}</i> or <i>/{BotCommands.PingCommand[1]}</i>: Check bot response time.

➲ <b><u>RSS</u></b>:  
• <i>/{BotCommands.RssCommand}</i>: Manage RSS feeds (Sub/Unsub/Start/Pause).
""",
    """
<b>🔐 Owner & Sudo Commands</b>

<i>Exclusive commands for bot management.</i>

➲ <b><u>Settings</u></b>:  
• <i>/{BotCommands.BotSetCommand[0]}</i> or <i>/{BotCommands.BotSetCommand[1]}</i> [query]: Bot settings.  
• <i>/{BotCommands.UsersCommand}</i>: View user stats.

➲ <b><u>Authentication</u></b>:  
• <i>/{BotCommands.AuthorizeCommand[0]}</i> or <i>/{BotCommands.AuthorizeCommand[1]}</i>: Authorize users/chats.  
• <i>/{BotCommands.UnAuthorizeCommand[0]}</i> or <i>/{BotCommands.UnAuthorizeCommand[1]}</i>: Unauthorize users/chats.  
• <i>/{BotCommands.AddSudoCommand}</i>: Add sudo user.  
• <i>/{BotCommands.RmSudoCommand}</i>: Remove sudo user.  
• <i>/{BotCommands.AddBlackListCommand[0]}</i> or <i>/{BotCommands.AddBlackListCommand[1]}</i>: Blacklist user.  
• <i>/{BotCommands.RmBlackListCommand[0]}</i> or <i>/{BotCommands.RmBlackListCommand[1]}</i>: Remove blacklist.

➲ <b><u>Stats</u></b>:  
• <i>/{BotCommands.BroadcastCommand[0]}</i> or <i>/{BotCommands.BroadcastCommand[1]}</i>: Broadcast to PM users.

➲ <b><u>Google Drive</u></b>:  
• <i>/{BotCommands.GDCleanCommand[0]}</i> or <i>/{BotCommands.GDCleanCommand[1]}</i> [drive_id]: Delete files from Drive.

➲ <b><u>Maintenance</u></b>:  
• <i>/{BotCommands.RestartCommand[0]}</i> or <i>/{BotCommands.RestartCommand[1]}</i>: Restart bot.  
• <i>/{BotCommands.RestartCommand[2]}</i>: Restart all bots.  
• <i>/{BotCommands.LogCommand}</i>: Get bot log file.

➲ <b><u>Executors</u></b>:  
• <i>/{BotCommands.ShellCommand}</i>: Run shell commands.  
• <i>/{BotCommands.EvalCommand}</i>: Run Python code.  
• <i>/{BotCommands.ExecCommand}</i>: Run exec commands.  
• <i>/{BotCommands.ClearLocalsCommand}</i>: Clear eval/exec locals.  
• <i>/exportsession</i>: Generate user session string.

➲ <b><u>Extras</u></b>:  
• <i>/{BotCommands.AddImageCommand}</i> [url/photo]: Add images to bot.  
• <i>/{BotCommands.ImagesCommand}</i>: Generate image grid.
""",
    """
<b>🎥 Miscellaneous Commands</b>

<i>Additional tools for searching and testing.</i>

➲ <b><u>Torrent/Drive Search</u></b>:  
• <i>/{BotCommands.ListCommand}</i> [query]: Search Google Drive.  
• <i>/{BotCommands.SearchCommand}</i> [query]: Search torrents via API.

➲ <b><u>Media Search</u></b>:  
• <i>/{BotCommands.IMDBCommand}</i>: Search IMDb.  
• <i>/{BotCommands.AniListCommand}</i>: Search AniList for anime.  
• <i>/{BotCommands.AnimeHelpCommand}</i>: Anime help guide.  
• <i>/{BotCommands.MyDramaListCommand}</i>: Search MyDramaList.

➲ <b><u>Speed & Media Info</u></b>:  
• <i>/{BotCommands.SpeedCommand[0]}</i> or <i>/{BotCommands.SpeedCommand[1]}</i>: Test server speed.  
• <i>/{BotCommands.MediaInfoCommand[0]}</i> or <i>/{BotCommands.MediaInfoCommand[1]}</i> [url/media]: Generate MediaInfo.
""",
]

PASSWORD_ERROR_MESSAGE = """
<b>🔒 Password-Protected Links</b>

<i>This link requires a password!</i>  
• Use <b>::</b> between the link and password (no spaces).  
• Passwords can include spaces.

<b>Example</b>: https://example.com/file.zip::my password
"""

default_desp = {
    "AS_DOCUMENT": "<i>Default Telegram file upload type. False means upload as media.</i>",
    "ANIME_TEMPLATE": "<i>Set AniList template with HTML tags support.</i>",
    "AUTHORIZED_CHATS": "<i>Authorize users/chats by user_id/chat_id (space-separated).</i>",
    "AUTO_DELETE_MESSAGE_DURATION": "<i>Time (seconds) before bot deletes messages. Set to -1 to disable.</i>",
    "BASE_URL": "<i>Bot's base URL (e.g., http://myip or http://myip:port).</i>",
    "BASE_URL_PORT": "<i>Port for BASE_URL. Default: 80.</i>",
    "BLACKLIST_USERS": "<i>Block users by user_id (space-separated).</i>",
    "BOT_MAX_TASKS": "<i>Max parallel tasks (including queue). Integer.</i>",
    "STORAGE_THRESHOLD": "<i>Min free storage (GB) before canceling downloads.</i>",
    "LEECH_LIMIT": "<i>Max torrent/direct/ytdlp leech size (GB).</i>",
    "CLONE_LIMIT": "<i>Max Google Drive clone size (GB).</i>",
    "MEGA_LIMIT": "<i>Max Mega download size (GB).</i>",
    "TORRENT_LIMIT": "<i>Max torrent download size (GB).</i>",
    "DIRECT_LIMIT": "<i>Max direct link download size (GB).</i>",
    "YTDLP_LIMIT": "<i>Max yt-dlp download size (GB).</i>",
    "PLAYLIST_LIMIT": "<i>Max playlist items. Integer.</i>",
    "IMAGES": "<i>Telegraph image links (space-separated).</i>",
    "IMG_SEARCH": "<i>Keywords for image download (comma-separated).</i>",
    "IMG_PAGE": "<i>Page number for image downloads (approx 70 images/page). Default: 1.</i>",
    "IMDB_TEMPLATE": "<i>IMDB template with HTML tags and emojis.</i>",
    "AUTHOR_NAME": "<i>Author name for Telegraph pages.</i>",
    "AUTHOR_URL": "<i>Author URL for Telegraph pages (e.g., channel link).</i>",
    "COVER_IMAGE": "<i>Telegraph cover image URL.</i>",
    "TITLE_NAME": "<i>Title for Telegraph pages (used with /list).</i>",
    "GD_INFO": "<i>Description for Google Drive uploads.</i>",
    "DELETE_LINKS": "<i>Delete Telegram links on task start. Default: False.</i>",
    "EXCEP_CHATS": "<i>Chats exempt from logging (space-separated chat_ids).</i>",
    "SAFE_MODE": "<i>Hide task name/source link for safety. Default: False.</i>",
    "SOURCE_LINK": "<i>Add source link button (magnet/file/DL). Default: False.</i>",
    "SHOW_EXTRA_CMDS": "<i>Enable extra commands for zip/unzip (e.g., /unzipxxx).</i>",
    "BOT_THEME": "<i>Bot theme (e.g., minimal). See <a href='https://t.ly/9rVXq'>sample</a>.</i>",
    "USER_MAX_TASKS": "<i>Max tasks per user/group. Integer.</i>",
    "DAILY_TASK_LIMIT": "<i>Max tasks per user daily. Integer.</i>",
    "DISABLE_DRIVE_LINK": "<i>Disable drive link button. Default: False.</i>",
    "DAILY_MIRROR_LIMIT": "<i>Daily mirror size limit (GB).</i>",
    "GDRIVE_LIMIT": "<i>Google Drive leech/zip/unzip size limit (GB).</i>",
    "DAILY_LEECH_LIMIT": "<i>Daily leech size limit (GB).</i>",
    "USER_TASKS_LIMIT": "<i>Max tasks per user. Integer.</i>",
    "FSUB_IDS": "<i>Force subscribe chat_ids (space-separated, bot must be admin).</i>",
    "BOT_PM": "<i>Send files/links to bot PM. Default: False.</i>",
    "BOT_TOKEN": "<i>Telegram bot token from @BotFather.</i>",
    "CMD_SUFFIX": "<i>Custom text/index for command suffixes.</i>",
    "DATABASE_URL": "<i>MongoDB URL for storing auth, settings, and tasks.</i>",
    "DEFAULT_UPLOAD": "<i>Default upload: rc (RClone), gd (GDrive), or ddl. Default: gd.</i>",
    "DOWNLOAD_DIR": "<i>Local folder path for downloads.</i>",
    "MDL_TEMPLATE": "<i>MyDramaList template with HTML tags/emojis.</i>",
    "CLEAN_LOG_MSG": "<i>Clean leech log and PM task messages. Default: False.</i>",
    "LEECH_LOG_ID": "<i>Chat ID for leech uploads (superGroup/channel, -100xxx).</i>",
    "MIRROR_LOG_ID": "<i>Chat ID for mirror uploads (space-separated, -100xxx).</i>",
    "EQUAL_SPLITS": "<i>Split large files into equal parts. Default: False.</i>",
    "EXTENSION_FILTER": "<i>File extensions to exclude (space-separated).</i>",
    "GDRIVE_ID": "<i>Google Drive folder/TeamDrive ID for uploads.</i>",
    "INCOMPLETE_TASK_NOTIFIER": "<i>Notify incomplete tasks after restart. Default: False.</i>",
    "INDEX_URL": "<i>Google Drive index URL.</i>",
    "IS_TEAM_DRIVE": "<i>Use TeamDrive for uploads. Default: False.</i>",
    "SHOW_MEDIAINFO": "<i>Add MediaInfo button for leeched files. Default: False.</i>",
    "SCREENSHOTS_MODE": "<i>Enable screenshots via -ss. Default: False.</i>",
    "CAP_FONT": "<i>Caption font: b, i, u, s, code, spoiler. Default: None.</i>",
    "LEECH_FILENAME_PREFIX": "<i>Custom prefix for leeched file names.</i>",
    "LEECH_FILENAME_SUFFIX": "<i>Custom suffix for leeched file names.</i>",
    "LEECH_FILENAME_CAPTION": "<i>Custom caption for leeched files/videos.</i>",
    "LEECH_FILENAME_REMNAME": "<i>Remove words from leeched file names.</i>",
    "LOGIN_PASS": "<i>Permanent pass to skip token system.</i>",
    "TOKEN_TIMEOUT": "<i>Token timeout for group members (seconds).</i>",
    "DEBRID_LINK_API": "<i>Debrid-link.com API for leeching support.</i>",
    "REAL_DEBRID_API": "<i>Real-debrid.com API for torrent cache/hosters.</i>",
    "LEECH_SPLIT_SIZE": "<i>Split size for uploads (bytes, default: 2GB, 4GB for premium).</i>",
    "MEDIA_GROUP": "<i>View split files as media group. Default: False.</i>",
    "MEGA_EMAIL": "<i>Mega.nz email for premium account.</i>",
    "MEGA_PASSWORD": "<i>Mega.nz password.</i>",
    "OWNER_ID": "<i>Telegram user ID of the bot owner.</i>",
    "QUEUE_ALL": "<i>Max parallel download/upload tasks.</i>",
    "QUEUE_DOWNLOAD": "<i>Max parallel download tasks.</i>",
    "QUEUE_UPLOAD": "<i>Max parallel upload tasks.</i>",
    "RCLONE_FLAGS": "<i>RClone flags (key:value|key).</i>",
    "RCLONE_PATH": "<i>Default RClone upload path.</i>",
    "RCLONE_SERVE_URL": "<i>RClone serve URL (e.g., http://myip:port).</i>",
    "RCLONE_SERVE_USER": "<i>RClone serve username.</i>",
    "RCLONE_SERVE_PASS": "<i>RClone serve password.</i>",
    "RCLONE_SERVE_PORT": "<i>RClone serve port. Default: 8080.</i>",
    "RSS_CHAT_ID": "<i>Chat ID for RSS links (-100xxx for channels).</i>",
    "RSS_DELAY": "<i>RSS refresh interval (seconds, min 900).</i>",
    "SEARCH_API_LINK": "<i>Search API link for torrents.</i>",
    "SEARCH_LIMIT": "<i>Search limit per site. Default: 0 (API default).</i>",
    "SEARCH_PLUGINS": "<i>qBittorrent search plugin links (GitHub raw).</i>",
    "STATUS_LIMIT": "<i>Max tasks shown in status. Default: 10, recommended: 4.</i>",
    "STATUS_UPDATE_INTERVAL": "<i>Status update interval (seconds, min 10).</i>",
    "STOP_DUPLICATE": "<i>Check for duplicates in Drive. Default: False.</i>",
    "SUDO_USERS": "<i>Sudo user IDs (space-separated).</i>",
    "TELEGRAM_API": "<i>Telegram API ID from my.telegram.org.</i>",
    "TELEGRAM_HASH": "<i>Telegram API hash from my.telegram.org.</i>",
    "TIMEZONE": "<i>Preferred timezone for restart messages. See <a href='http://www.timezoneconverter.com/cgi-bin/findzone.tzc'>here</a>.</i>",
    "TORRENT_TIMEOUT": "<i>Timeout for dead torrents (seconds).</i>",
    "UPSTREAM_REPO": "<i>GitHub repo for updates (private: https://username:token@github.com/...).</i>",
    "UPSTREAM_BRANCH": "<i>Branch for updates. Default: master.</i>",
    "UPGRADE_PACKAGES": "<i>Install new requirements without crash checks. Default: False.</i>",
    "SAVE_MSG": "<i>Add save message button. Default: False.</i>",
    "SET_COMMANDS": "<i>Auto-set bot commands. Default: False.</i>",
    "JIODRIVE_TOKEN": "<i>Jiodrive.xyz token for downloads.</i>",
    "USER_TD_MODE": "<i>Enable User TeamDrive uploads. Default: False.</i>",
    "USER_TD_SA": "<i>Global SA email for UserTD permissions.</i>",
    "USER_SESSION_STRING": "<i>Session string for Telegram account downloads/RSS.</i>",
    "USE_SERVICE_ACCOUNTS": "<i>Use service accounts for Google Drive. Default: False.</i>",
    "WEB_PINCODE": "<i>Require pincode for torrent file selection. Default: False.</i>",
    "YT_DLP_OPTIONS": "<i>Default yt-dlp options (key:value|key:value).</i>",
}
