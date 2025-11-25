# NetEaseMusicWorld

简体中文 | [English](README_EN.md) | [日本語](README_JA.md)

> 帮助海外用户访问网易云音乐的 Python 工具，支持二维码登录和每日自动刷新 IP

## ✨ 功能特点

- 🔐 **二维码登录** - 使用网易云音乐 APP 扫码登录
- 🌏 **海外访问** - 自动添加中国 IP 头部，解除海外访问限制
- ⏰ **自动刷新** - 每日自动刷新 IP 会话，保持访问畅通
- 📝 **每日签到** - 自动完成 PC 端和移动端签到任务
- 🔄 **守护进程模式** - 可在后台持续运行

## 📦 安装

### 环境要求

- Python 3.8 或更高版本
- pip 包管理器

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/HackingU0/NetEaseMusicWorldNext.git
cd NetEaseMusicWorldNext

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

## 🚀 使用方法

### 1. 二维码登录

```bash
python main.py login
```

运行后会生成二维码图片并在终端显示，使用网易云音乐 APP 扫描登录。

### 2. 检查登录状态

```bash
python main.py status
```

### 3. 手动刷新 IP 会话

```bash
python main.py refresh
```

### 4. 守护进程模式（推荐）

```bash
# 默认每 24 小时刷新一次
python main.py daemon

# 自定义刷新间隔（例如每 12 小时）
python main.py daemon -i 12
```

### 命令行参数

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

## 📁 项目结构

```
NetEaseMusicWorldNext/
├── main.py              # 主程序入口
├── netease_client.py    # 网易云音乐 API 客户端
├── crypto_utils.py      # 加密工具
├── config.json          # 配置文件
├── requirements.txt     # Python 依赖
├── cookies.json         # 登录凭证（自动生成，已忽略）
└── README.md            # 说明文档
```

## 🔧 配置说明

配置文件 `config.json`:

```json
{
    "cookie_file": "cookies.json",
    "refresh_interval_hours": 24,
    "china_ip": "211.161.244.70"
}
```

- `cookie_file`: Cookie 存储文件路径
- `refresh_interval_hours`: 自动刷新间隔（小时）
- `china_ip`: 用于请求头的中国 IP 地址

## 🐳 Docker 部署（可选）

```bash
# 构建镜像
docker build -t netease-music-world .

# 运行容器
docker run -d --name netease-music \
  -v $(pwd)/cookies.json:/app/cookies.json \
  netease-music-world daemon
```

## ⚠️ 注意事项

1. 首次使用需要先运行 `python main.py login` 进行登录
2. `cookies.json` 文件包含登录凭证，请妥善保管
3. 建议使用守护进程模式保持登录状态
4. 本项目仅供学习交流使用

## 📜 历史版本

本项目基于以下项目演变而来：

- 第一版：[acgotaku/NetEaseMusicWorld](https://github.com/acgotaku/NetEaseMusicWorld) - Chrome 扩展
- 第二版：[nondanee/NetEaseMusicWorldPlus](https://github.com/nondanee/NetEaseMusicWorldPlus) - Chrome 扩展
- 当前版本：Python 实现，支持自动化运行

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证