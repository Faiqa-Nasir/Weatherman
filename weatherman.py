from Controllers.weather_detail_parser_controller import WeatherDetailParserController
from Helper.helper_functions import extracting_the_weather_files
from Views.weather_detail_parser_view import WeatherDetailParserView
from Services.weather_detail_parser_model import WeatherDetailParserModel

# Call the function to extract files
extracting_the_weather_files()
# dependency injection
view = WeatherDetailParserView()
model = WeatherDetailParserModel()
controller = WeatherDetailParserController(view, model)

try:
    controller.display_results_based_upon_user_input()
except Exception as error:
    # handle the exception
    print("An exception occurred:", error)
