import requests


# from conf.config import settings

def get_news(n_results: int = 3):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8e36a9daff9841de9fdbcf891366b061'
    response = requests.get(url).json()
    data = response['articles'][0:n_results]
    print(response['articles'])
    return data


if __name__ == '__main__':
    get_news()
