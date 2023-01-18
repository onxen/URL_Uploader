import os


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5895581615:AAFXUNzqSqGTwitPaXfW4wpYDT4lpjZMFKs")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 21569673 ))
    API_HASH = os.environ.get("API_HASH", "1ba68f53204b8add14973b7c7fdda399")
    # Get these values from my.telegram.org
    OWNER_ID = int(os.environ.get("OWNER_ID", "1126504307"))
    # Array to store users who are authorized to use the bot
    AUTH_USERS = list({int(x)
                      for x in os.environ.get("AUTH_USERS", "1126504307").split()})
    AUTH_USERS.append(OWNER_ID)
    # The download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # The anonfile upload location, where the HTTP Server runs
    UPLOADER_LOCATION = "./ANONFILE_UPLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    CHUNK_SIZE = 128
    PROCESS_MAX_TIMEOUT = 3600
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get(
        "DEF_THUMB_NAIL_VID_S",
        "https://placehold.it/90x90"
    )
    # proxy for accessing yt-dlp in GeoRestricted Areas
    # Get your own proxy from
    # https://github.com/rg3/yt-dlp/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
