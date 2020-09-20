import requests


# https://openweathermap.org/current
# https://rapidapi.com/
# https://rapidapi.com/blog/most-popular-api/?utm_source=google&utm_medium=cpc&utm_campaign=Beta_100613405446&utm_term=%2Bapi_b&gclid=CjwKCAjw4_H6BRALEiwAvgfzq3sYd82izYNJ5b_plcFA-SnWqrI-7ZvYfPJBgeDdKc5pt__GfmkwzRoCPHAQAvD_BwE

def weatherAPI(place):
    # place = input("Enter the place name : ")
    key = "&APPID=d0ec1e64923de97d0a8e1d7fb596aee3"
    api_address = "https://api.openweathermap.org/data/2.5/weather?q=" + place + key
    json_data = requests.get(api_address).json()
    return json_data
# place = "damauli"
# json_data = weatherAPI(place)
# key = list(json_data.keys())
# if 'weather' in key:
#     weather = json_data['weather'][0]['main']
#     temp = json_data['main']['temp_max']
#     print(weather)
#     # print(f"temp_min: {temp['temp_min']} and temp_max: {temp['temp_max']}")
#     # print(temp)
#     print(json_data['main']['temp_max']-273.15)
#     print(json_data)
# else:
#     print(json_data['message'])


# https://api.nasa.gov/
# def nasaAPI():
#     # place = input("Enter the place name : ")
#     api_address = "https://api.nasa.gov/planetary/apod?api_key=1KLI1UPQpeAutltU5NFXcDFgQY0YYTLYU5Hb9qbr"
#     json_data = requests.get(api_address).json()
#     return json_data
# out = nasaAPI()
# print(out)


def covid(count):
    url = "https://covid-19-data.p.rapidapi.com/country"
    country = count
    querystring = {"format": "json", "name": country}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "857458162fmshed714e4075c6415p1334a3jsn31fbef49ebfc"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()
# countr = "south africa"
# data = covid(countr)
# print(len(data))
# if len(data) == 0:
#     print('country wrong')
# else:
#     for i in range(len(data)):
#         confirmed = data[i]['confirmed']
#         recovered = data[i]['recovered']
#         critical = data[i]['critical']
#         deaths = data[i]['deaths']
#         print(confirmed, recovered, critical, deaths)
# print(data)


# https://rapidapi.com/apilayernet/api/rest-countries-v1?endpoint=53aa5a09e4b051a76d24136a
def RestCountries(country):
    url = "https://restcountries-v1.p.rapidapi.com/name/" + country
    headers = {
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
        'x-rapidapi-key': "857458162fmshed714e4075c6415p1334a3jsn31fbef49ebfc"
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()
# nat = 'npoo'  # 'united kingdom'
# countryIn = RestCountries(nat)
# [country_name , calling_codes] =['']*2
# if type(countryIn) == list:
#     for i in range(len(countryIn)):
#         if ((countryIn[i]['name']).lower() == nat.lower()) or ((countryIn[i]['alpha2Code']).lower() == nat.lower()) or (
#                 (countryIn[i]['alpha3Code']).lower() == nat.lower()) or (
#                 (countryIn[i]['topLevelDomain'][0][1:]).lower() == nat.lower()):
#             capital = countryIn[i]['capital']
#             region = countryIn[i]['region']
#             population = countryIn[i]['population']
#             area = countryIn[i]['area']
#             borders = countryIn[i]['borders']
#             currencies = countryIn[i]['currencies'][0]
#             calling_codes = countryIn[i]['callingCodes'][0]
#             country_name = countryIn[i]['name']
#             print(country_name)
#             # print(countryIn[i])
#             print(calling_codes)
#             print(capital)
#             print(region)
#             print(population)
#             print(area)
#             print(borders)
#             print(currencies)
# else:
#     error_msg = countryIn['message']
# print(country_name)
# if country_name:
#     print('yes')
# else:
#     print('no')
# print(countryIn)
# print(calling_codes)
# print(capital)
# print(region)
# print(population)
# print(area)
# print(borders)
# print(currencies)



# https://newsapi.org/docs/get-started
# sort_by='latest' , 'popularity'
def newsAPI(category):
    url = ('http://newsapi.org/v2/everything?'
           'q='+category+'&'
           'sortBy=latest&'
           'apiKey=04ce00363b534259b0a7d157fe0cd4d3')
    response = requests.get(url)
    return response.json()

# category='mobile'
# news = newsAPI(category)
# print(news)
# if len(news['articles'])>0:
#     print(news['articles'][0]['title'],news['articles'][0]['url'])
#     print(news['articles'][1]['title'])
#     print(news['articles'][2]['title'])
# else:
#     print('No title')
