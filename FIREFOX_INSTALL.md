# Firefox Extension Installation Guide

## 安装指南 / Installation Guide / インストールガイド

### 中文安装说明

1. **下载扩展文件**
   - 下载本仓库的所有文件到本地文件夹

2. **打开 Firefox 开发者模式**
   - 在 Firefox 地址栏输入：`about:debugging`
   - 点击左侧的"此 Firefox"

3. **加载扩展**
   - 点击"临时载入附加组件"按钮
   - 选择下载文件夹中的 `manifest.json` 文件
   - 扩展将自动加载并显示在扩展列表中

4. **使用扩展**
   - 扩展图标将出现在 Firefox 工具栏中
   - 点击图标切换启用/禁用状态
   - 红色图标表示启用，灰色图标表示禁用

### English Installation Instructions

1. **Download Extension Files**
   - Download all files from this repository to a local folder

2. **Open Firefox Developer Mode**
   - Type `about:debugging` in Firefox address bar
   - Click "This Firefox" on the left side

3. **Load Extension**
   - Click "Load Temporary Add-on" button
   - Select the `manifest.json` file from the downloaded folder
   - Extension will be automatically loaded and shown in the extension list

4. **Use Extension**
   - Extension icon will appear in Firefox toolbar
   - Click icon to toggle enable/disable status
   - Red icon means enabled, grey icon means disabled

### 日本語インストール手順

1. **拡張機能ファイルのダウンロード**
   - このリポジトリのすべてのファイルをローカルフォルダにダウンロード

2. **Firefox開発者モードを開く**
   - Firefoxのアドレスバーに `about:debugging` と入力
   - 左側の「このFirefox」をクリック

3. **拡張機能の読み込み**
   - 「一時的なアドオンを読み込む」ボタンをクリック
   - ダウンロードしたフォルダから `manifest.json` ファイルを選択
   - 拡張機能が自動的に読み込まれ、拡張機能リストに表示されます

4. **拡張機能の使用**
   - 拡張機能のアイコンがFirefoxツールバーに表示されます
   - アイコンをクリックして有効/無効を切り替え
   - 赤いアイコンは有効、グレーのアイコンは無効を示します

## 技术说明 / Technical Notes / 技術仕様

- **支持的 Firefox 版本 / Supported Firefox Versions / 対応Firefoxバージョン**: 57+
- **Manifest 版本 / Manifest Version / マニフェストバージョン**: V2
- **使用的 API / APIs Used / 使用API**: webRequest, storage, browserAction
- **权限 / Permissions / 権限**: storage, webRequest, webRequestBlocking, *://music.163.com/*, *://*.music.126.net/*

## 故障排除 / Troubleshooting / トラブルシューティング

### 常见问题 / Common Issues / よくある問題

1. **扩展无法加载 / Extension won't load / 拡張機能が読み込まれない**
   - 确保下载了所有文件 / Make sure all files are downloaded / すべてのファイルがダウンロードされていることを確認
   - 检查 manifest.json 文件是否存在 / Check if manifest.json exists / manifest.jsonファイルが存在するかチェック

2. **图标不显示 / Icon not showing / アイコンが表示されない**
   - 重新加载扩展 / Reload the extension / 拡張機能を再読み込み
   - 检查 Firefox 版本是否支持 / Check Firefox version compatibility / Firefoxバージョンの互換性をチェック

3. **功能不工作 / Function not working / 機能が動作しない**
   - 确保已访问 music.163.com / Make sure to visit music.163.com / music.163.comにアクセスしていることを確認
   - 检查扩展是否已启用（红色图标）/ Check if extension is enabled (red icon) / 拡張機能が有効（赤いアイコン）かチェック