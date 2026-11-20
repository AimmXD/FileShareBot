<h1 align="center">
  <b>Alpha Share Bot</b>
</h1>
 
<p align="center">
  <a href="https://github.com/utkarshdubey2008/AlphaShare">
    <img src="https://envs.sh/SlS.jpg" alt="Alpha Share Bot" width="500">
  </a>
  <br>
  <b>A Powerful File Sharing Bot for Telegram</b>
</p>

<p align="center">
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.11.6-blue?style=for-the-badge&logo=python" alt="Python Version">
  </a>
  <a href="https://github.com/utkarshdubey2008/AlphaShare/stargazers">
    <img src="https://img.shields.io/github/stars/utkarshdubey2008/AlphaShare?style=for-the-badge" alt="GitHub Stars">
  </a>
  <a href="https://github.com/utkarshdubey2008/AlphaShare/fork">
    <img src="https://img.shields.io/github/forks/utkarshdubey2008/AlphaShare?style=for-the-badge" alt="GitHub Forks">
  </a>
  <br>
  <a href="https://github.com/utkarshdubey2008/AlphaShare/issues">
    <img src="https://img.shields.io/github/issues/utkarshdubey2008/AlphaShareBot?style=for-the-badge" alt="GitHub Issues">
  </a>
  <a href="https://github.com/utkarshdubey2008/AlphaShare/network/members">
    <img src="https://img.shields.io/github/last-commit/utkarshdubey2008/AlphaShare?style=for-the-badge" alt="Last Commit">
  </a>
  <a href="https://t.me/Thealphabotz">
    <img src="https://img.shields.io/badge/Updates-Channel-blue?style=for-the-badge&logo=telegram" alt="Updates Channel">
  </a>
</p>

<details>
<summary><b>🌟 Features</b></summary>

- **Admin-Only Uploads**: Authorized admins can securely upload files with multi-admin support.
- **Universal File Support**: Supports images, videos, documents, audio files, and all Telegram-supported files.
- **Unique File Sharing**: UUID-based unique links with real-time download tracking.
- **Advanced Statistics**: Track downloads, monitor storage usage, and view user engagement metrics.
- **Professional UI**: Clean formatting, interactive inline buttons, and real-time progress bars.
- **Security Features**: Admin verification, download monitoring, and file access control.
- **Auto Delete Feature**: Helps prevent copyright issues!
  - **Command**: /auto_del
  - **Usage**: /auto_del 2 → Sets auto-delete timer to 2 minutes.
- **Cleaner UI**: Smoother and more user-friendly experience.
- **Bot Keep-Alive Mechanism**: Ensures 24/7 uptime for a seamless experience on Koyeb.
- **URL Shortening**: Shorten any link using the `/short` command with Modiji URL API.
- **Privacy Mode**: Protects files by preventing users from forwarding or copying them.
- **BATCH UPLOADS** : Allows Users To Upload Multiple File At Once And Get A Single Link For It.
</details>

<details>
<summary><b>🛠️ Installation</b></summary>

### Local Deployment

```bash
# Clone the repository
git clone https://github.com/utkarshdubey2008/AlphaShare.git

# Navigate to directory
cd AlphaShareBot

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the bot
python main.py
```

### Heroku Deployment

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/utkarshdubey2008/AlphaShare)

[![Watch Deployment Tutorial](https://img.shields.io/badge/Watch%20Tutorial-YouTube-red?logo=youtube)](https://youtu.be/8d9XsFhWj5s?si=02OPS6p_h6pov5HW)

### Koyeb Deployment

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://youtu.be/2EKt3nVcY6E?si=NKMlRw3qx6eaWjNU)

[![Watch Deployment Tutorial](https://img.shields.io/badge/Watch%20Tutorial-YouTube-red?logo=youtube)](https://youtu.be/2EKt3nVcY6E?si=NKMlRw3qx6eaWjNU)

### Required Variables

```
BOT_TOKEN - Get from @BotFather
API_ID - Get from my.telegram.org
API_HASH - Get from my.telegram.org
MONGO_URI - Your MongoDB connection string
DB_CHANNEL_ID - Channel ID for file storage
ADMIN_IDS - List of admin user IDs
MODIJI_API_KEY - Your Modiji URL API key
```

</details>

<details>
<summary><b>📚 Commands</b></summary>

### User Commands

```
/start - Start the bot
/help - Show help message
/about - About the bot

```

### Admin Commands

```
/upload - Upload files (reply to file)
/stats - Get bot statistics
/broadcast - Send message to all users
/delete - Delete a file
/fileinfo - Get file information
/auto_del - Set auto-delete timer
/short <url> - To short the url in your preferred Shortner
/batch - Batch Multiple Files At Once
```

</details>

<details>
<summary><b>Supported Types, Extensions, and MIME Types</b></summary>

### Supported Types

```python
SUPPORTED_TYPES = [
    "document", "video", "audio", "photo", "voice", "video_note", "animation"
]
```

### Supported Extensions

```python
SUPPORTED_EXTENSIONS = [
    "pdf", "txt", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "py", "js", "html",
    "css", "json", "xml", "yaml", "yml", "zip", "rar", "7z", "tar", "gz", "bz2",
    "mp4", "mp3", "m4a", "wav", "avi", "mkv", "flv", "mov", "webm", "3gp", "m4v",
    "ogg", "opus", "jpg", "jpeg", "png", "gif", "webp", "bmp", "ico", "apk", "exe",
    "msi", "deb", "rpm", "text", "log", "csv", "md", "srt", "sub"
]
```

### Supported MIME Types

```python
SUPPORTED_MIME_TYPES = [
    "application/pdf", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/zip", "application/x-rar-compressed", "application/x-7z-compressed", "video/mp4", "audio/mpeg",
    "audio/mp4", "image/jpeg", "image/png", "image/gif", "application/vnd.android.package-archive", "application/x-executable"
]
```

</details>

<details>
  <summary><b>📦 Tech Stack</b></summary>
- **Python** - Programming Language
- **Pyrogram** - Telegram MTProto API Framework
- **MongoDB** - Database
- **Motor** - Async MongoDB Driver
- **aiofiles** - Async File Operations

  </details>

<details>
<summary><b>📋 Dependencies</b></summary>

- `pyrogram==2.0.106`
- `tgcrypto==1.2.5`
- `motor==3.3.1`
- `dnspython==2.4.2`
- `humanize==4.9.0`
- `python-dotenv==1.0.0`
- `aiofiles==23.2.1`
- `pytz==2023.3`
- `pymongo==4.5.0`

</details>

<details>
<summary><b>🤝 Contributing</b></summary>

Contributions are welcome! Please submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

</details>

<details>
<summary><b>📜 License</b></summary>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

</details>

<details>
<summary><b>📞 Support</b></summary>

- Channel: [@Thealphabotz](https://t.me/Thealphabotz)
- Developer: [@adarsh2626](https://t.me/adarsh2626)

</details>

<details>
<summary><b>🙏 Credits</b></summary>

- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Adarsh](https://t.me/adarsh2626)
- [All Contributors](https://github.com/utkarshdubey2008/AlphaShare/graphs/contributors)

</details>

<details>
<summary><b>Contributors</b></summary>

- @trashxrd [Telegram](https://t.me/trashxrd)
- @nxghtz [Telegram](https://t.me/nxghtz)
- @Mak0912 [Telegram](https://t.me/Mak0912)

</details>

<p align="center">
  <b>Last Updated: 2025-03-19 16:42:54 UTC</b>
  <br>
  <i>Made with ❤️ by <a href="https://t.me/adarsh2626">Adarsh</a></i>
</p>
