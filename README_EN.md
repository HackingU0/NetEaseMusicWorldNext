# NetEaseMusicWorld++

[简体中文](README.md) | English | [日本語](README_JA.md)

> Firefox extension for unlocking overseas access to NetEase Music (New Version)

## Extension URL

Firefox version: Manual installation from source code (see installation method below)

## Introduction

This is a Firefox extension that helps overseas users access NetEase Music. This project is converted from the Chrome version to Firefox extension format, using Manifest V2 for better compatibility.

As the original authors are no longer maintaining their versions, and I personally need to use NetEase Music overseas, I've updated this extension and converted it to Firefox format to help more overseas users.

## Firefox Installation Method

1. Download all files from this repository
2. Open Firefox browser
3. Type `about:debugging` in the address bar
4. Click "This Firefox"
5. Click "Load Temporary Add-on"
6. Select the downloaded `manifest.json` file
7. The extension will be loaded into Firefox

## Version History

- Version 1: [acgotaku/NetEaseMusicWorld](https://github.com/acgotaku/NetEaseMusicWorld)
- Version 2: [nondanee/NetEaseMusicWorldPlus](https://github.com/nondanee/NetEaseMusicWorldPlus)

## Major Updates

1. Converted to Firefox Extension Format
   - Using Manifest V2 for Firefox compatibility
   - Replaced declarativeNetRequest with webRequest API
   - Using browser API instead of Chrome-specific APIs
   - Supports Firefox 57+ versions

2. Optimized Implementation
   - Using webRequest API for request interception and modification
   - Simplified to single mode for intuitive operation
   - No system hosts file modification needed
   - Maintains same functionality as original Chrome version

## Usage

1. After installation, click the extension icon in the toolbar to toggle enable/disable
2. Grey icon indicates disabled status
3. Red icon indicates enabled status

## Privacy Notice

- No user data collection
- Only modifies necessary network requests
- All code is open source 