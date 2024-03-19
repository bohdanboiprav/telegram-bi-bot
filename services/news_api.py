# This file is used to get the news from the news api
import requests


# Function to get the news from the news api
def get_news(n_results: int = 3):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8e36a9daff9841de9fdbcf891366b061'
    response = requests.get(url).json()
    data = response['articles'][0:n_results]
    print(response['articles'])
    return data


if __name__ == '__main__':
    get_news()

"""In the above code snippet, we have defined a function get_news that takes the number of results as an argument and returns
the top headlines from the news API. The function sends a request to the news API and retrieves the top headlines for the
business category in the US. The API key is included in the URL for authentication. The function returns the top headlines
based on the number of results provided."""
