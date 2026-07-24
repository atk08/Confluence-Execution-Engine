"""
Application configuration.
"""

from backend.config import settings

from dotenv import load_dotenv

load_dotenv()


class Settings:
    TWELVE_DATA_API_KEY = settings.TWELVE_DATA_API_KEY


settings = Settings()