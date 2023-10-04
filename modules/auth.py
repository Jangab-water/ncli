import requests
import hashlib
import hmac
import base64
from typing import Optional

from models.auth_model import AuthModel, ResourceModel
from modules import BaseModule


class NcloudAuth(BaseModule):
    def __init__(self, auth_model: AuthModel, resource_model: ResourceModel, name: str, log_level: str, addon_header: Optional[dict]=None):
        super().__init__(name, log_level)
        self.auth_model=auth_model
        self.resource_model=resource_model
        self.addon_header=addon_header
        
        signature=self.__make_signature()
        self.headers=self.__build_header(signature)
        

    def __make_signature(self):
        self.logger.debug("Build signature key.")
        timestamp=self.resource_model.timestamp*1000
        timestamp_casted=str(int(self.resource_model.timestamp))
        method=self.resource_model.method
        uri=self.resource_model.uri
        
        access_key=self.auth_model.reveal_secret(self.auth_model.access_key)
        secret_key=self.auth_model.reveal_secret(self.auth_model.secret_key)
        
        secret_key_casted=bytes(secret_key, 'UTF-8')
        message=method+" "+uri+"\n"+timestamp_casted+"\n"+access_key
        message_casted=bytes(message, 'UTF-8')
        
        signature=base64.b64encode(hmac.new(secret_key_casted, message, digestmod=hashlib.sha256).digest())
        return signature
    
    def __build_header(self, signature: any):
        self.logger.debug("Build authz headers.")
        headers={
            "x-ncp-apigw-timestamp":self.resource_model.timestamp,
            "x-ncp-iam-access-key":self.auth_model.reveal_secret(self.auth_model.access_key),
            "x-ncp-apigw-signature-v2":signature
        }
        if self.addon_header: headers.update(self.addon_header)
        return headers
    
    def open_request(self, gateway_domain: str):
        res=requests.