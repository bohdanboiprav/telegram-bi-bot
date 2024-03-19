# Python Telegram Bot with AIogram

Welcome to the README for our Business Analytics Telegram bot! This bot, powered by the AIogram library, is designed to provide users with a seamless experience of retrieving various types of data from different sources. Let's dive into the details of what this bot can do and how it works.

## Overview

Our Python Telegram bot is a versatile tool that leverages web scraping, API integration, and database management to fetch and deliver real-time data to users. It operates on a scheduled basis using cron tasks to ensure that the information provided is always up-to-date. The bot is hosted on KOYEB Servers, utilizing a PostgreSQL database for data storage.

## Features

- **Web Scraping**: Utilizing BeautifulSoup and the requests library, the bot scrapes data from multiple websites, ensuring a comprehensive range of information.
- **API Integration**: The bot connects with the NewsAPI.org API to retrieve live top-5 business news in the United States, offering users access to the latest developments in the finance sector.
- **Database Management**: Data fetched by the bot is stored efficiently in a PostgreSQL database, enabling quick and organized access for users.
- **User-Friendly Commands**: The bot offers a range of commands that users can easily input to retrieve specific data sets. These commands include:
    - `/start`: Initiates the bot with a warm greeting message, welcoming users to the platform.
    - `/stock_tracker`: Retrieves up-to-date stock prices, providing valuable insights for investors.
    - `/crypto_tracker`: Fetches the latest cryptocurrency prices, catering to the growing interest in digital assets.
    - `/news_tracker`: Delivers the top 5 news articles in the finance domain, ensuring users stay informed about market trends.
    - `/gdp_tracker`: Presents GDP data on various countries, offering a macroeconomic perspective to users.
    - `/other_trackers`: Provides a list of additional trackers available, such as COVID statistics, expanding the bot's utility beyond financial data.
    - `/help`: Offers users a convenient list of available commands, ensuring smooth navigation within the bot interface.

## Usage

To begin using our Python Telegram bot, follow these simple steps:

1. **Open the link**: https://t.me/assistantba_bot
2. **Start the Bot**: Send the `/start` command to initiate the bot and receive a friendly greeting message.
3. **Explore Commands**: Use the available commands listed above to access the desired data. Whether you're interested in stocks, cryptocurrencies, news, or other trackers, our bot has you covered.
4. **Stay Informed**: Enjoy the convenience of accessing real-time data directly through the Telegram bot interface. Stay informed and make informed decisions with ease!

## Contributions

We welcome contributions from the community to enhance the functionality and usability of our bot. Whether you have suggestions for new features, improvements to existing ones, or bug fixes, we appreciate your input. Feel free to submit issues or pull requests on our GitHub repository.

## Disclaimer

While we strive to provide accurate and reliable data through our bot, please note that all information is provided for informational purposes only. We do not guarantee the accuracy or completeness of the data, and users are encouraged to conduct their own research before making any decisions based on the information provided by the bot.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Authors**: Bohdan Boiprav & Catalin Bondari
