"""
NetEase Cloud Music API Client

This module provides the main API client for interacting with
NetEase Cloud Music services.
"""

import json
import logging
import os
import time
from typing import Optional
from http.cookies import SimpleCookie

import qrcode
import requests

from crypto_utils import NetEaseCrypto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('NetEaseClient')


class NetEaseClient:
    """NetEase Cloud Music API Client."""
    
    BASE_URL = 'https://music.163.com'
    CHINA_IP = '211.161.244.70'
    
    def __init__(self, cookie_file: str = 'cookies.json'):
        """
        Initialize the NetEase client.
        
        Args:
            cookie_file: Path to the cookie storage file
        """
        self.cookie_file = cookie_file
        self.session = requests.Session()
        self._setup_headers()
        self._load_cookies()
    
    def _setup_headers(self):
        """Setup default headers for requests."""
        self.session.headers.update({
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            ),
            'Referer': 'https://music.163.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Real-IP': self.CHINA_IP,
        })
    
    def _load_cookies(self):
        """Load cookies from file if exists."""
        if os.path.exists(self.cookie_file):
            try:
                with open(self.cookie_file, 'r', encoding='utf-8') as f:
                    cookies = json.load(f)
                    for name, value in cookies.items():
                        self.session.cookies.set(name, value)
                logger.info('Cookies loaded successfully')
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f'Failed to load cookies: {e}')
    
    def _save_cookies(self):
        """Save cookies to file."""
        try:
            cookies = {name: value for name, value in self.session.cookies.items()}
            with open(self.cookie_file, 'w', encoding='utf-8') as f:
                json.dump(cookies, f, ensure_ascii=False, indent=2)
            logger.info('Cookies saved successfully')
        except IOError as e:
            logger.error(f'Failed to save cookies: {e}')
    
    def _weapi_request(self, endpoint: str, data: dict) -> dict:
        """
        Make a request to the weapi endpoint.
        
        Args:
            endpoint: API endpoint path
            data: Request data dictionary
            
        Returns:
            JSON response as dictionary
        """
        url = f'{self.BASE_URL}/weapi{endpoint}'
        encrypted = NetEaseCrypto.encrypt_request(json.dumps(data))
        
        try:
            response = self.session.post(url, data=encrypted)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f'Request failed: {e}')
            return {'code': -1, 'message': str(e)}
    
    def _api_request(self, endpoint: str, data: Optional[dict] = None) -> dict:
        """
        Make a request to the api endpoint.
        
        Args:
            endpoint: API endpoint path
            data: Optional request data dictionary
            
        Returns:
            JSON response as dictionary
        """
        url = f'{self.BASE_URL}/api{endpoint}'
        
        try:
            if data:
                response = self.session.post(url, data=data)
            else:
                response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f'Request failed: {e}')
            return {'code': -1, 'message': str(e)}
    
    def get_qr_key(self) -> Optional[str]:
        """
        Get QR code key for login.
        
        Returns:
            QR code unique key or None if failed
        """
        data = {'type': 1}
        result = self._weapi_request('/login/qrcode/unikey', data)
        
        if result.get('code') == 200:
            unikey = result.get('unikey')
            logger.info(f'QR key obtained: {unikey}')
            return unikey
        else:
            logger.error(f'Failed to get QR key: {result}')
            return None
    
    def generate_qr_code(self, qr_key: str, save_path: str = 'qrcode.png') -> str:
        """
        Generate QR code image for login.
        
        Args:
            qr_key: QR code unique key
            save_path: Path to save QR code image
            
        Returns:
            Path to saved QR code image
        """
        qr_url = f'https://music.163.com/login?codekey={qr_key}'
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(save_path)
        
        logger.info(f'QR code saved to {save_path}')
        return save_path
    
    def check_qr_status(self, qr_key: str) -> dict:
        """
        Check QR code scan status.
        
        Args:
            qr_key: QR code unique key
            
        Returns:
            Status dictionary with code:
            - 800: QR code expired
            - 801: Waiting for scan
            - 802: Scanned, waiting for confirmation
            - 803: Login successful
        """
        data = {'key': qr_key, 'type': 1}
        return self._weapi_request('/login/qrcode/client/login', data)
    
    def qr_login(self, timeout: int = 120) -> bool:
        """
        Perform QR code login flow.
        
        Args:
            timeout: Maximum time to wait for login in seconds
            
        Returns:
            True if login successful, False otherwise
        """
        # Get QR key
        qr_key = self.get_qr_key()
        if not qr_key:
            return False
        
        # Generate and display QR code
        qr_path = self.generate_qr_code(qr_key)
        print(f'\n请使用网易云音乐APP扫描二维码登录')
        print(f'QR code saved to: {qr_path}')
        print('Please scan the QR code with NetEase Music app\n')
        
        # Also print QR code to terminal
        try:
            qr_url = f'https://music.163.com/login?codekey={qr_key}'
            qr = qrcode.QRCode(box_size=1, border=1)
            qr.add_data(qr_url)
            qr.make(fit=True)
            qr.print_ascii(invert=True)
        except Exception as e:
            logger.warning(f'Could not print QR code to terminal: {e}')
            print('(Terminal QR code not available, please use the saved image)')
        
        # Wait for scan
        start_time = time.time()
        while time.time() - start_time < timeout:
            status = self.check_qr_status(qr_key)
            code = status.get('code')
            
            if code == 800:
                logger.warning('QR code expired, please try again')
                return False
            elif code == 801:
                print('.', end='', flush=True)
            elif code == 802:
                print('\n扫描成功，请在手机上确认登录...')
                print('Scanned! Please confirm on your phone...')
            elif code == 803:
                print('\n登录成功！')
                print('Login successful!')
                self._save_cookies()
                return True
            
            time.sleep(2)
        
        logger.warning('Login timeout')
        return False
    
    def get_user_account(self) -> dict:
        """
        Get current user account info.
        
        Returns:
            User account info dictionary
        """
        return self._api_request('/nuser/account/get')
    
    def is_logged_in(self) -> bool:
        """
        Check if user is logged in.
        
        Returns:
            True if logged in, False otherwise
        """
        result = self.get_user_account()
        return result.get('code') == 200 and result.get('account') is not None
    
    def refresh_ip_session(self) -> bool:
        """
        Refresh the IP session to maintain overseas access.
        
        This simulates accessing NetEase with a Chinese IP header,
        which helps maintain access for overseas users.
        
        Returns:
            True if refresh successful, False otherwise
        """
        logger.info('Refreshing IP session...')
        
        # Make a request with the China IP header to refresh session
        try:
            response = self.session.get(
                f'{self.BASE_URL}/discover',
                headers={'X-Real-IP': self.CHINA_IP}
            )
            
            if response.status_code == 200:
                logger.info('IP session refreshed successfully')
                self._save_cookies()
                return True
            else:
                logger.warning(f'IP refresh returned status: {response.status_code}')
                return False
                
        except requests.RequestException as e:
            logger.error(f'Failed to refresh IP session: {e}')
            return False
    
    def daily_sign_in(self, sign_type: int = 0) -> dict:
        """
        Perform daily sign-in task.
        
        Args:
            sign_type: 0 for PC, 1 for mobile
            
        Returns:
            Sign-in result dictionary
        """
        data = {'type': sign_type}
        result = self._weapi_request('/point/dailyTask', data)
        
        if result.get('code') == 200:
            logger.info(f'Daily sign-in successful (type={sign_type})')
        elif result.get('code') == -2:
            logger.info('Already signed in today')
        else:
            logger.warning(f'Daily sign-in failed: {result}')
        
        return result
    
    def logout(self):
        """Clear session and cookies."""
        self.session.cookies.clear()
        if os.path.exists(self.cookie_file):
            os.remove(self.cookie_file)
        logger.info('Logged out successfully')


if __name__ == '__main__':
    # Simple test
    client = NetEaseClient()
    
    if client.is_logged_in():
        print('Already logged in!')
        account = client.get_user_account()
        if account.get('profile'):
            print(f"Welcome, {account['profile'].get('nickname', 'User')}!")
    else:
        print('Not logged in. Starting QR login...')
        if client.qr_login():
            account = client.get_user_account()
            if account.get('profile'):
                print(f"Welcome, {account['profile'].get('nickname', 'User')}!")
