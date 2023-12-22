from pydantic import BaseModel
from typing import Union, List
from enum import Enum


class Region(Enum):
    KR="KR-1"


class Site(Enum):
    PUB=1
    GOV=2
    FIN=3


class AuthModel(BaseModel):
    ncloud_access_key: str
    ncloud_secret_key: str
    ncloud_region: str
    ncloud_site_endpoint: str