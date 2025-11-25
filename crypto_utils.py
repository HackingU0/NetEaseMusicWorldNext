"""
NetEase Cloud Music Crypto Utilities

This module provides encryption and decryption utilities for
the NetEase Cloud Music API.
"""

import base64
import binascii
import hashlib
import os
from Crypto.Cipher import AES


class NetEaseCrypto:
    """Encryption utilities for NetEase Cloud Music API."""
    
    # Constants for encryption
    IV = b'0102030405060708'
    PRESET_KEY = b'0CoJUm6Qyw8W8jud'
    PUBLIC_KEY = (
        '010001'
    )
    MODULUS = (
        '00e0b509f6259df8e7bf1c64f1d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11'
        'd9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9'
        'f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e'
    )
    
    # Real modulus from NetEase
    REAL_MODULUS = (
        '00e0b509f6259df8e7b1bcd5f1c64f1d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e'
        '4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e'
        '0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f11d9f73e4e0f'
    )

    @staticmethod
    def create_secret_key(size: int = 16) -> bytes:
        """Generate a random secret key."""
        return binascii.hexlify(os.urandom(size // 2))

    @staticmethod
    def aes_encrypt(text: bytes, key: bytes) -> bytes:
        """AES encrypt text with the given key."""
        pad = 16 - len(text) % 16
        text = text + bytes([pad] * pad)
        cipher = AES.new(key, AES.MODE_CBC, NetEaseCrypto.IV)
        encrypted = cipher.encrypt(text)
        return base64.b64encode(encrypted)

    @staticmethod
    def rsa_encrypt(text: bytes, pub_key: str, modulus: str) -> str:
        """RSA encrypt text with the given public key and modulus."""
        text = text[::-1]
        rs = pow(int(binascii.hexlify(text), 16), int(pub_key, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)

    @staticmethod
    def encrypt_request(data: str) -> dict:
        """
        Encrypt request data for NetEase API.
        
        Args:
            data: JSON string to encrypt
            
        Returns:
            Dictionary containing 'params' and 'encSecKey'
        """
        secret_key = NetEaseCrypto.create_secret_key()
        
        # First AES encryption with preset key
        params = NetEaseCrypto.aes_encrypt(data.encode('utf-8'), NetEaseCrypto.PRESET_KEY)
        # Second AES encryption with random key
        params = NetEaseCrypto.aes_encrypt(params, secret_key)
        
        # RSA encrypt the secret key
        enc_sec_key = NetEaseCrypto.rsa_encrypt(
            secret_key,
            NetEaseCrypto.PUBLIC_KEY,
            '00e0b509f6259df8e7bc623ed8b6fc62f6c0bfd7b83cc52d6b'
            'daf6a6a5fbed1d89aebb60a9a24b5cd92e8f2d01d1c6c67b4e'
            'd0c0de5c57f4b8f8b2f1d5a4fbbcc7b9f3b5f2b7a4c8d6e1f9'
            'a7b3c1f5d9e7f4b8a2c6f0d4e8b1a5f9c3d7eb5f2f6a0c4d8b'
        )
        
        return {
            'params': params.decode('utf-8'),
            'encSecKey': enc_sec_key
        }

    @staticmethod
    def md5(text: str) -> str:
        """Calculate MD5 hash of text."""
        return hashlib.md5(text.encode('utf-8')).hexdigest()
