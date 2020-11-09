## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- good

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- ok
- okay
- right
- yaa
- ya

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good
- fine
- nice

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
- who r u

## intent:ask_residence
- where do you live
- in which city do you live
- whats your residence
- wheres your home
- where r u from
- where are you
- your city
- your town
- whats your hometown
- where do you stay
- where's your residence
- what is your city
- where are you staying
- where do u stay
- what's ur job

## intent:check_balance
- what is my balance
- how much do I have on my [savings](source_account)
- how much do I have on my [savings account]{"entity": "source_account", "value": "savings"}
- Could I pay in [yen](currency)?
- money in [dollar](currency)
- balance in [rupee](currency)

## intent:buy_phone_laptop
- I would like to buy a [phone](category)
- buy me [smart phone]{"entity": "category", "value": "phone"}
- I wanna buy a [smart phones]{"entity": "category", "value": "phone"}
- Im interested in purchasing a [smartphone]{"entity": "category", "value": "phone"}
- I want [mobile]{"entity": "category", "value": "phone"}
- I want to buy a [mobilephones]{"entity": "category", "value": "phone"}
- give me some recommendations for [mobile phones]{"entity": "category", "value": "phone"}
- can u recommend me [mobile phone]{"entity": "category", "value": "phone"}
- I wanted to purchase a [phone](category)
- I want to buy a [laptop](category)
- Please suggest me a good [laptop](category)
- Can you recommend me a [laptop](category)
- Can you suggest a [laptops]{"entity": "category", "value": "laptop"}
- want [samsung](phone_name)
- i got [iphone](phone_name) [mobile]{"entity": "category", "value": "phone"}
- like to get [redmi](phone_name)
- i want to buy [mobile phone]{"entity": "category", "value": "phone"}
- i want to buy [laptop](category)
- want to buy [laptop](category)
- buy [laptop](category)
- i want to buy [smart](category) [mobile phone]{"entity": "category", "value": "phone"}

## intent:latest_news
- Whats the latest news with [phones](category)
- Can you tell me about the trends regarding [phones](category)
- Any new releases for [mobiles]{"entity": "category", "value": "phone"}, whats the news
- update me on the [mobile]{"entity": "category", "value": "phone"} news
- news on new or latest [smart phone]{"entity": "category", "value": "phone"}
- show me the latest news for [mobiles](category)
- latest [mobile]{"entity": "category", "value": "phone"} on market
- Whats going in the tech world for [laptop](category)
- Can you show me the trends in [laptops]{"entity": "category", "value": "laptop"}
- latest [360 laptop]{"entity": "category", "value": "laptop"} on market
- new feature on latest [mobile]{"entity": "category", "value": "phone"}
- latest [phone](category) news
- [Finland](country) latest news on [politic](category)
- [mobile]{"entity": "category", "value": "phone"} news
- [politic](category) news
- news

## intent:give_information
- I'm looking for 4 GB RAM
- I would like 10 GB RAM
- around 16 GB RAM
- 8 GB RAM
- 2 GB RAM
- 16
- around 8 GB RAM
- I want a camera of 65 megapixel
- I'm looking for 15 megapixel
- Well around 50 mp camera
- 25 megapixel camera
- 20 mp camera
- 25
- A camera of 40 mp
- Well I would like 25 mp
- I was looking for 4000 mah battery backup
- 3500 mah battery
- battery 3000 mah
- I am looking for 5000 mah  battery
- Well the battery should be 4300 mah
- battery 3300 mah capacity
- 3000
- wants 4 GB RAM , good camera 50 mp and 3000 mah battery capacity
- 8
- 5 hr
- 200
- 2 gb ram
- 3000 mah
- 50 mp

## intent:budget_available
- my budget is around 400 usd
- Well I can spend around 300 usd budget
- my total spending on the phone can be 250 usd
- I can shell out approx 450 usd budget
- well its around 500 usd
- budget 900 usd
- money around 500 usd
- 200 usd money
- 500 usd
- 400 usd

## intent:out_of_scope
- blablablablalblab
- asdasdasdasd
- hmmmmmm
- haa
- haha
- hahaha
- .....
- where are you
- what do you
- ..@67890
- what else can you do
- whats the weather update
- im sleeping
- hahahaha
- hehehe
- ...

## intent:food_request
- I'd like beef [tacos](food) and a [burrito](food)
- How about some [mapo tofu](food)
- i like to have [momo](food)
- do u like to eat chicken [roast](food)
- have to tried [pork momo]{"entity": "food", "value": "momo"}
- get me full [chaumin](food)
- let's have [thupa](food) soup
- bring me [roast](food) tonight
- cook [noodle](food) for breakfast
- hot [samosa](food) are testy
- do u like [aalu chop](food)
- Where can i find [mutton](food) soup restaurants
- what u like, boiled or fried [egg](food)
- which curry do u like [chicken](food), [pork](food), [fist](food) or [buff](food)
- can i have [beef](food) [roast](food)
- can we have 2 plate [mo:mo]{"entity": "food", "value": "momo"} with drinks

