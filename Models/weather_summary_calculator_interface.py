from abc import ABC, abstractmethod
from Helper.singleton_meta import SingletonABCMeta


class IWeatherSummaryCalculator(metaclass=SingletonABCMeta):
    # the calculator is a singleton class and would only be initialized once

    @abstractmethod
    def yearly_min_temp(self, weather_info: list):
        pass

    @abstractmethod
    def yearly_max_temp(self, weather_info: list):
        pass

    @abstractmethod
    def yearly_max_humidity(self, weather_info: list):
        pass

    @abstractmethod
    def monthly_min_temp(self, weather_info: list):
        pass

    @abstractmethod
    def monthly_max_temp(self, weather_info: list):
        pass

    @abstractmethod
    def monthly_max_humidity(self, weather_info: list):
        pass

    @abstractmethod
    def months_per_day_min_max_temp(self, weather_info: list):
        pass
