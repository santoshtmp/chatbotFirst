## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## food_request
* food_request
  - utter_food_req_accept
* goodbye
  - utter_goodbye

## greet + show_latest_news
* greet
  - utter_greet
* latest_news
  - action_show_latest_news

## great + show_latest_news
* greet
    - utter_greet
* latest_news{"category":"laptop"}
    - slot{"category":"laptop"}
    - action_show_latest_news
    - slot{"category": null}
* latest_news{"category": "phone"}
    - slot{"category": "phone"}
    - action_show_latest_news
    - slot{"category": null}
* latest_news{"category": "politic"}
    - slot{"category": "politic"}
    - action_show_latest_news
    - slot{"category": null}

## buy_phone_laptop + form 
* buy_phone_laptop
  - product_search_form
  - form{"name":"product_search_form"}
  - form{"name":null}

## show_phones + form 
* buy_phone_laptop{"category":"phone"}
    - slot{"category":"phone"}
    - product_search_form
    - form{"name":"product_search_form"}
    - slot{"requested_slot":"ram"}
* give_information
    - product_search_form
    - slot{"ram":null}
* give_information
    - product_search_form
    - slot{"ram":8}
* give_information
    - product_search_form
    - slot{"battery":6000}
* give_information
    - product_search_form
    - slot{"camera":50}
* give_information
    - product_search_form
    - form{"name":null}
    - slot{"budget":500}

## phone_search_story_1
* buy_phone_laptop{"category": "phone"}
    - slot{"category": "phone"}
    - product_search_form
    - form{"name": "product_search_form"}
    - slot{"requested_slot": "ram"}
* form: give_information
    - form: product_search_form
    - slot{"ram": 2}
    - slot{"requested_slot": "battery"}
* form: give_information
    - form: product_search_form
    - slot{"battery": 3000}
    - slot{"requested_slot": "camera"}
    - form: followup{"name": "product_search_form"}
    - form: product_search_form
    - slot{"requested_slot": "camera"}
* form: give_information
    - form: product_search_form
    - slot{"camera": 50}
    - slot{"requested_slot": "budget"}
* form: out_of_scope
    - form: product_search_form
    - slot{"budget": null}
    - slot{"requested_slot": "budget"}
* form: budget_available
    - form: product_search_form
    - slot{"budget": 400}
    - slot{"ram": null}
    - slot{"camera": null}
    - slot{"battery_backup": null}
    - slot{"battery": null}
    - slot{"storage_capacity": null}
    - slot{"budget": null}
    - form{"name": null}
    - slot{"requested_slot": null}


## laptop_search_story_1
* buy_phone_laptop{"category": "laptop"}
    - slot{"category": "laptop"}
    - product_search_form
    - form{"name": "product_search_form"}
    - slot{"requested_slot": "ram"}
* form: give_information
    - form: product_search_form
    - slot{"ram": 8}
    - slot{"requested_slot": "battery_backup"}
* form: give_information
    - form: product_search_form
    - slot{"battery_backup": 5}
    - slot{"requested_slot": "storage_capacity"}
* form: give_information
    - form: product_search_form
    - slot{"storage_capacity": 200}
    - slot{"requested_slot": "budget"}
* form: budget_available
    - form: product_search_form
    - slot{"budget": 500}
    - slot{"ram": null}
    - slot{"camera": null}
    - slot{"battery_backup": null}
    - slot{"battery": null}
    - slot{"storage_capacity": null}
    - slot{"budget": null}
    - form{"name": null}
    - slot{"requested_slot": null}


## out_of_scope_intent
* out_of_scope
  - action_my_fallback

## General_country_quest with country and attribute
* General_country_quest{"country": "us", "attribute": "capital"}
    - slot{"attribute": "capital"}
    - slot{"country": "us"}
    - action_country_general_info
    - slot{"country": null}
    - slot{"attribute": null}

## General_country_quest with country
* General_country_quest{"country": "Turkey"}
    - slot{"country": "Turkey"}
    - action_country_general_info
    - slot{"country": null}
    - slot{"attribute": null}

