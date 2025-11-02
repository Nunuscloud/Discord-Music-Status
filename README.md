# 🎧 Vibe Check
> Discord Rich Presence that shows what you're listening to on YouTube Music.

---

## 🚀 Introduction
**Vibe Check** is a simple Python script that automatically updates your Discord status  
to show the title of the song currently playing on YouTube Music.

---

## 📦 Installation

### 1️⃣ Install Python
Python 3.10 or higher is required.  
Check your version with:
```bash
python --version
```

---

### 2️⃣ Install required packages
```bash
pip install -r requirements.txt
```

---

### 3️⃣ Register a Discord Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)  
2. Create a new Application (recommended name: `Vibe Check`)  
3. Copy the `Client ID` and paste it into the `config.ini` file like this:  
   ```ini
   [Config]
   token = YOUR_CLIENT_ID
   ```

---

### 4️⃣ Run the script
```bash
python run_rpc_youtubemusic.py
```

Your Discord status will now show the song title you're listening to. 🎶

---

## ⚡ How It Works
- Uses the Windows API (`ctypes`) to read the titles of currently open windows.  
- Extracts the song title from the YouTube Music tab (e.g. `Song - YouTube Music - Chrome`).  
- Updates Discord Rich Presence in real time using the `pypresence` library.

---

## 🧩 Editing config.ini
Replace the token with your own Discord Application Client ID.
```ini
[Config]
token = 1434498596719300658
```

---

## 🧠 Example
![vibe-check-demo](https://user-images.githubusercontent.com/example/vibecheck-demo.png)

---

## 💡 Notes
- Discord must be running for this to work.  
- The YouTube Music tab must be open.  
- Currently only shows the **song title**, not the artist name.

---

## 🪶 License
MIT License © 2025 Nunu
