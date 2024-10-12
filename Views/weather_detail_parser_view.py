import argparse
from helper_functions import string_to_formatted_date


class WeatherDetailParserView:

    def getting_user_input(self) -> list:
        parser = argparse.ArgumentParser(
            description="Weatherman: A weather data processing tool.")

        parser.add_argument("directory", type=str, nargs='+',
                            help="Path to the weather data files directory")
        parser.add_argument("-e", "--year", type=int, nargs='+',
                            help="Specify the year to filter the data")
        parser.add_argument("-a", "--month", type=str, nargs='+',
                            help="Specify the month to filter the data")
        parser.add_argument("-c", "--chart", type=str, nargs='+',
                            help="Specify the event to filter the data (e.g., Rain, Snow)")
        args = parser.parse_args()
        return args

    def display_yearly_details(self, yearly_info: list) -> None:
        for yearly_detail in yearly_info:
            for description, value in yearly_detail.items():
                if (description == " was recorded on "):
                    value = string_to_formatted_date(value)
                print(description + str(value),end="")
            print('\n')

    def display_monthly_details(self, monthly_info: list) -> None:
        for monthly_detail in monthly_info:
            for description, value in monthly_detail.items():
                if (description == " was recorded on "):
                    value = string_to_formatted_date(value)
                print(description + str(value),end="")
            print('\n')
