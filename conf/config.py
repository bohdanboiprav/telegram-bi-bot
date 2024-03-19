# This file contains the configuration settings for the bot.
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


# Class to store the configuration settings
class Settings(BaseSettings):
    BOT_TOKEN: str
    ENDPOINT: str
    PORT: int
    DB_USER: str
    DBNAME: str
    PASSWORD: str
    NEWS_API_KEY: str


settings = Settings()  # Creating an instance of the Settings class

"""In the above code snippet, we have defined a Settings class that inherits from the BaseSettings class provided 
by the pydantic_settings library. This class contains the configuration settings required for the bot, such as the 
bot token, database connection details, and the news API key. The settings object is an instance of the Settings class 
that can be used to access these configuration settings in other parts of the code."""
