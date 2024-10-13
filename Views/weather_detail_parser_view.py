import argparse
from Helper.helper_functions import string_to_formatted_date
from Helper.helper_functions import mapping_of_months


class WeatherDetailParserView:

    def getting_user_input(self) -> list:
        parser = argparse.ArgumentParser(
            description="Weatherman: A weather data processing tool.")
        parser.add_argument("directory", type=str, nargs='+',
                            help="Path to the weather data files directory")
        parser.add_argument("-e", "--year", action='append', type=int, nargs='+',
                            help="Specify the year to filter the data")
        parser.add_argument("-a", "--month", action='append', type=str, nargs='+',
                            help="Specify the month to filter the data")
        parser.add_argument("-c", "--chart", action='append', type=str, nargs='+',
                            help="Specify the event to filter the data (e.g., Rain, Snow)")
        args = parser.parse_args()
        return args

    def display_yearly_details(self, yearly_info: list, year: int) -> None:
        print("----------------------------\nWeather Summary of the year " +
              str(year)+" : ", end="\n")
        for yearly_detail in yearly_info:
            for description, value in yearly_detail.items():
                if (description == " was recorded on "):
                    value = string_to_formatted_date(value)
                print(description + str(value), end="")
            print('\n')

    def display_monthly_details(self, monthly_info: list, year_and_month: list) -> None:
        print("----------------------------\nWeather Summary of " +
              mapping_of_months[str(year_and_month[1])]+" in year "+str(year_and_month[0]), end="\n")
        for monthly_detail in monthly_info:
            for description, value in monthly_detail.items():
                if (description == " was recorded on "):
                    value = string_to_formatted_date(value)
                print(description + str(value), end="")
            print('\n')

    def display_monthly_details_as_a_chart(self, monthly_info: list, year_and_month: list) -> None:
        print("----------------------------\nWeather Summary of " +
              mapping_of_months[str(year_and_month[1])]+" in year "+str(year_and_month[0]), end="\n")
        for per_day_detail in monthly_info:
            print(per_day_detail)
