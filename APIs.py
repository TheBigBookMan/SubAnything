import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

API_KEY = 'a931d65d2e564a9d9959d549fc4f3d9e'
today = datetime.today()
one_week_ago = today - timedelta(days=7)
date = one_week_ago.strftime("%Y-%m-%d")

def check_api_calls(content):
    list_content = []

    for item in content:
        for key, value in item.items():
            if key == 'house':
                house_content = house_api(value)
                list_content.append({"house": house_content})
            elif key == 'news':
                news_content = news_api(value)
                list_content.append({"news": news_content})
            elif key == 'stock':
                stock_content = stock_api(value)
                list_content.append({"stock": stock_content})
        
    return list_content


# ? will need to web scrape domain website

def house_api(queries):
    # print(queries)
    print("house")
    # query_suburbs = ""
    # for query in queries:
    #     single_query = ""
    #     split_query = query['suburb'].split(' ')
    #     print(split_query)
    #     for word in split_query:
    #         single_query = single_query + f"+{word.lower()}"

    #     if query == queries[-1]:
    #         single_query = single_query + f",+{query['state']}+{query['postcode']}"
    #     else:
    #         single_query = single_query + f",+{query['state']}+{query['postcode']}%3b"
        
    #     query_suburbs = query_suburbs + single_query
    
    # url = f'https://www.realestate.com.au/sold/property-house-in-{query_suburbs}/list-1?maxSoldAge=1-month&activeSort=solddate&source=refinement'

    # source_code = requests.get(url).text
    # print(source_code)




#? https://newsapi.org/docs/endpoints/top-headlines
def news_api(queries):
    news_list = []

    def query_by_country(country, query):
        response = requests.get(f'https://newsapi.org/v2/top-headlines?country={country}&q={query}&apiKey={API_KEY}&language=en&from={date}')
        content = response.json()
        articles = content['articles']
        body_articles = []
        for article in articles: 
            body = {
                "title": article['title'],
                "author": article['author'],
                "source": article['source']['name'],
                "description": article['description'],
                "url": article['url'],
                "publishedDate": article['publishedAt'],
                "content": article['content']
            }
            body_articles.append(body)
        news_list.append({query: body_articles})

    for query in queries:
        query_split = [query.lower() for query in query.split()]
        if query_split[0] == 'australian':
            country = 'au'
            query_by_country(country, query_split[1])
        elif query_split[0] == 'us':
            country = 'us'
            query_by_country(country, query_split[1])
        elif query_split[0] == 'global':
            response = requests.get(f'https://newsapi.org/v2/everything?q="{query_split[1]} startup"&from={date}&sortBy=publishedAt&apiKey={API_KEY}&language=en&pageSize=20')
            content = response.json()
            articles = content['articles']
            body_articles = []
            for article in articles: 
                body = {
                    "title": article['title'],
                    "author": article['author'],
                    "source": article['source']['name'],
                    "description": article['description'],
                    "url": article['url'],
                    "publishedDate": article['publishedAt'],
                    "content": article['content']
                }
                body_articles.append(body)
            news_list.append({query: body_articles})

    return news_list



def stock_api(queries):
    print(queries)
# ? Stock prices- https://au.finance.yahoo.com/
