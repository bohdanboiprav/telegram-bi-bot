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

    #model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa


settings = Settings()
