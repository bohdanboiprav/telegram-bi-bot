from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    ENDPOINT: str
    PORT: int
    DB_USER: str
    DBNAME: str
    PASSWORD: str
    NEWS_API_KEY: str


settings = Settings()
