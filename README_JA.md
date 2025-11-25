# NetEaseMusicWorld

[简体中文](README.md) | [English](README_EN.md) | 日本語

> QRコードログインと毎日の自動IP更新をサポートする、海外ユーザー向けNetEase Cloud MusicアクセスPythonツール

## ✨ 機能

- 🔐 **QRコードログイン** - NetEase Music APPでQRコードをスキャンしてログイン
- 🌏 **海外アクセス** - 中国IPヘッダーを自動追加して地域制限を解除
- ⏰ **自動更新** - 毎日の自動IPセッション更新でアクセスを維持
- 📝 **毎日のサインイン** - PCとモバイルのサインインタスクを自動実行
- 🔄 **デーモンモード** - バックグラウンドで継続的に実行可能

## 📦 インストール

### 必要条件

- Python 3.8以上
- pipパッケージマネージャー

### インストール手順

```bash
# リポジトリをクローン
git clone https://github.com/HackingU0/NetEaseMusicWorldNext.git
cd NetEaseMusicWorldNext

# 仮想環境を作成（推奨）
python -m venv venv
source venv/bin/activate  # Linux/macOS
# または
venv\Scripts\activate  # Windows

# 依存関係をインストール
pip install -r requirements.txt
```

## 🚀 使用方法

### 1. QRコードログイン

```bash
python main.py login
```

QRコード画像を生成し、ターミナルに表示します。NetEase Music APPでスキャンしてログインしてください。

### 2. ログイン状態を確認

```bash
python main.py status
```

### 3. 手動でIPセッションを更新

```bash
python main.py refresh
```

### 4. デーモンモード（推奨）

```bash
# デフォルト：24時間ごとに更新
python main.py daemon

# カスタム更新間隔（例：12時間ごと）
python main.py daemon -i 12
```

### コマンドライン引数

```
usage: main.py [-h] [-i INTERVAL] [-c COOKIES] {login,refresh,status,daemon}

NetEase Music World - 海外ユーザーのNetEase Musicアクセスを支援

positional arguments:
  {login,refresh,status,daemon}
                        実行するコマンド

optional arguments:
  -h, --help            ヘルプを表示
  -i INTERVAL, --interval INTERVAL
                        デーモンモードの更新間隔（時間単位、デフォルト：24）
  -c COOKIES, --cookies COOKIES
                        Cookieファイルのパス（デフォルト：cookies.json）
```

## 📁 プロジェクト構造

```
NetEaseMusicWorldNext/
├── main.py              # メインエントリーポイント
├── netease_client.py    # NetEase Music APIクライアント
├── crypto_utils.py      # 暗号化ユーティリティ
├── config.json          # 設定ファイル
├── requirements.txt     # Python依存関係
├── cookies.json         # ログイン資格情報（自動生成、無視）
└── README.md            # ドキュメント
```

## 🔧 設定

設定ファイル `config.json`:

```json
{
    "cookie_file": "cookies.json",
    "refresh_interval_hours": 24,
    "china_ip": "211.161.244.70"
}
```

- `cookie_file`: Cookie保存ファイルのパス
- `refresh_interval_hours`: 自動更新間隔（時間）
- `china_ip`: リクエストヘッダーに使用する中国IPアドレス

## 🐳 Dockerデプロイメント（オプション）

```bash
# イメージをビルド
docker build -t netease-music-world .

# コンテナを実行
docker run -d --name netease-music \
  -v $(pwd)/cookies.json:/app/cookies.json \
  netease-music-world daemon
```

## ⚠️ 注意事項

1. 初回使用時は `python main.py login` でログインする必要があります
2. `cookies.json` ファイルにはログイン資格情報が含まれています。安全に保管してください
3. ログイン状態を維持するためにデーモンモードを推奨
4. このプロジェクトは学習・教育目的のみです

## 📜 バージョン履歴

このプロジェクトの進化：

- 第1版：[acgotaku/NetEaseMusicWorld](https://github.com/acgotaku/NetEaseMusicWorld) - Chrome拡張機能
- 第2版：[nondanee/NetEaseMusicWorldPlus](https://github.com/nondanee/NetEaseMusicWorldPlus) - Chrome拡張機能
- 現在：自動化サポート付きPython実装

## 🤝 貢献

IssueとPull Requestを歓迎します！

## 📄 ライセンス

このプロジェクトはMITライセンスの下でライセンスされています 