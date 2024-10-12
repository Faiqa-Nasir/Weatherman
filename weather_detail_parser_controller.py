from Services.weather_detail_parser_model import WeatherDetailParserModel
from Views.weather_detail_parser_view import WeatherDetailParserView
from weather_summary_calculator import WeatherSummaryCalculator
from helper_functions import parse_month_input


class WeatherDetailParserController:
    def __init__(self, weather_detail_view: WeatherDetailParserView, weather_detail_model: WeatherDetailParserModel, weather_summary_calculate: WeatherSummaryCalculator):
        self.weather_detail_view = weather_detail_view
        self.weather_detail_model = weather_detail_model
        self.weather_summary_calculate = weather_summary_calculate

    def get_weather_details_of_a_year(self, year: int):
        yearly_details = self.weather_detail_model.get_weather_details_of_a_year(
            year)
        yearly_info = []
        yearly_info.append(
            self.weather_summary_calculate.yearly_min_temp(yearly_details))
        yearly_info.append(
            self.weather_summary_calculate.yearly_max_temp(yearly_details))
        yearly_info.append(
            self.weather_summary_calculate.yearly_max_humidity(yearly_details))
        return yearly_info

    def get_weather_details_of_a_month(self, month: list[int]):
        monthly_details = self.weather_detail_model.get_weather_details_of_a_month(
            month)
        monthly_info = []
        monthly_info.append(
            self.weather_summary_calculate.monthly_min_temp(monthly_details))
        monthly_info.append(
            self.weather_summary_calculate.monthly_max_temp(monthly_details))
        monthly_info.append(
            self.weather_summary_calculate.monthly_max_humidity(monthly_details))
        return monthly_info

    def display_results_based_upon_user_input(self):
        args = self.weather_detail_view.getting_user_input()
        if (args.year):
            for year in args.year:
                yearly_details = self.get_weather_details_of_a_year(
                    year)
                self.weather_detail_view.display_yearly_details(yearly_details)
        elif (args.month):
            for month in args.month:
                year_and_month = parse_month_input(month)
                monthly_details = self.get_weather_details_of_a_month(
                    year_and_month)
                self.weather_detail_view.display_monthly_details(monthly_details)
