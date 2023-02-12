import requests
from datetime import datetime, timedelta

API_KEY = 'a931d65d2e564a9d9959d549fc4f3d9e'
today = datetime.today()
one_week_ago = today - timedelta(days=7)
date = one_week_ago.strftime("%Y-%m-%d")

def check_api_calls(content):
    # print(content)
    for item in content:
      for key, value in item.items():
          if key == 'house':
              house_api(value)
          elif key == 'news':
              news_api(value)
          elif key == 'stock':
              stock_api(value)


def house_api(queries):
    print(queries)
    print("house")
    # ? createa --- https://developer.domain.com.au/docs/latest/getting-started/creating-first-project
    # ? Houses prices- https://developer.domain.com.au/docs/latest/apis/pkg_properties_locations/references/suburbperformance_get_bynamedsuburb_withoutpostcode




def news_api(queries):
    def query_by_country(country, query):
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&q={query}&apiKey={API_KEY}&language=en")
        content = response.json()
        # TODO sort the content
        # TODO add the content to message
        print(content)

        
    # TODO make the timeframe from datetime--- from=2023-01-08   this is format of it--- make these automatically one week apart with the to being current day and the from being current day minus 7-- dont need to put n the to beause it will auto be going up to that
    for query in queries:
        query_split = [query.lower() for query in query.split()]
        print(query_split)
        if query_split[0] == 'australian':
            country = 'au'
            query_by_country(country, query_split[1])
        elif query_split[0] == 'us':
            country = 'us'
            query_by_country(country, query_split[1])
        elif query_split[0] == 'global':
            response = requests.get(f"https://newsapi.org/v2/everything?q=election&from={date}&sortBy=publishedAt&apiKey={API_KEY}&language=en&pageSize=20")
            content = response.json()
            # TODO sort the content
            # TODO add the content to the message 
            print(content)
            print("global")

        
    


def stock_api(queries):
    print(queries)
# ? Stock prices- https://au.finance.yahoo.com/
