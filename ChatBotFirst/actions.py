# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import re
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, UserUtteranceReverted, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from API import weatherAPI, RestCountries, covid, newsAPI


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ProductSearchForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "product_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        if tracker.get_slot('category') == 'phone':
            return ["ram", "battery", "camera", "budget"]
        elif tracker.get_slot('category') == 'laptop':
            return ["ram", "battery_backup", "storage_capacity", "budget"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {"ram": [self.from_text()],
                "camera": [self.from_text()],
                "battery": [self.from_text()],
                "budget": [self.from_text()],
                "battery_backup": [self.from_text()],
                "storage_capacity": [self.from_text()]
                }

    def validate_battery_backup(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        try:
            battery_backup_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            battery_backup_int = 500000
        # Query the DB and check the max value, that way it can be dynamic
        if battery_backup_int < 500000:
            return {"battery_backup": battery_backup_int}
        else:
            dispatcher.utter_message(template="utter_wrong_battery_backup")

            return {"battery_backup": None}

    def validate_storage_capacity(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        try:
            storage_capacity_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            storage_capacity_int = 500000
        # Query the DB and check the max value, that way it can be dynamic
        if storage_capacity_int < 2000:
            return {"storage_capacity": storage_capacity_int}
        else:
            dispatcher.utter_message(template="utter_wrong_storage_capacity")

            return {"storage_capacity": None}

    def validate_ram(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        try:
            ram_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            ram_int = 500000
        # Query the DB and check the max value, that way it can be dynamic
        if ram_int < 50:
            return {"ram": ram_int}
        else:
            dispatcher.utter_message(template="utter_wrong_ram")

            return {"ram": None}

    def validate_camera(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        try:
            camera_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            camera_int = 500000
        # Query the DB and check the max value, that way it can be dynamic
        if camera_int < 150:
            return {"camera": camera_int}
        else:
            dispatcher.utter_message(template="utter_wrong_camera")

            return {"camera": None}

    def validate_budget(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        try:
            budget_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            budget_int = 500000
        # Query the DB and check the max value, that way it can be dynamic
        if budget_int < 4000:
            return {"budget": budget_int}
        else:
            dispatcher.utter_message(template="utter_wrong_budget")

            return {"budget": None}

    def validate_battery(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        try:
            battery_int = int(re.findall(r'[0-9]+', value)[0])
        except:
            battery_int = 500000
        # Query the DB and check the max value, that way it can be dynamic
        if battery_int < 8000:
            return {"battery": battery_int}
        else:
            dispatcher.utter_message(template="utter_wrong_battery")

            return {"battery": None}

    # USED FOR DOCS: do not rename without updating in docs
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        ram = tracker.get_slot('ram')
        camera = tracker.get_slot('camera')
        battery = tracker.get_slot('battery')
        budget = tracker.get_slot('budget')
        battery_backup = tracker.get_slot('battery_backup')
        storage_capacity = tracker.get_slot('storage_capacity')

        if tracker.get_slot('category') == 'phone':
            dispatcher.utter_message(text="Searched phone items here.....RAM GB: " + str(ram) +
                                          ", Camera mp : " + str(camera) + ", battery mah : " + str(battery)
                                          + ", price around : " + str(budget))

        elif tracker.get_slot('category') == 'laptop':
            dispatcher.utter_message(text="Searched laptop items here.....RAM GB : " + str(ram) +
                                          ", battery backup hr : " + str(battery_backup) + ", storage :" +
                                          str(storage_capacity) + ", price around : " + str(budget))

        return [SlotSet('ram', None), SlotSet('camera', None), SlotSet('battery_backup', None),
                SlotSet('battery', None), SlotSet('storage_capacity', None), SlotSet('budget', None),
                SlotSet('category', None)]


class ActionShowLatestNews(Action):

    def name(self) -> Text:
        return "action_show_latest_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if tracker.get_slot('category'):
            category = tracker.get_slot('category')
            news = newsAPI(category)
            if len(news['articles']) > 0:
                title_1 = news['articles'][0]['title']
                url_1 = news['articles'][0]['url']
                title_2 = news['articles'][1]['title']
                title_3 = news['articles'][2]['title']
                dispatcher.utter_message(text="Here the latest news for  category" + str(category)+" are \nTitle_1 : " +
                                         str(title_1)+"\nTitle_2 : "+str(title_2)+"\nTitle_3 : "+str(title_3))
            else:
                no_msg = 'No title'
                dispatcher.utter_message(text="Here the latest news for your category......" + str(category)+'....'+str(no_msg))
        else:
            dispatcher.utter_message(text="Enter category doesn't exit, category=[mobile,laptop,phone,politic]")
        return [SlotSet('category', None)]


class MyFallback(Action):

    def name(self) -> Text:
        return "action_my_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_fallback")

        return []


class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("place") or tracker.get_slot("country"):
            place_input = tracker.get_slot("place") or tracker.get_slot("country")
            json_data = weatherAPI(place_input)
            key = list(json_data.keys())
            if 'weather' in key:
                weather = json_data['weather'][0]['main']
                temp = json_data['main']['temp_max'] - 273.15
                dispatcher.utter_message(
                    text=str(place_input) + " weather condition is " + str(weather) + " and the temperature is " + str(
                        temp) + " C ")
            else:
                msg = json_data['message']
                dispatcher.utter_message(text=str(place_input) + " -- " + str(msg))
            dispatcher.utter_message(text=" thank you ")
            return [SlotSet("place", None), SlotSet("country", None)]
        else:
            dispatcher.utter_message(template="utter_conform_weather")
            return []


class WeatherForm(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "weather_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["location"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"location": [self.from_text()]
                }

    # USED FOR DOCS: do not rename without updating in docs
    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],
               ) -> List[Dict]:
        place_input = tracker.get_slot("location")
        json_data = weatherAPI(place_input)
        key = list(json_data.keys())
        if 'weather' in key:
            weather = json_data['weather'][0]['main']
            temp = json_data['main']['temp_max'] - 273.15
            dispatcher.utter_message(
                text=str(place_input) + " weather condition is " + str(weather) + " and the temperature is " + str(
                    temp) + " C ")
        else:
            msg = json_data['message']
            dispatcher.utter_message(text=str(place_input) + " -- " + str(msg))
        dispatcher.utter_message(text="thank you ")
        dispatcher.utter_message(template="utter_submit", name=place_input)
        return [SlotSet("place", None), SlotSet("country", None), SlotSet("location", None)]


class YourResidence(Action):

    def name(self) -> Text:
        return "action_your_residence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_residence")

        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('name'))]


class ActionCovid(Action):
    def name(self) -> Text:
        return "action_covid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        country = tracker.get_slot('country')
        if country:
            covid_data = covid(country)
            if len(covid_data) == 0:
                dispatcher.utter_message(text="Please correct country name: " + str(country))
            else:
                for i in range(len(covid_data)):
                    confirmed = covid_data[i]['confirmed']
                    recovered = covid_data[i]['recovered']
                    critical = covid_data[i]['critical']
                    deaths = covid_data[i]['deaths']
                    dispatcher.utter_message(
                        text="corona data for country " + str(country) + " are: \nconfirmed case : " + str(confirmed) +
                             " \nrecovered case : " + str(recovered) + " \ncritical case : " + str(critical) +
                             "\ndeath case : " + str(deaths))
        else:
            dispatcher.utter_message(text="Please Re-enter with correct country name for covid data ")
        return [SlotSet("country", None)]


class ActionCountryGeneralInfo(Action):
    def name(self) -> Text:
        return "action_country_general_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        [capital, region, population, currencies, borders, area, code, error_msg, country_name] = ['']*9

        attribute = tracker.get_slot('attribute')
        if tracker.get_slot('country'):
            country = tracker.get_slot('country')
            countryIn = RestCountries(country)
            if type(countryIn) == list:
                for i in range(len(countryIn)):
                    if ((countryIn[i]['name']).lower() == country.lower()) or (
                            (countryIn[i]['alpha2Code']).lower() == country.lower()) or (
                            (countryIn[i]['alpha3Code']).lower() == country.lower()) or (
                            (countryIn[i]['topLevelDomain'][0][1:]).lower() == country.lower()):
                        country_name = countryIn[i]['name']
                        capital = countryIn[i]['capital']
                        region = countryIn[i]['region']
                        population = countryIn[i]['population']
                        area = countryIn[i]['area']
                        borders = countryIn[i]['borders']
                        currencies = countryIn[i]['currencies'][0]
                        code = countryIn[i]['callingCodes'][0]
            else:
                error_msg = countryIn['message']

        if country_name and attribute:
            if attribute == 'capital' and capital:
                dispatcher.utter_message(text=" The " + str(attribute) + " of the country " + str(country) + " is " +
                                              str(capital))
            elif attribute == 'region' and region:
                dispatcher.utter_message(
                    text=" The " + str(attribute) + " of the country " + str(country) + " is " + str(region))
            elif attribute == 'population' and population:
                dispatcher.utter_message(
                    text=" The " + str(attribute) + " of the country " + str(country) + " is " + str(population))
            elif attribute == 'area' and area:
                dispatcher.utter_message(
                    text=" The " + str(attribute) + " of the country " + str(country) + " is " + str(area))
            elif attribute == 'currencies' and currencies:
                dispatcher.utter_message(
                    text=" The " + str(attribute) + " of the country " + str(country) + " is " + str(currencies))
            elif attribute == 'code' and code:
                dispatcher.utter_message(
                    text=" The " + str(attribute) + " of the country " + str(country) + " is " + str(code))
            elif attribute == 'borders' and borders:
                dispatcher.utter_message(
                    text=" The " + str(attribute) + " of the country " + str(country) + " is " + str(borders))
            else:
                dispatcher.utter_message(text="correct your : " + str(attribute) +
                                              " to capital, region, population, area, currencies, code, borders \nAnd country name")
        elif error_msg:
            dispatcher.utter_message(text=str(country) + " value" + str(error_msg))
        elif country_name == '':
            dispatcher.utter_message(text=" Please include country name")
            return [SlotSet('attribute', None)]
        else:
            dispatcher.utter_message(text="The general basic information about country " + str(country) + " are: \n" +
                                          "Captial: " + str(capital) + "\nArea: " + str(area) + "\nPopulation: " +
                                          str(population) + "\nCountry calling code: " + str(code) + "\nCurrency: " +
                                          str(currencies) + "\nCountry location region: " + str(region) +
                                          "\nCountry Boarder: " + str(borders))

        return [SlotSet("country", None), SlotSet('attribute', None)]