## intent:weather_place_status
- [kathmandu](place) weather forecasts
- tell me [ktm]{"entity": "place", "value": "kathmandu"} today's weather
- can u forecasts [pokhara](place) weather
- today's [pkr]{"entity": "place", "value": "pokhara"}
- weather status of [dharan](place)
- weather in [new york](place)
- show me today weather on [dang](place)
- [Dadeldhura](place) weather
- [Dipayal](place) weather data
- [dang](place) weather
- weather in [tanahun](place)
- weather in [new delhi](place)
- [london](place) weather
- weather in [uk](country)
- weather data in [nepal](country)
- weather in [Tuvalu](country)
- [USA](country) weather data
- what is [Romania](country) weather
- what is the weather is [mumbai](place)
- [tokyo](place) weather
- [us]{"entity": "country", "value": "USA"} weather
- what is weather be in [Romania](country)
- weaather [ofnepal](country)
- weather data
- weather news on [Oman](country)
- [Iceland](country) weather news

## intent:give_city_place
- Dadeldhura
- Dipayal
- Dhangadi
- Birendranagar
- Nepalgunj
- Jumla
- Dang
- Pokhara
- Bhairahawa
- Simara
- Kathmandu
- Okhaldhunga
- Taplejung
- Dhankuta
- Biratnagar
- Jomsom
- Dharan
- Lumle
- Janakpur
- Jiri
- kathmandu
- pokhara
- london
- new york
- [japan](country)
- [nepal](country)
- dharan
- [new delhi](place)
- nepaaaaalloi

## intent:ask_weather
- what is the today's weather
- weather forecasts
- tell me today's weather
- how is the weather today
- is it rainy today
- what's the temperature today
- weather status
- is it sunny?
- will it be rainy today?
- is today rainy, sunny or modorate
- today's temperature
- weather in condition
- can u tell me about today's weather condition?
- What's the weather going to be like.
- is it cloudy
- what is weather be today
- today's weather
- weather news
- update on weather data
- latest news on weather forecasts
- what's the news on weather

## intent:General_country_quest
- what is the [capital](attribute) of [nepal](country)
- what is the [population](attribute) of [united kingdom](country)
- what is the [area](attribute) of [india](country)
- what is the [currencies](attribute) of the [china](country)
- [code](attribute) of [South Korea](country) to call
- what is the [calling code]{"entity": "attribute", "value": "code"} of the [russia](country)
- [maldives](country) [telephone code]{"entity": "attribute", "value": "code"}
- in which region is [saudi arabia](country) located?
- in which [region](attribute) is country [maxico](country) located.
- [boarder](attribute) country or [neighbour country]{"entity": "attribute", "value": "boarder"} of [sri lanka](country)
- Give general information of country? [brazil](country)
- basic information about [Denmark](country)
- short information about country [United States]{"entity": "country", "value": "USA"}
- [usa]{"entity": "country", "value": "USA"} [capital](attribute)
- general info of [Turkey](country)
- what is [code](attribute) to call in
- what is [area](attribute) of [bhutan](country)
- what is the [area](attribute) of [chile](country)
- information on [uruguay](country)
- what is the [area](attribute) of [bangladesh](country)
- give me [calling code]{"entity": "attribute", "value": "code"}
- what is [calling](attribute) [code](attribute) of [peru](country)
- what is [area](attribute) [canada](country)
- give me information about [sudan](country)
- [india](country)

## intent:covid19_case
- covid case in [germany](country)
- [United States]{"entity": "country", "value": "USA"} covid19 conform case
- [Spain](country) covid-19 virus death
- recovered case of covid in [United Kingdom]{"entity": "country", "value": "uk"}
- covid status in my place [italy](country)
- covid data of [Nepal](country)
- how many people are dead by corona virus in [france](country)?
- what is the virus case in [iraq](country)
- [iran](country) corona virus case
- corona case in [Libya](country)
- give me corona update on [us]{"entity": "country", "value": "USA"}
- corona case in [Zambia](country)
- [japan](country) corona case
- corona case
- corona detail
- [Qatar](country) covid case

## intent:req_math_que
- ask me math question
- let's play math quiz
- [addition]{"entity": "math_operation", "value": "add"}
- [subtraction]{"entity": "math_operation", "value": "sub"}
- [multiply]{"entity": "math_operation", "value": "mult"}
- [division]{"entity": "math_operation", "value": "div"}
- ask me add question
- sub question

## synonym:25 mp
- 25 megapixel

## synonym:USA
- us
- United States
- usa
- united states of america

## synonym:boarder
- neighbour country
- side country
- nearest country

## synonym:code
- calling code
- telephone code

## synonym:currency_unit
- yen
- dollar
- rupee
- euro
- riyal
- Yuan

## synonym:kathmandu
- ktm

## synonym:laptop
- laptops
- 360 laptop

## synonym:momo
- pork momo
- mo:mo

## synonym:phone
- smart phone
- smart phones
- smartphone
- mobile
- mobilephones
- mobile phones
- mobile phone
- mobiles

## synonym:pokhara
- pkr
- pkt

## synonym:savings
- savings account

## synonym:uk
- United Kingdom

## lookup:place
  data/lookup_table/place_lookup.txt

## lookup:country
  data/lookup_table/countryLookup.txt
