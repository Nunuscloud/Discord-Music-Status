import time
import re
import ctypes
import configparser
import os
from datetime import datetime
from pypresence import Presence

# ===== Config path =====
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.ini")

# ===== Read config.ini =====
CFG = configparser.ConfigParser()
if not os.path.exists(CONFIG_PATH):
    print("config.ini not found. Please create one with [Config] token=ApplicationID.")
    raise SystemExit(1)

CFG.read(CONFIG_PATH, encoding="utf-8")
CLIENT_ID = CFG.get("Config", "token", fallback="").strip()
if not CLIENT_ID:
    print("Please provide your Application ID (token) in config.ini.")
    raise SystemExit(1)

# ===== Connect to Discord RPC =====
rpc = Presence(CLIENT_ID)
rpc.connect()
print("✅ Connected to Discord RPC")

# ===== Read window titles (Windows API) =====
user32 = ctypes.windll.user32
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
GetWindowTextLengthW = user32.GetWindowTextLengthW
GetWindowTextW = user32.GetWindowTextW
IsWindowVisible = user32.IsWindowVisible

def list_window_titles():
    """Return a list of all visible window titles"""
    titles = []

    @EnumWindowsProc
    def foreach(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLengthW(hwnd)
            if length > 0:
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowTextW(hwnd, buff, length + 1)
                t = buff.value.strip()
                if t:
                    titles.append(t)
        return True

    user32.EnumWindows(foreach, 0)
    return titles

# ===== Extract YouTube Music song title =====
BROWSERS = (" - Google Chrome", " - Microsoft Edge", " - Brave", " - Opera", " - Vivaldi")

def extract_song_from_title(title: str) -> str | None:
    """Extract song title from YouTube Music browser tab"""
    if "YouTube Music" not in title:
        return None

    t = title.strip()

    # Remove browser suffix
    for tail in BROWSERS:
        if t.endswith(tail):
            t = t[: -len(tail)]
            break

    # Remove " - YouTube Music"
    t = re.sub(r"[\-\–—·| ]*YouTube Music[\-\–—·| ]*", "", t, flags=re.IGNORECASE)

    t = t.strip(" -–—·|")
    if not t or len(t) < 2:
        return None

    return f"🎧 {t}"

def get_now_playing_youtubemusic() -> str | None:
    """Find the currently playing YouTube Music song"""
    for t in list_window_titles():
        song = extract_song_from_title(t)
        if song:
            return song
    return None

# ===== Update Discord presence =====
last_text = None
start_ts = int(datetime.now().timestamp())

def update_presence(text: str | None):
    """Update Discord Rich Presence with the current song"""
    global last_text
    if text and text != last_text:
        rpc.update(
            details=text[:128],
            start=start_ts,
        )
        print("✅ Updated:", text)
        last_text = text
    elif not text and last_text is not None:
        rpc.clear()
        print("🧹 Cleared presence (no song)")
        last_text = None

# ===== Main loop =====
try:
    print("🎵 Monitoring YouTube Music...")
    while True:
        title = get_now_playing_youtubemusic()
        update_presence(title)
        time.sleep(3)
except KeyboardInterrupt:
    print("🛑 Exiting...")
    rpc.clear()
