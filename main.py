#!/usr/bin/env python3
"""
NetEase Music World - Python Edition

A tool to help overseas users access NetEase Cloud Music by:
1. QR code login
2. Daily automatic IP refresh
3. Session maintenance

Usage:
    python main.py login     - Login with QR code
    python main.py refresh   - Manually refresh IP session
    python main.py status    - Check login status
    python main.py daemon    - Run as daemon with scheduled refresh
"""

import argparse
import logging
import os
import signal
import sys
import time
from datetime import datetime

import schedule

from netease_client import NetEaseClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('netease_music.log', encoding='utf-8')
    ]
)
logger = logging.getLogger('NetEaseMusicWorld')


class NetEaseMusicWorld:
    """Main application class for NetEase Music World."""
    
    def __init__(self, cookie_file: str = 'cookies.json'):
        """
        Initialize the application.
        
        Args:
            cookie_file: Path to cookie storage file
        """
        self.client = NetEaseClient(cookie_file)
        self.running = True
    
    def login(self) -> bool:
        """
        Perform QR code login.
        
        Returns:
            True if login successful, False otherwise
        """
        print('=' * 50)
        print('NetEase Music World - QR Code Login')
        print('网易云音乐海外版 - 二维码登录')
        print('=' * 50)
        
        if self.client.is_logged_in():
            account = self.client.get_user_account()
            nickname = account.get('profile', {}).get('nickname', 'User')
            print(f'\n已登录账号: {nickname}')
            print(f'Already logged in as: {nickname}')
            
            choice = input('\n是否重新登录? (y/N): ').strip().lower()
            if choice != 'y':
                return True
            
            self.client.logout()
        
        return self.client.qr_login()
    
    def check_status(self) -> bool:
        """
        Check and display login status.
        
        Returns:
            True if logged in, False otherwise
        """
        print('=' * 50)
        print('Checking Login Status...')
        print('=' * 50)
        
        if self.client.is_logged_in():
            account = self.client.get_user_account()
            profile = account.get('profile', {})
            
            print(f"\n✓ 登录状态: 已登录")
            print(f"✓ Login Status: Logged In")
            print(f"\n用户信息 / User Info:")
            print(f"  昵称 / Nickname: {profile.get('nickname', 'N/A')}")
            print(f"  用户ID / User ID: {profile.get('userId', 'N/A')}")
            print(f"  VIP类型 / VIP Type: {profile.get('vipType', 0)}")
            
            return True
        else:
            print(f"\n✗ 登录状态: 未登录")
            print(f"✗ Login Status: Not Logged In")
            print("\n请运行 'python main.py login' 进行登录")
            print("Please run 'python main.py login' to login")
            
            return False
    
    def refresh_session(self) -> bool:
        """
        Refresh the IP session.
        
        Returns:
            True if refresh successful, False otherwise
        """
        print('=' * 50)
        print(f'Refreshing IP Session... ({datetime.now().strftime("%Y-%m-%d %H:%M:%S")})')
        print('=' * 50)
        
        if not self.client.is_logged_in():
            logger.warning('Not logged in, please login first')
            return False
        
        # Refresh IP session
        success = self.client.refresh_ip_session()
        
        if success:
            print('✓ IP会话刷新成功')
            print('✓ IP session refreshed successfully')
            
            # Also perform daily sign-in
            print('\n执行每日签到...')
            print('Performing daily sign-in...')
            
            # PC sign-in
            pc_result = self.client.daily_sign_in(sign_type=0)
            if pc_result.get('code') == 200:
                print('✓ PC端签到成功')
            elif pc_result.get('code') == -2:
                print('✓ PC端今日已签到')
            
            # Mobile sign-in
            mobile_result = self.client.daily_sign_in(sign_type=1)
            if mobile_result.get('code') == 200:
                print('✓ 移动端签到成功')
            elif mobile_result.get('code') == -2:
                print('✓ 移动端今日已签到')
        else:
            print('✗ IP会话刷新失败')
            print('✗ IP session refresh failed')
        
        return success
    
    def scheduled_refresh(self):
        """Perform scheduled refresh task."""
        logger.info('Running scheduled IP refresh...')
        self.refresh_session()
    
    def run_daemon(self, interval_hours: int = 24):
        """
        Run as daemon with scheduled refresh.
        
        Args:
            interval_hours: Hours between refresh tasks
        """
        print('=' * 50)
        print('NetEase Music World - Daemon Mode')
        print('网易云音乐海外版 - 守护进程模式')
        print('=' * 50)
        
        if not self.client.is_logged_in():
            print('\n未登录，请先登录')
            print('Not logged in, please login first')
            print("运行 'python main.py login' 进行登录")
            print("Run 'python main.py login' to login")
            return
        
        print(f'\n守护进程已启动，每 {interval_hours} 小时刷新一次')
        print(f'Daemon started, refreshing every {interval_hours} hours')
        print('按 Ctrl+C 停止 / Press Ctrl+C to stop\n')
        
        # Perform initial refresh
        self.refresh_session()
        
        # Schedule periodic refresh
        schedule.every(interval_hours).hours.do(self.scheduled_refresh)
        
        # Handle graceful shutdown
        def signal_handler(signum, frame):
            print('\n\n正在停止守护进程...')
            print('Stopping daemon...')
            self.running = False
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        # Run scheduler
        while self.running:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
        
        print('守护进程已停止')
        print('Daemon stopped')


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='NetEase Music World - Help overseas users access NetEase Music',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
    python main.py login      Login with QR code
    python main.py refresh    Manually refresh IP session
    python main.py status     Check login status
    python main.py daemon     Run as daemon with scheduled refresh
    python main.py daemon -i 12    Refresh every 12 hours
        '''
    )
    
    parser.add_argument(
        'command',
        choices=['login', 'refresh', 'status', 'daemon'],
        help='Command to execute'
    )
    
    parser.add_argument(
        '-i', '--interval',
        type=int,
        default=24,
        help='Refresh interval in hours for daemon mode (default: 24)'
    )
    
    parser.add_argument(
        '-c', '--cookies',
        type=str,
        default='cookies.json',
        help='Cookie file path (default: cookies.json)'
    )
    
    args = parser.parse_args()
    
    # Initialize application
    app = NetEaseMusicWorld(cookie_file=args.cookies)
    
    # Execute command
    if args.command == 'login':
        success = app.login()
        sys.exit(0 if success else 1)
    
    elif args.command == 'refresh':
        success = app.refresh_session()
        sys.exit(0 if success else 1)
    
    elif args.command == 'status':
        logged_in = app.check_status()
        sys.exit(0 if logged_in else 1)
    
    elif args.command == 'daemon':
        app.run_daemon(interval_hours=args.interval)
        sys.exit(0)


if __name__ == '__main__':
    main()
