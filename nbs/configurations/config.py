import os
from pydantic import BaseSettings , Field
from functools import lru_cache

os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

class Settings(BaseSettings):
    ASTRA_DB_CLIENT_ID : str
    ASTRA_DB_CLIENT_SECRET : str
    

    class Config:   
        env_file = 'conf.txt'


@lru_cache
def get_settings():
    return Settings()
