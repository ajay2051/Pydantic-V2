import os
from pydantic import Field, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict

os.environ["PRODUCTION_AUTH_KEY"] = 'test_auth_key'
os.environ["PRODUCTION_MY_API_KEY"] = 'test'
os.environ["PRODUCTION_ENV2"] = 'https://superurl.com'


class Settings(BaseSettings):
    """
    Base Settings extract the values from .env files
    """
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='production_',
        extra='ignore')

    service_name: str = Field(default='default')
    auth_key: str
    api_key: str = Field(alias='my_api_key')
    url: str = Field(validation_alias=AliasChoices("env1", "env2"))  # Evaluate from left to right


print(Settings().model_dump())
