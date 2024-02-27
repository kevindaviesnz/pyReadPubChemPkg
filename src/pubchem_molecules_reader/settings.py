#from pydantic_settings import BaseSettings, SettingsConfigDict
import logging
import os


class Settings(BaseSettings):
     LOG_LEVEL: int = logging.INFO
 
SettingsProvider = Settings()
