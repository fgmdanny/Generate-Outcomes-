import requests
import json
import random

news_api_url = "https://newsapi.org/v2/top-headlines"
news_api_key = "<your_api_key_here>" 

stats_api_url = "<your_stats_api_url_here>"
stats_api_key = "<your_api_key_here>" 

def get_news_data():
    news_params = {
        "country": "us",
        "category": "business",
        "apiKey": news_api_key
    }
    response = requests.get(news_api_url, params=news_params)
    if response.status_code == 200:
        news_data = json.loads(response.text)
        return news_data["articles"]
    else:
        return None

def get_stats_data():
    stats_params = {
        "country": "us",
        "indicator": "gdp",
        "apiKey": stats_api_key
    }
    response = requests.get(stats_api_url, params=stats_params)
    if response.status_code == 200:
        stats_data = json.loads(response.text)
        return stats_data["data"]
    else:
        return None

news_articles = get_news_data()
stats_data = get_stats_data()

random_article = random.choice(news_articles)
random_stat = random.choice(stats_data)

print(f"Based on recent news, {random_article['title']}. In addition, the latest {random_stat['indicator']} data shows {random_stat['value']}.")
