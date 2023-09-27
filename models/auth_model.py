from pydantic import BaseModel, SecretStr, field_serializer, validator
from pydantic.dataclasses import dataclass


@dataclass
class Region(BaseModel):
    region: str
    
    @validator("region")
    def validate_region(cls, v):
        allowed_values=["KR-1" ,"KR-2", "KR-GOV-1"]
        if v not in allowed_values:
            raise ValueError(f"Region must be one of {', '.join(allowed_values)}.")
        return v


class AuthModel(BaseModel):
    access_key: SecretStr
    secret_key: SecretStr
    region: Region
    
    @field_serializer("access_key", "secret_key", when_used="json")
    def reveal_secret(self, sensitive_value):
        return sensitive_value.get_secret_value()