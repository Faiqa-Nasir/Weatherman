import os
from helper_functions import creation_of_daily_weather_detail_object
mapping_of_months = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}


class WeatherDetailParserModel:
    def __get_weather_details_of_a_month_from_file(self, filename):
        monthly_weather_data = []
        dir_path = r'C:\\Users\\PMLS\\Desktop\\python\\destination\\weatherfiles\\'

        if os.path.isfile(os.path.join(dir_path, filename)):
            with open(os.path.join(dir_path, filename)) as my_weather_file:
                next(my_weather_file)  # skip the header of file
                for line in my_weather_file:
                    field_values = line.strip().split(',')
                    daily_weather_details = creation_of_daily_weather_detail_object(
                        field_values)
                    monthly_weather_data.append(daily_weather_details)
        else:
            print("File or directory doesn't exist")
        return monthly_weather_data

    def get_weather_details_of_a_month(self, year_and_month: list[int]):
        year = year_and_month[0]
        month = mapping_of_months[str(year_and_month[1])]
        filename = "Murree_weather_"+str(year)+"_"+str(month)+".txt"
        return self.__get_weather_details_of_a_month_from_file(filename)

    def get_weather_details_of_a_year(self, year: int):
        filename = "Murree_weather_"+str(year)+"_"
        dir_path = r'C:\\Users\\PMLS\\Desktop\\python\\destination\\weatherfiles\\'
        yearly_weather_info = []
        for path in os.listdir(dir_path):
            if filename in path:
                months_weather_info = self.__get_weather_details_of_a_month_from_file(
                    path)
                yearly_weather_info.append(months_weather_info)
        return yearly_weather_info
