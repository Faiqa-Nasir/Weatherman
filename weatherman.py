from Controllers.weather_detail_parser_controller import WeatherDetailParserController
from helper_functions import extracting_the_weather_files
from Views.weather_detail_parser_view import WeatherDetailParserView
from Services.weather_detail_parser_model import WeatherDetailParserModel
from weather_summary_calculator import WeatherSummaryCalculator

# Call the function to extract files
extracting_the_weather_files()
# dependency injection
view = WeatherDetailParserView()
model = WeatherDetailParserModel()
calculator = WeatherSummaryCalculator()
controller = WeatherDetailParserController(view, model, calculator)
# run the program
controller.display_results_based_upon_user_input()
