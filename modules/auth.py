import hashlib
import hmac
import base64
import time
import urllib3
from modules import BaseModule


class NcloudAuth(BaseModule):
    def __init__(self, access_key: str, secret_key: str, region: str, name: str, log_level: str, expose_dnager: bool = True):
        super().__init__(name, log_level, expose_dnager)
        