## corona19 data story
* covid19_case{"country": "Zambia"}
    - slot{"country": "Zambia"}
    - action_covid
    - slot{"country": null}
* affirm
    - utter_happy
* covid19_case{"country": "germany"}
    - slot{"country": "germany"}
    - action_covid
    - slot{"country": null}
* covid19_case{"country": "japan"}
    - slot{"country": "japan"}
    - action_covid
    - slot{"country": null}
* covid19_case
    - action_covid
    - slot{"country": null}


## General_country_quest + covid19_case
* General_country_quest{"attribute": "code"}
    - slot{"attribute": "code"}
    - action_country_general_info
    - slot{"attribute": null}
* General_country_quest{"attribute": "code", "country": "Nepal"}
    - slot{"attribute": "code"}
    - slot{"country": "Nepal"}
    - action_country_general_info
    - slot{"country": null}
    - slot{"attribute": null}
* General_country_quest{"attribute": "area", "country": "ofnepal"}
    - slot{"attribute": "area"}
    - slot{"country": "ofnepal"}
    - action_country_general_info
    - slot{"country": null}
    - slot{"attribute": null}
* General_country_quest{"country": "sudan"}
    - slot{"country": "sudan"}
    - action_country_general_info
    - slot{"country": null}
    - slot{"attribute": null}
* covid19_case
    - action_covid
    - slot{"country": null}
* covid19_case{"country": "Qatar"}
    - slot{"country": "Qatar"}
    - action_covid
    - slot{"country": null}


## weather place together 
* weather_place_status
  - action_weather_state

## ask weather status
* ask_weather
  - weather_search_form
  - form{"name":"weather_search_form"}
  - form{"name":null}

## weather place together line-1
* weather_place_status{"place": "new york"}
    - slot{"place": "new york"}
    - action_weather_state
    - slot{"place": null}
    - slot{"country": null}
* weather_place_status{"country": "Romania"}
    - slot{"country": "Romania"}
    - action_weather_state
    - slot{"place": null}
    - slot{"country": null}
* weather_place_status
    - action_weather_state
* deny
    - utter_goodbye
* weather_place_status
    - action_weather_state
* ask_weather
    - weather_search_form
    - form{"name": "weather_search_form"}
    - slot{"requested_slot": "location"}
* form: give_city_place
    - form: weather_search_form
    - slot{"location": "london"}
    - slot{"place": null}
    - slot{"country": null}
    - slot{"location": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* weather_place_status
    - action_weather_state
* ask_weather
    - weather_search_form
    - form{"name": "weather_search_form"}
    - slot{"requested_slot": "location"}
* form: General_country_quest{"country": "india"}
    - slot{"country": "india"}
    - form: weather_search_form
    - slot{"location": "india"}
    - slot{"place": null}
    - slot{"country": null}
    - slot{"location": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* weather_place_status
    - action_weather_state
* mood_great
    - utter_happy
* ask_weather
    - weather_search_form
    - form{"name": "weather_search_form"}
    - slot{"requested_slot": "location"}
* form: give_city_place
    - form: weather_search_form
    - slot{"location": "new york"}
    - slot{"place": null}
    - slot{"country": null}
    - slot{"location": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_weather
    - weather_search_form
    - form{"name": "weather_search_form"}
    - slot{"requested_slot": "location"}
* form: give_city_place
    - form: weather_search_form
    - slot{"location": "dharan"}
    - slot{"place": null}
    - slot{"country": null}
    - slot{"location": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_weather
    - weather_search_form
    - form{"name": "weather_search_form"}
    - slot{"requested_slot": "location"}
* form: give_city_place{"place": "new delhi"}
    - slot{"place": "new delhi"}
    - form: weather_search_form
    - slot{"location": "new delhi"}
    - slot{"place": null}
    - slot{"country": null}
    - slot{"location": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_weather
    - weather_search_form
    - form{"name": "weather_search_form"}
    - slot{"requested_slot": "location"}
* form: give_city_place
    - form: weather_search_form
    - slot{"location": "nepaaaaalloi"}
    - slot{"place": null}
    - slot{"country": null}
    - slot{"location": null}
    - form{"name": null}
    - slot{"requested_slot": null}

