import requests






def check_api_calls(content):
    # print(content)
    for item in content:
      for key, value in item.items():
          if key == 'house':
              house_api(value)
          elif key == 'business':
              business_api(value)
          elif key == 'stock':
              stock_api(value)



def house_api(queries):
    print(queries)
    # ? createa --- https://developer.domain.com.au/docs/latest/getting-started/creating-first-project
    # ? Houses prices- https://developer.domain.com.au/docs/latest/apis/pkg_properties_locations/references/suburbperformance_get_bynamedsuburb_withoutpostcode


def business_api(queries):
    print(queries)
    # ? News api- https://newsapi.org/
# ! Also needs an api key which i have but might change i dunno


def stock_api(queries):
    print(queries)
# ? Stock prices- https://au.finance.yahoo.com/
