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
    PUBLIC_KEY = '010001'
    # Correct RSA modulus for NetEase Cloud Music weapi encryption
    MODULUS = (
        '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
        'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
        '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
        '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
        '3ece0462db0a22b8e7'
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
            NetEaseCrypto.MODULUS
        )
        
        return {
            'params': params.decode('utf-8'),
            'encSecKey': enc_sec_key
        }

    @staticmethod
    def md5(text: str) -> str:
        """Calculate MD5 hash of text."""
        return hashlib.md5(text.encode('utf-8')).hexdigest()
