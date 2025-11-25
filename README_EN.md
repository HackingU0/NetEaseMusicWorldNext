# NetEaseMusicWorld

[简体中文](README.md) | English | [日本語](README_JA.md)

> A Python tool to help overseas users access NetEase Cloud Music with QR code login and daily automatic IP refresh

## ✨ Features

- 🔐 **QR Code Login** - Login by scanning QR code with NetEase Music APP
- 🌏 **Overseas Access** - Automatically adds China IP header to bypass regional restrictions
- ⏰ **Auto Refresh** - Daily automatic IP session refresh to maintain access
- 📝 **Daily Check-in** - Automatically perform PC and mobile check-in tasks
- 🔄 **Daemon Mode** - Can run continuously in the background

## 📦 Installation

### Requirements

- Python 3.8 or higher
- pip package manager

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/HackingU0/NetEaseMusicWorldNext.git
cd NetEaseMusicWorldNext

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

### 1. QR Code Login

```bash
python main.py login
```

This will generate a QR code image and display it in terminal. Scan with NetEase Music APP to login.

### 2. Check Login Status

```bash
python main.py status
```

### 3. Manually Refresh IP Session

```bash
python main.py refresh
```

### 4. Daemon Mode (Recommended)

```bash
# Default: refresh every 24 hours
python main.py daemon

# Custom refresh interval (e.g., every 12 hours)
python main.py daemon -i 12
```

### Command Line Arguments

```
usage: main.py [-h] [-i INTERVAL] [-c COOKIES] {login,refresh,status,daemon}

NetEase Music World - Help overseas users access NetEase Music

positional arguments:
  {login,refresh,status,daemon}
                        Command to execute

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        Refresh interval in hours for daemon mode (default: 24)
  -c COOKIES, --cookies COOKIES
                        Cookie file path (default: cookies.json)
```

## 📁 Project Structure

```
NetEaseMusicWorldNext/
├── main.py              # Main entry point
├── netease_client.py    # NetEase Music API client
├── crypto_utils.py      # Encryption utilities
├── config.json          # Configuration file
├── requirements.txt     # Python dependencies
├── cookies.json         # Login credentials (auto-generated, ignored)
└── README.md            # Documentation
```

## 🔧 Configuration

Configuration file `config.json`:

```json
{
    "cookie_file": "cookies.json",
    "refresh_interval_hours": 24,
    "china_ip": "211.161.244.70"
}
```

- `cookie_file`: Path to cookie storage file
- `refresh_interval_hours`: Auto refresh interval in hours
- `china_ip`: China IP address used in request headers

## 🐳 Docker Deployment (Optional)

```bash
# Build image
docker build -t netease-music-world .

# Run container
docker run -d --name netease-music \
  -v $(pwd)/cookies.json:/app/cookies.json \
  netease-music-world daemon
```

## ⚠️ Notes

1. First-time users must run `python main.py login` to login
2. The `cookies.json` file contains login credentials, keep it secure
3. Daemon mode is recommended to maintain login status
4. This project is for learning and educational purposes only

## 📜 Version History

This project evolved from:

- Version 1: [acgotaku/NetEaseMusicWorld](https://github.com/acgotaku/NetEaseMusicWorld) - Chrome Extension
- Version 2: [nondanee/NetEaseMusicWorldPlus](https://github.com/nondanee/NetEaseMusicWorldPlus) - Chrome Extension
- Current: Python implementation with automation support

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

This project is licensed under the MIT License 