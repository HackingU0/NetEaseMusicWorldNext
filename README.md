# NetEaseMusicWorld++

简体中文 | [English](README_EN.md) | [日本語](README_JA.md)

> 解锁网易云音乐网页版海外访问限制的 Firefox 扩展程序（新版）

## 插件地址

Firefox 版本：可通过源码手动安装（见下方安装方法）

## 简介

这是一个帮助海外用户访问网易云音乐的 Firefox 扩展程序。本项目是在 Chrome 版本的基础上，转换为 Firefox 扩展格式，使用 Manifest V2 以确保更好的兼容性。

由于原作者不再维护，且本人在海外经常需要使用网易云音乐，因此对这个扩展进行了更新，并转换为 Firefox 格式，方便更多海外用户使用。

## Firefox 安装方法

1. 下载本仓库的所有文件
2. 打开 Firefox 浏览器
3. 在地址栏输入 `about:debugging`
4. 点击"此 Firefox"
5. 点击"临时载入附加组件"
6. 选择下载的 `manifest.json` 文件
7. 扩展程序将被加载到 Firefox 中

## 历史版本

- 第一版：[acgotaku/NetEaseMusicWorld](https://github.com/acgotaku/NetEaseMusicWorld)
- 第二版：[nondanee/NetEaseMusicWorldPlus](https://github.com/nondanee/NetEaseMusicWorldPlus)

## 主要更新

1. 转换为 Firefox 扩展格式
   - 使用 Manifest V2 以确保 Firefox 兼容性
   - 替换 declarativeNetRequest 为 webRequest API
   - 使用 browser API 替代 Chrome 特定 API
   - 支持 Firefox 57+ 版本

2. 优化功能实现
   - 使用 webRequest API 进行请求拦截和修改
   - 简化为单一模式，操作更直观
   - 无需修改系统 hosts 文件
   - 保持与原 Chrome 版本相同的功能

## 使用方法

1. 安装扩展后，点击工具栏的扩展图标即可切换启用/禁用状态
2. 灰色图标表示禁用状态
3. 红色图标表示启用状态

## 隐私说明

- 不收集任何用户数据
- 仅修改必要的网络请求
- 所有代码开源可见