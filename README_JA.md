# NetEaseMusicWorld++

[简体中文](README.md) | [English](README_EN.md) | 日本語

> NetEase Musicの海外アクセス制限を解除するFirefox拡張機能（新バージョン）

## 拡張機能のURL

Firefoxバージョン：ソースコードから手動インストール（下記インストール方法を参照）

## 概要

これは海外ユーザーがNetEase MusicにアクセスできるようにするFirefox拡張機能です。本プロジェクトは、ChromeバージョンからFirefox拡張機能形式に変換し、より良い互換性のためにManifest V2を使用しています。

オリジナルの作者がメンテナンスを終了し、私自身も海外でNetEase Musicを使用する必要があるため、この拡張機能を更新し、Firefox形式に変換して、より多くの海外ユーザーのために提供しています。

## Firefoxインストール方法

1. このリポジトリのすべてのファイルをダウンロード
2. Firefoxブラウザを開く
3. アドレスバーに `about:debugging` と入力
4. 「このFirefox」をクリック
5. 「一時的なアドオンを読み込む」をクリック
6. ダウンロードした `manifest.json` ファイルを選択
7. 拡張機能がFirefoxに読み込まれます

## バージョン履歴

- 第1版：[acgotaku/NetEaseMusicWorld](https://github.com/acgotaku/NetEaseMusicWorld)
- 第2版：[nondanee/NetEaseMusicWorldPlus](https://github.com/nondanee/NetEaseMusicWorldPlus)

## 主な更新内容

1. Firefox拡張機能形式への変換
   - Firefox互換性のためのManifest V2使用
   - declarativeNetRequestをwebRequest APIに置き換え
   - Chrome固有のAPIの代わりにbrowser APIを使用
   - Firefox 57+バージョンをサポート

2. 機能の最適化
   - リクエストの傍受と変更にwebRequest APIを使用
   - 直感的な操作のための単一モード
   - システムのhostsファイルの変更が不要
   - 元のChromeバージョンと同じ機能を維持

## 使用方法

1. インストール後、ツールバーの拡張機能アイコンをクリックして有効/無効を切り替え
2. グレーのアイコンは無効状態
3. 赤いアイコンは有効状態

## プライバシー通知

- ユーザーデータを収集しません
- 必要なネットワークリクエストのみを変更
- すべてのコードはオープンソース 