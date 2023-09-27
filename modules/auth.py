import hashlib
import hmac
import base64
import time
import urllib3
from modules import BaseModule
from pydantic import BaseModel


class NcloudAuth(BaseModule):
    def __init__(self, model: BaseModel, name: str, log_level: str, expose_dnager: bool = True):
        super().__init__(name, log_level, expose_dnager)
        self.model=model
    
    def make_signature(self, timestamp: float, uri: str, method: str):