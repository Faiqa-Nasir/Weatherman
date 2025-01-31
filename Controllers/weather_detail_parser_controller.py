from Services.weather_detail_parser_model import WeatherDetailParserModel
from Views.weather_detail_parser_view import WeatherDetailParserView
from Helper.weather_summary_calculator import WeatherSummaryCalculator
from Helper.helper_functions import parse_month_input


class WeatherDetailParserController:
    weather_summary_calculate = WeatherSummaryCalculator()  # static member

    def __init__(self, weather_detail_view: WeatherDetailParserView, weather_detail_model: WeatherDetailParserModel):
        self.weather_detail_view = weather_detail_view
        self.weather_detail_model = weather_detail_model

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

    def get_weather_details_of_a_month_as_chart(self, month: list[int]):
        monthly_details = self.weather_detail_model.get_weather_details_of_a_month(
            month)
        return self.weather_summary_calculate.months_per_day_min_max_temp(monthly_details)

    def display_results_based_upon_user_input(self):
        try:
            args = self.weather_detail_view.getting_user_input()

        except Exception as error:
            print("An exception occurred:", error)
            return
        if (args.year):
            for year in args.year:
                yearly_details = self.get_weather_details_of_a_year(
                    year[0])
                self.weather_detail_view.display_yearly_details(
                    yearly_details, year[0])
        if (args.month):
            for month in args.month:
                year_and_month = parse_month_input(month[0])
                monthly_details = self.get_weather_details_of_a_month(
                    year_and_month)
                self.weather_detail_view.display_monthly_details(
                    monthly_details, year_and_month)
        if (args.chart):
            for month in args.chart:
                year_and_month = parse_month_input(month[0])
                monthly_details = self.get_weather_details_of_a_month_as_chart(
                    year_and_month)
                self.weather_detail_view.display_monthly_details_as_a_chart(
                    monthly_details, year_and_month)
