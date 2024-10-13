from Models.weather_summary_calculator_interface import IWeatherSummaryCalculator


class WeatherSummaryCalculator(IWeatherSummaryCalculator):
    def yearly_min_temp(self, yearly_weather_info: list) -> dict:
        lowest_temp_in_month = float('inf')
        day_with_monthly_lowest_temperature = ""

        for monthly_weather_details in yearly_weather_info:
            for daily_weather_details in monthly_weather_details:

                if daily_weather_details.min_temperature_c is not None and lowest_temp_in_month > daily_weather_details.min_temperature_c:
                    lowest_temp_in_month = daily_weather_details.min_temperature_c
                    day_with_monthly_lowest_temperature = daily_weather_details.pkt

        min_temp_info = {
            "Minimum Temperature : ": lowest_temp_in_month,
            " was recorded on ": day_with_monthly_lowest_temperature
        }
        return min_temp_info

    def yearly_max_temp(self, yearly_weather_info: list) -> dict:
        highest_temp_in_month = float('-inf')
        day_with_monthly_highest_temperature = ""

        for monthly_weather_details in yearly_weather_info:
            for daily_weather_details in monthly_weather_details:
                if daily_weather_details.max_temperature_c is not None and highest_temp_in_month < daily_weather_details.max_temperature_c:
                    highest_temp_in_month = daily_weather_details.max_temperature_c
                    day_with_monthly_highest_temperature = daily_weather_details.pkt

        max_temp_info = {
            "Maximum Temperature : ": highest_temp_in_month,
            " was recorded on ": day_with_monthly_highest_temperature
        }
        return max_temp_info

    def yearly_max_humidity(self, yearly_weather_info: list) -> dict:
        highest_humidity_in_month = float('-inf')
        day_with_monthly_highest_humidity = ""

        for monthly_weather_details in yearly_weather_info:
            for daily_weather_details in monthly_weather_details:
                if daily_weather_details.max_humidity is not None and highest_humidity_in_month < daily_weather_details.max_humidity:
                    highest_humidity_in_month = daily_weather_details.max_humidity
                    day_with_monthly_highest_humidity = daily_weather_details.pkt

        max_humidity_info = {
            "Maximum Humidity : ": highest_humidity_in_month,
            " was recorded on ": day_with_monthly_highest_humidity
        }
        return max_humidity_info

    def monthly_min_temp(self, monthly_weather_info: list) -> dict:
        lowest_temp_in_month = float('inf')
        day_with_monthly_lowest_temperature = ""

        for daily_weather_details in monthly_weather_info:
            if daily_weather_details.min_temperature_c is not None and lowest_temp_in_month > daily_weather_details.min_temperature_c:
                lowest_temp_in_month = daily_weather_details.min_temperature_c
                day_with_monthly_lowest_temperature = daily_weather_details.pkt

        return {
            "Minimum Temperature : ": lowest_temp_in_month,
            " was recorded on ": day_with_monthly_lowest_temperature
        }

    def monthly_max_temp(self, monthly_weather_info: list) -> dict:
        highest_temp_in_month = float('-inf')
        day_with_monthly_highest_temperature = ""

        for daily_weather_details in monthly_weather_info:
            if daily_weather_details.max_temperature_c is not None and highest_temp_in_month < daily_weather_details.max_temperature_c:
                highest_temp_in_month = daily_weather_details.max_temperature_c
                day_with_monthly_highest_temperature = daily_weather_details.pkt

        return {
            "Maximum Temperature : ": highest_temp_in_month,
            " was recorded on ": day_with_monthly_highest_temperature
        }

    def monthly_max_humidity(self, monthly_weather_info: list) -> dict:
        highest_humidity_in_month = float('-inf')
        day_with_monthly_highest_humidity = ""

        for daily_weather_details in monthly_weather_info:
            if daily_weather_details.max_humidity is not None and highest_humidity_in_month < daily_weather_details.max_humidity:
                highest_humidity_in_month = daily_weather_details.max_humidity
                day_with_monthly_highest_humidity = daily_weather_details.pkt

        return {
            "Maximum Humidity : ": highest_humidity_in_month,
            " was recorded on ": day_with_monthly_highest_humidity
        }

    def months_per_day_min_max_temp(self, monthly_weather_info: list):
        months_max_min_temp = []
        for daily_weather_details in monthly_weather_info:
            if daily_weather_details.max_temperature_c is not None or daily_weather_details.min_temperature_c is not None:
                max_temp = "+" * int(daily_weather_details.max_temperature_c)
                per_day_max_min_temp = str(daily_weather_details.min_temperature_c)+str(
                    max_temp)+str(daily_weather_details.max_temperature_c)
                months_max_min_temp.append(per_day_max_min_temp)
        return months_max_min_temp
