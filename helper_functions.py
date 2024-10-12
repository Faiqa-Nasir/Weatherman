from zipfile import ZipFile
import os
from datetime import datetime
from Models.daily_weather_detail import DailyWeatherDetails


def extracting_the_weather_files():
    """
    Extract all the weather files from a zip to the destination folder.
    """

    # Define paths
    zip_file_path = "C:\\Users\\PMLS\\Desktop\\python\\weatherfiles.zip"
    destination_folder = "C:\\Users\\PMLS\\Desktop\\python\\destination"

    # Check if destination folder exists
    if os.path.exists(destination_folder):
        print("Files have already been extracted!\n")
        return

    try:
        # Loading the zip file and creating a zip object
        with ZipFile(zip_file_path, 'r') as zObject:
            # Extracting all the members of the zip into a specific location
            zObject.extractall(path=destination_folder)
            print(f"Files extracted successfully to {destination_folder}\n")
    except FileNotFoundError:
        print(f"Error: The file {zip_file_path} was not found.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")


def parse_month_input(month: str) -> list:
    return list(int(value) for value in month.split('/'))


def string_to_formatted_date(date_string: str):
    date = datetime.strptime(date_string, '%Y-%m-%d').date()
    formatted_date = datetime.strftime(date, '%B %d')
    return formatted_date


def creation_of_daily_weather_detail_object(fields: list[str]) -> DailyWeatherDetails:
    try:
        daily_weather = DailyWeatherDetails(
            pkt=fields[0],  # Date field, assuming it's always present
            max_temperature_c=float(fields[1]) if fields[1] != '' else None,
            mean_temperature_c=float(fields[2]) if fields[2] != '' else None,
            min_temperature_c=float(fields[3]) if fields[3] != '' else None,
            dew_point_c=float(fields[4]) if fields[4] != '' else None,
            mean_dew_point_c=float(fields[5]) if fields[5] != '' else None,
            min_dew_point_c=float(fields[6]) if fields[6] != '' else None,
            max_humidity=float(fields[7]) if fields[7] != '' else None,
            mean_humidity=float(fields[8]) if fields[8] != '' else None,
            min_humidity=float(fields[9]) if fields[9] != '' else None,
            max_sea_level_pressure_hpa=float(
                fields[10]) if fields[10] != '' else None,
            mean_sea_level_pressure_hpa=float(
                fields[11]) if fields[11] != '' else None,
            min_sea_level_pressure_hpa=float(
                fields[12]) if fields[12] != '' else None,
            max_visibility_km=float(fields[13]) if fields[13] != '' else None,
            mean_visibility_km=float(fields[14]) if fields[14] != '' else None,
            min_visibility_km=float(fields[15]) if fields[15] != '' else None,
            max_wind_speed_kmh=float(fields[16]) if fields[16] != '' else None,
            mean_wind_speed_kmh=float(
                fields[17]) if fields[17] != '' else None,
            max_gust_speed_kmh=float(fields[18]) if fields[18] != '' else None,
            precipitation_mm=float(fields[19]) if fields[19] != '' else None,
            cloud_cover=float(fields[20]) if fields[20] != '' else None,
            events=fields[21],  # Events can be a string
            wind_dir_degrees=float(fields[22]) if fields[22] != '' else None
        )
        return daily_weather
    except ValueError as e:
        print(f"Error parsing line: {fields}\nError: {e}")
        return None
