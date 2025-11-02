# 🎧 Vibe Check
> Discord Rich Presence that shows what you're listening to on YouTube Music.

---

## 📁 프로젝트 구성
```
Discord-Music-Status/
├── run_rpc_youtubemusic.py
├── config.ini
├── requirements.txt
├── Makefile
└── README.md
```

---

## 🧩 config.ini
```ini
[Config]
token = 1434498596719300658
```
> 💡 이 파일에는 Discord Application의 **Client ID**(=token)가 들어 있습니다.  
> 다른 사용자는 자신의 Discord 개발자 포털에서 발급받은 Application ID로 교체하면 됩니다.  

---

## 📦 requirements.txt
```txt
pypresence==4.3.0
```
> (`ctypes`, `configparser`, `os`, `re`, `datetime`, `time` 등은 Python 표준 라이브러리이므로 추가 설치 불필요)

---

## ⚙️ Makefile
```makefile
run:
	python run_rpc_youtubemusic.py

install:
	pip install -r requirements.txt

clean:
	del /Q last-run.log 2>nul || true
```

---

## 🧠 README.md
```markdown
# 🎧 Vibe Check
> Discord Rich Presence that shows what you're listening to on YouTube Music.

---

## 🚀 소개
**Vibe Check**는 현재 YouTube Music에서 재생 중인 곡 제목을  
디스코드 상태 메시지에 자동으로 표시해주는 간단한 파이썬 스크립트입니다.

---

## 📦 설치 방법

### 1️⃣ Python 설치
Python 3.10 이상이 필요합니다.  
명령 프롬프트에서 다음을 입력해 확인하세요:
```bash
python --version
```

---

### 2️⃣ 필수 패키지 설치
```bash
pip install -r requirements.txt
```

---

### 3️⃣ Discord Application 등록
1. [Discord Developer Portal](https://discord.com/developers/applications) 접속  
2. 새 Application 생성 → 이름은 `Vibe Check` 추천  
3. `Client ID`를 복사해서 `config.ini`의 `token` 값에 붙여넣기  
   ```ini
   [Config]
   token = YOUR_CLIENT_ID
   ```

---

### 4️⃣ 실행
```bash
python run_rpc_youtubemusic.py
```

디스코드에서 **현재 재생 중인 곡 제목**이 표시됩니다. 🎶

---

## ⚡ 작동 원리
- Windows API (`ctypes`)를 이용해 열려 있는 윈도우 창의 제목을 검사합니다.
- YouTube Music 탭의 제목(`노래 제목 - YouTube Music - Chrome`)을 분석해 곡 제목만 추출합니다.
- `pypresence` 라이브러리를 사용해 Discord 상태를 갱신합니다.

---

## 🧩 config.ini 수정
다른 사용자는 Discord Application의 Client ID를 넣어 사용하면 됩니다.
```ini
[Config]
token = 1434498596719300658
```
이 값을 자신의 Discord Application ID로 교체하세요.

---

## 🧠 예시
![vibe-check-demo](https://user-images.githubusercontent.com/example/vibecheck-demo.png)

---

## 💡 주의사항
- Discord 앱이 실행 중이어야 합니다.  
- YouTube Music 탭이 열려 있어야 정상 동작합니다.  
- 현재는 곡 제목만 표시하며, 가수명은 포함되지 않습니다.

---

## 🪶 License
MIT License © 2025 누누
```

---

## 📝 커밋 메시지 제안
```bash
🎧 Add "Vibe Check" — Discord YouTube Music status script

- Added run_rpc_youtubemusic.py (simplified YouTube Music tracker)
- Included config.ini with sample token (replace with your own Application ID)
- Added requirements.txt and Makefile for setup convenience
- Wrote complete README.md for setup & usage guide
```
