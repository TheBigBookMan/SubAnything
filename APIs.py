import requests

# ? Houses prices- https://developer.domain.com.au/docs/latest/apis/pkg_properties_locations/references/suburbperformance_get_bynamedsuburb_withoutpostcode

# ? News api- https://newsapi.org/
# ! Also needs an api key which i have but might change i dunno

# ? Stock prices- https://au.finance.yahoo.com/

def check_api_calls(content):
    # print(content)
    for item in content:
      for key, value in item.items():
          if key == 'house':
              house_api(value)
          elif key == 'business':
              business_api(value)



def house_api(queries):
    print(queries)


def business_api(queries):
    print(queries)