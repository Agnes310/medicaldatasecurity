from Crypto.Cipher import AES
import random
import sys
import base64

import json
class Cipher(object):
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs).encode("ascii")

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

key="12345678901234561234567890123456"
print(len(key))
msg="hello"
cipher = Cipher(key.encode("utf8"))

encrypted = cipher.encrypt(msg.encode("utf8"))

print("Message: ",msg)
print("Encrypted Content: ",encrypted)


cipher = Cipher(key.encode("utf8"))
decrypted = cipher.decrypt(encrypted)
print("Encrypted Content: ",encrypted)
print("Decrypted Content: ",decrypted)
